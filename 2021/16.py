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


def get_version(packet: str) -> int:
    """The packet version is the decimal repr of the
    first three bits"""
    return int(packet[:3], 2)


def get_type(packet: str) -> int:
    """The packet type ID the decimal rep of the
    three bits after the packet version"""
    return int(packet[3:6], 2)


packet = hex_to_bin("38006F45291200")

total_versions = get_version(packet)


def process_packet(packet: str):
    print(get_version(packet))
    if get_type(packet) == 4:
        # literal packet
        literal_packet = packet[6:]
        chunks = [
            literal_packet[i : i + 5]
            for i in range(0, len(literal_packet), 5)
            if len(literal_packet[i : i + 5]) == 5
        ]
    else:
        # operator packet
        if packet[6] == "0":
            # total length ID
            total_length = int(packet[7:22], 2)
            # HOW DO WE SPLIT UP INTO SUBPACKETS?
        elif packet[7] == "1":
            # sub-packet ID
            num_sub_packets = int(packet[7:18], 2)

        else:
            raise ValueError("Packet length ID not 1 or 0")
