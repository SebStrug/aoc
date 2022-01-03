from collections import defaultdict, deque
from typing import Optional
import numpy as np

with open("input_19.txt", "r") as f:
    RAW = f.read()

with open("input_19_test.txt", "r") as f:
    RAW_TEST = f.read()

with open("input_19_test_orientations.txt", "r") as f:
    RAW_TEST_ORIENT = f.read()


class Beacon:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Beacon({self.x}, {self.y}, {self.z})"

    def get_manhattan_dist(self, other: "Beacon") -> int:
        """Calculate the Manhattan distance between one point and another"""
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def __sub__(self, other: "Beacon") -> "Beacon":
        return Beacon(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other: "Beacon") -> "Beacon":
        return Beacon(self.x + other.x, self.y + other.y, self.z + other.z)

    def __eq__(self, other: "Beacon") -> bool:
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

    @staticmethod
    def _apply_rotation(beacon: 'Beacon', rotation, repeats) -> 'Beacon':
        rotating_point = np.array([beacon.x, beacon.y, beacon.z])
        for _ in range(repeats):
            rotating_point = rotating_point * rotation
            rotating_point = np.squeeze(np.asarray(rotating_point))

        return Beacon(rotating_point[0], rotating_point[1], rotating_point[2])    

    def rotate(self, x: int, y: int, z: int) -> 'Beacon':
        """https://en.wikipedia.org/wiki/Rotation_matrix#In_three_dimensions
        Using the above formulas setting theta to 90deg.
        """
        rotate_x_transform = np.matrix([
            [1, 0, 0],
            [0, 0 ,-1],
            [ 0, 1, 0]
        ])

        rotate_y_transform = np.matrix([
            [0, 0, 1],
            [0, 1, 0],
            [-1, 0, 0]
        ])

        rotate_z_transform = np.matrix([
            [0, -1, 0],
            [1, 0, 0],
            [0, 0, 1]
        ])

        new_point = self._apply_rotation(self, rotate_x_transform, x)
        new_point = self._apply_rotation(new_point, rotate_y_transform, y)
        new_point = self._apply_rotation(new_point, rotate_z_transform, z)
        return new_point  

    def get_rotations(self) -> dict['Beacon', list[tuple[int, int, int]]]:
        beacons = defaultdict(list)
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    new_beacon = self.rotate(x, y, z)
                    beacons[new_beacon].append((x, y, z))
        # uniquify from 64 to 24
        return beacons

    def to_tuple(self) -> tuple[int, int, int]:
        return (self.x, self.y, self.z)

ORIGIN = Beacon(0, 0, 0)
class Scanner:
    
    def __init__(self, num: int, beacons: list[Beacon], scanner_position: Beacon = ORIGIN) -> None:
        self.num = num
        self.beacons = beacons
        self.manhattans = self.get_manhattans()
        self.scanner_position: Beacon = scanner_position
        # position relative to the 0th scanner
        # beacons relative to scanner 0
        self.relative_beacons: list[Beacon] = []

    def reorientate(self, orientation=(0,0,0), offset=ORIGIN) -> 'Scanner':
        x, y, z = orientation
        new_points = tuple([
            point.rotate(x, y, z) + offset
            for point
            in self.beacons
        ])
        new_scanner_position = self.scanner_position.rotate(orientation[0], orientation[1], orientation[2]) + offset
        
        return Scanner(
            num=self.num,
            beacons=new_points,
            scanner_position=new_scanner_position  
        )

    def __repr__(self):
        return f"Scanner {self.num} (beacons={self.beacons})"

    def get_manhattans(self) -> tuple[tuple[int, ...]]:
        """Calculate the manhattan distance from each beacon to each other beacon
        Return tuples which are hashable
        """
        manhattans = []
        for beacon in self.beacons:
            manhattan_b = [beacon.get_manhattan_dist(b) for b in self.beacons]
            manhattans.append(manhattan_b)
        return tuple(tuple(m) for m in manhattans)

    def get_overlapping(self, other: "Scanner") -> tuple[list, list, list]:
        """Get the beacons that overlap between two scanners

        Returns:
            - overlapping beacons from the class instance
            - overlapping beacons from the scanner passed as argument
            - manhattan distance per beacon
        """
        # Create separate lists so we have a 1:1 correspondence of beacons per scanner
        self_beacons, other_beacons, valid_ms = [], [], []
        for self_ind, self_m in enumerate(self.manhattans):
            for other_ind, other_m in enumerate(other.manhattans):
                # Must be at least 12 overlapping
                if sum(1 for m in self_m if m in other_m) >= 12:
                    self_beacons.append(self.beacons[self_ind])
                    other_beacons.append(other.beacons[other_ind])
                    valid_ms.append(self_m)
        return self_beacons, other_beacons, valid_ms


def parse_input(input: str) -> list[Scanner]:
    scanners = []
    for line in input.split("--- scanner "):
        if line == "":
            continue
        num_, beacons_coords = line.split(" ---\n")
        beacons = []
        for b in beacons_coords.strip().split("\n"):
            x_, y_, z_ = map(int, b.split(","))
            beacons.append(Beacon(x_, y_, z_))
        scanners.append(Scanner(num_, beacons))
    return scanners

def process_scanner(original: Scanner, to_process: Scanner):
    # get the matching beacons from original (reference) scanner and
    # the scanner to process, in order
    self_b, other_b, ms = original.get_overlapping(to_process)
    all_diffs = {}
    matches = defaultdict(int)
    for i in range(len(self_b)):
        rotations = other_b[i].get_rotations()
        # track the differences given all rotations, the difference
        # that occurs 12 times is the valid one
        diffs = {(self_b[i] - r): v for r, v in rotations.items()}
        for d in diffs.keys():
            matches[d] += 1
        all_diffs.update(diffs)
    good_matches = [m for m in matches.items() if m[1] == 12]
    if not good_matches:
        return None
    other_b_pos, _ = good_matches[0]
    # rotations represented here are isomorphic
    required_rotation = all_diffs[other_b_pos][0]
    # update all beacons of the scanner to process relative to original scanner
    return to_process.reorientate(orientation=required_rotation, offset=other_b_pos)

scanners = parse_input(RAW)

q = deque(scanners[1:])
good_scanners = [scanners[0]]
while q:
    print(f'Num good scanners: {len(good_scanners)}')
    s_to_process = q.pop()
    for s in good_scanners:
        new_s = process_scanner(s, s_to_process)
        if new_s:
            good_scanners.append(new_s)
            break
    else:
        q.appendleft(s_to_process)

# scanner0 = scanners[0]
# scanner1 = process_scanner(scanner0, scanners[1])
# scanner4 = process_scanner(scanner1, scanners[4])

all_beacons = []
for s in good_scanners:
    all_beacons.extend(s.beacons)
print(len(set(all_beacons)))

from itertools import combinations
all_combos = list(combinations((s.scanner_position for s in good_scanners), 2))
dists = [a.get_manhattan_dist(b) for a,b in all_combos]