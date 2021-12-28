from typing import Optional

with open('input_19.txt', 'r') as f:
    RAW = f.read()

with open('input_19_test.txt', 'r') as f:
    RAW_TEST = f.read()

with open('input_19_test_orientations.txt', 'r') as f:
    RAW_TEST_ORIENT = f.read()

class Beacon:
    def __init__(self, x: int, y: int, z: int) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f'Beacon({self.x}, {self.y}, {self.z})'

    def get_manhattan_dist(self, other: 'Beacon') -> int:
        """Calculate the Manhattan distance between one point and another"""
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def __eq__(self, other: 'Beacon') -> bool:
        return (self.x == other.x) and (self.y == other.y) and (self.z == other.z)

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))

class Scanner:
    def __init__(self, num: int, beacons: list[Beacon]) -> None:
        self.num = num
        self.beacons = beacons
        self.manhattans = self.get_manhattans()
        # position relative to the 0th scanner
        self.relative_pos: tuple(int, int, int) = tuple()
    
    def __repr__(self):
        return f'Scanner {self.num} (beacons={self.beacons})'

    def get_manhattans(self) -> tuple[tuple[int, ...]]:
        """Calculate the manhattan distance from each beacon to each other beacon
        Return tuples which are hashable
        """
        manhattans = []
        for beacon in self.beacons:
            manhattan_b = [beacon.get_manhattan_dist(b) for b in self.beacons]
            manhattans.append(manhattan_b)
        return tuple(tuple(m) for m in manhattans)

    def get_overlapping(self, other: 'Scanner') -> tuple[list, list, list]:
        self_beacons, other_beacons, valid_ms = [], [], []
        for self_ind, self_m in enumerate(self.manhattans):
            for other_ind, other_m in enumerate(other.manhattans):
                # Must be at least 12 overlapping
                if sum(1 for m in self_m if m in other_m) >= 12:
                    self_beacons.append(self.beacons[self_ind])
                    other_beacons.append(other.beacons[other_ind])
                    valid_ms.append(self_m)
        return self_beacons, other_beacons, valid_ms

    def get_relative_pos(self, other: 'Scanner') -> tuple[int, int, int]:
        self_b, other_b, _ = self.get_overlapping(other)
        # how do you figure out the relative position?

def parse_input(input: str) -> list[Scanner]:
    scanners = []
    for line in input.split('--- scanner '):
        if line == '':
            continue
        num_, beacons_coords = line.split(' ---\n')
        beacons = []
        for b in beacons_coords.strip().split('\n'):
            x_, y_, z_ = map(int, b.split(','))
            beacons.append(Beacon(x_, y_, z_))
        scanners.append(Scanner(num_, beacons))
    return scanners

scanners = parse_input(RAW_TEST)
self_b, other_b, ms = scanners[0].get_overlapping(scanners[1])
# need to figure out the relative position of each set of beacons, so you can update
# the positions of each scanners beacons to be relative to the 0th scanner...!