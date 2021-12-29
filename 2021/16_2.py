from dataclasses import dataclass
from io import StringIO
from math import prod

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

with open("input_16.txt", "r") as f:
    RAW = f.read().strip()


def hex_to_bin(hex_str: str) -> str:
    bin_str = ""
    for char in hex_str:
        bin_str += hex_to_bin_map[char]
    return bin_str


def read_literal(data: str) -> int:
    total = ""
    while True:
        total += data[1:5]
        if data[0] == "0":
            break
        data = data[5:]
    return int(total, 2)


@dataclass
class Packet:
    type_id: int
    children: list["Packet"]
    val: int


def read(data: StringIO):
    version_str = data.read(3)
    if version_str == "":
        return
    version = int(version_str, 2)
    type_id = int(data.read(3), 2)
    sub_packets = []
    val = None

    if type_id == 4:
        total = ""
        while True:
            padding = data.read(1)
            total += data.read(4)
            if padding == "0":
                break
        val = int(total, 2)

    else:
        length_type_id = data.read(1)
        if length_type_id == "0":
            val = int(data.read(15), 2)
            substream = StringIO(data.read(val))
            while True:
                packet = read(substream)
                if not packet:
                    break
                sub_packets.append(packet)
        elif length_type_id == "1":
            val = int(data.read(11), 2)
            sub_packets = [read(data) for _ in range(val)]

    return Packet(type_id=type_id, children=sub_packets, val=val)


function_map = {
    0: sum,
    1: prod,
    2: min,
    3: max,
    5: lambda x: 1 if x[0] > x[1] else 0,
    6: lambda x: 1 if x[0] < x[1] else 0,
    7: lambda x: 1 if x[0] == x[1] else 0,
}


def unpack(packet: Packet):
    if packet.type_id == 4:
        return packet.val
    operation = function_map[packet.type_id]
    return operation([unpack(c) for c in packet.children])


binary_packet = hex_to_bin(RAW)
root = read(StringIO(binary_packet))
print(unpack(root))
