import io

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


def hex_to_bin(hex_str: str) -> str:
    bin_str = ""
    for char in hex_str:
        bin_str += hex_to_bin_map[char]
    return bin_str

def process_literal(literal: io.StringIO):
    total = ''
    while True:
        chunk = literal.read(5)
        if len(chunk) < 5:
            break
        total += chunk[1:]
    return int(total, 2)

def read_packet(packet: io.StringIO):
    version_str = packet.read(3)
    if version_str == '':
        return
    version = int(version_str, 2)
    print(f'{version=}')

    packet_type = int(packet.read(3), 2)
    print(f'{packet_type=}')
    if packet_type == 4:
        # literal packet
        literal = process_literal(packet)
        print(f'{literal=}')
        return read_packet(packet)
    else:
        # operator packet
        length_type = packet.read(1)
        print(f'{length_type=}')
        if length_type == '0':
            # length type ID
            length = int(packet.read(15), 2)
            return read_packet(io.StringIO(packet.read(length)))
        elif length_type == '1':
            sub_packets = int(packet.read(11), 2)
            return read_packet(io.StringIO(packet.read()))

packet_str = hex_to_bin("38006F45291200")
packet = io.StringIO(packet_str)
print(read_packet(packet))