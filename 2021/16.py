hex_to_bin_map = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

with open('input_16.txt', 'r') as f:
    RAW = f.read().strip()

def hex_to_bin(hex_str: str) -> str:
    bin_str = ""
    for char in hex_str:
        bin_str += hex_to_bin_map[char]
    return bin_str

def read_literal(data: str) -> int:
    total = ''
    while True:
        total += data[1:5]
        if data[0] == '0':
            break
        data = data[5:]
    return int(total, 2)



total_version = 0

def read(data: str) -> str:
    global total_version
    total_version += int(data[:3], 2)
    data = data[3:]

    type_id = int(data[:3], 2)
    data = data[3:]
    if type_id == 4:
        total = ''
        while True:
            total += data[1:5]
            padding = data[0]
            data = data[5:]
            if padding == '0':
                break
    else:
        length_type_id = data[0]
        data = data[1:]
        if length_type_id == '0':
            total_length = int(data[:15], 2)
            data = data[15:]
            sub_packets = read(data[:total_length])
            while sub_packets:
                sub_packets = read(sub_packets)
            data = data[total_length:]

        elif length_type_id == '1':
            num_packets = int(data[:11], 2)
            data = data[11:]
            for _ in range(num_packets):
                data = read(data)
    return data


packet = hex_to_bin(RAW)
read(packet)
print(total_version)