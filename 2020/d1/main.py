with open('input.txt', 'r') as f:
    raw = f.readlines()

data = [int(i.strip()) for i in raw]

# Problem 1
for num in data:
    for nim in data:
        # Problem 2
        for nab in data:
            if num + nim + nab == 2020:
                print(num*nim*nab)
                exit()
