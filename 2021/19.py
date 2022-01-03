from collections import defaultdict
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
    def _apply_rotation(beacon: 'Beacon', rotation, repeats):
        rotating_point = np.array([beacon.x, beacon.y, beacon.z])
        for _ in range(repeats):
            rotating_point = rotating_point * rotation
            rotating_point = np.squeeze(np.asarray(rotating_point))

        return Beacon(rotating_point[0], rotating_point[1], rotating_point[2])    

    def rotate(self, x: int, y: int, z: int):
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

    def get_rotations(self):
        rots = []
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    rots.append(self.rotate(x, y, z))
        # uniquify from 64 to 24
        return list(set(rots))

    def to_tuple(self) -> tuple[int, int, int]:
        return (self.x, self.y, self.z)

class Scanner:
    def __init__(self, num: int, beacons: list[Beacon]) -> None:
        self.num = num
        self.beacons = beacons
        self.manhattans = self.get_manhattans()
        # position relative to the 0th scanner
        self.relative_pos: tuple(int, int, int) = tuple()
        # beacons relative to scanner 0
        self.relative_beacons: list[Beacon] = []

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


scanners = parse_input(RAW_TEST)
self_b, other_b, ms = scanners[0].get_overlapping(scanners[1])
scanners[0].relative_pos = (0, 0, 0)

matches = defaultdict(int)
for i in range(len(self_b)):
    diffs = [self_b[i] - r for r in other_b[i].get_rotations()]
    for d in diffs:
        matches[d] += 1
other_b_pos = [m for m in matches.items() if m[1] == 12][0][0]
print(f'Other scanner position: ')