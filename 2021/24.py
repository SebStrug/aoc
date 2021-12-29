# 14 instructions, all very similar

# each 'inp' inputs the next character
# of the 14 digit number (1-9 allowed only)

# deleted instructions that are `div z 1`, these don't do anything

# instructions only differ on third line (add x ...)
# and the third line from the end (add y ...)

# each instruction...
# starts by setting x and y to 0 before they are used (mul x 0)

# the use of mod strongly hints that we are in base 26

with open('input_24.txt', 'r') as f:
    RAW = f.read()

lines = RAW.split('inp w\n')[1:]
div_z, add_x, add_y = [], [], []
for l in lines:
    instr = l.split('\n')
    div_z.append(instr[3].split(' ')[-1])
    add_x.append(instr[4].split(' ')[-1])
    add_y.append(instr[14].split(' ')[-1])

for a, b, c in zip(div_z, add_x, add_y):
    print(a, b, c)
    # the z divisor is 1 if add_x is positive, otherwise it's 26

def instr(z: int, w: int, div_z: int, add_x: int, add_y: int) -> int:
    x = ((z % 26) + add_x) != w # if x and digit are equal, x is set to 1 but then compared to 0
    z = z // div_z # div z is either 1 or 26, i.e. like base 26
    z *= (25 * x) + 1 # i.e. z *= 26 or z
    z += (w + add_y) * x # i.e. y = 0 or y = (digit + add_y)

# if we're considering a stack of base-26 numbers:
# a modulo is a peek
# a division is a pop
# a multiplication is a push