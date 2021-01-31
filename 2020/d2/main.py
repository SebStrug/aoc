with open('input.txt') as f:
    raw = f.readlines()

# Problem 1
good_lines = 0
for line in raw:
    line = line.strip()
    min_ = int(line.split('-')[0])
    max_ = int(line.split('-')[1].split()[0])
    letter = line.split()[1].split(':')[0]
    string = line.rsplit()[-1]

    occurrences = string.count(letter)
    if occurrences >= min_ and occurrences <= max_:
        good_lines += 1
print(good_lines)

# Problem 2
good_lines = 0
for line in raw:
    line = line.strip()
    min_ = int(line.split('-')[0])
    max_ = int(line.split('-')[1].split()[0])
    letter = line.split()[1].split(':')[0]
    string = line.rsplit()[-1]

    if string[min_ - 1] == letter and string[max_ - 1] == letter:
        continue
    elif string[min_ - 1] == letter or string[max_ - 1] == letter:
        good_lines += 1
print(good_lines)