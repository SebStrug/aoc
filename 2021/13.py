RAW_TEST = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""

with open('input_13.txt', 'r') as f:
    RAW = f.read()
    
data = RAW.splitlines()

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"
    
    @classmethod
    def from_string(cls, string: str) -> 'Point':
        x, y = string.split(',')
        return cls(int(x), int(y))

    def to_tuple(self) -> tuple:
        return self.x, self.y

point_strings = [line for line in data if ',' in line]
points = [Point.from_string(point_string) for point_string in point_strings]
instructions = [line for line in data if line.startswith('fold')]


def fold_along_y(y: int, point: Point) -> Point:
    """To reflect along x axis (x, y) -> (x, -y)
    Only reflect points that have a y bigger than the val
    """
    if point.y < y:
        return point
    point.y = (2*y) - point.y
    return point

def fold_along_x(x: int, point: Point) -> Point:
    """To reflect along y axis (x, y) -> (-x, y)"""
    if point.x < x:
        return point
    point.x = (2 * x) - point.x
    return point

for instr in [instructions[0]]:
    val = int(instr.split('=')[1])
    if instr.startswith('fold along y'):
        points = [fold_along_y(val, point) for point in points]            
    elif instr.startswith('fold along x'):
        points = [fold_along_x(val, point) for point in points]

p_tuples = set(point.to_tuple() for point in points)
print(list(sorted(list(p_tuples))))
print(len(set(p_tuples)))