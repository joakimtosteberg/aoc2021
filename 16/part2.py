import sys
import math

VERSION_LEN = 3
TYPE_LEN = 3
LITERAL_LEN = 5
LENGTH_TYPE_LEN = 1
PACKET_TYPE_LITERAL = 4
PACKET_LENGTH_TYPE_BITS = 0
PACKET_LENGTH_TYPE_PACKETS = 1

SUB_PACKETS_BITS_LENGTH = 15
SUB_PACKETS_COUNT_LENGTH = 11

def greater(values):
    return 1 if values[0] > values[1] else 0

def less(values):
    return 1 if values[0] < values[1] else 0

def equal(values):
    return 1 if values[0] == values[1] else 0

operations = {0: sum,
              1: math.prod,
              2: min,
              3: max,
              5: greater,
              6: less,
              7: equal}


class Packet:
    def __init__(self, packet_version, packet_type):
        self.packet_version = packet_version
        self.packet_type = packet_type
        self.subpackets = []

    def get_subpackets(self):
        return self.subpackets

class LiteralPacket(Packet):
    def __init__(self, packet_version, packet_type, value):
        super().__init__(packet_version, packet_type)
        self.value = value

    def __str__(self):
        return f"version={self.packet_version}, type={self.packet_type}, value={self.value}"

    def calculate(self):
        return self.value


class OperatorPacket(Packet):
    def __init__(self, packet_version, packet_type, subpackets):
        super().__init__(packet_version, packet_type)
        self.subpackets = subpackets

    def __str__(self):
        data = f"version={self.packet_version}, type={self.packet_type}, num_sub={len(self.subpackets)}\n"
        for packet in self.subpackets:
            data = data + str(packet) + "\n"
        return data

    def calculate(self):
        values = [packet.calculate() for packet in self.subpackets]
        res = operations[self.packet_type](values)
#        print(f"op={self.packet_type} values={values} res={res}")
        return res

class Parser:
    def __init__(self, data, length, start = 0):
        self.data = data
        self.start = start
        self.pos = start
        self.end = self.pos + length

    def parse_version(self):
        packet_version = int(self.data[self.pos:self.pos+VERSION_LEN],2)
        self.pos = self.pos + VERSION_LEN
        return packet_version

    def parse_type(self):
        packet_type = int(self.data[self.pos:self.pos+TYPE_LEN],2)
        self.pos = self.pos + TYPE_LEN
        return packet_type

    def parse_literal(self):
        literal_data = ""
        more_data = True
        while more_data:
            literal_part = self.data[self.pos:self.pos+LITERAL_LEN]
            literal_data = literal_data + literal_part[1:LITERAL_LEN]
            self.pos = self.pos + LITERAL_LEN
            more_data = (literal_part[0] == '1')
        self.end = self.pos
        return int(literal_data,2)

    def parse_length_type(self):
        packet_length_type = int(self.data[self.pos:self.pos+LENGTH_TYPE_LEN],2)
        self.pos = self.pos + LENGTH_TYPE_LEN
        return packet_length_type

    def parse_operator(self):
        subpackets = []
        packet_length_type = self.parse_length_type()
        if packet_length_type == PACKET_LENGTH_TYPE_BITS:
            sub_packets_bits = int(self.data[self.pos:self.pos+SUB_PACKETS_BITS_LENGTH],2)
            self.pos = self.pos + SUB_PACKETS_BITS_LENGTH
            while sub_packets_bits > 0:
                parser = Parser(self.data, sub_packets_bits, start=self.pos)
                packet = parser.parse()
                sub_packets_bits = sub_packets_bits - (parser.end - parser.start)
                self.pos = parser.end
                subpackets.append(packet)
        elif packet_length_type == PACKET_LENGTH_TYPE_PACKETS:
            num_sub_packets = int(self.data[self.pos:self.pos+SUB_PACKETS_COUNT_LENGTH],2)
            self.pos = self.pos + SUB_PACKETS_COUNT_LENGTH
            for i in range(0,num_sub_packets):
                parser = Parser(self.data, len(self.data[self.pos:]), start=self.pos)
                packet = parser.parse()
                self.pos = parser.end
                subpackets.append(packet)
        else:
            print(f"Unhandled length type {packet_length_type}")
        self.end = self.pos
        return subpackets

    def parse(self):
        packet_version = self.parse_version()
        packet_type = self.parse_type()
        if packet_type == PACKET_TYPE_LITERAL:
            return LiteralPacket(packet_version,
                                 packet_type,
                                 self.parse_literal())
        else:
            return OperatorPacket(packet_version,
                                  packet_type,
                                  self.parse_operator())
        

def to_binary(hex_data):
    binary_data = bin(int(hex_data, 16))[2:]
    leading_hex_zeroes = 0
    while hex_data[leading_hex_zeroes] == "0":
        leading_hex_zeroes = leading_hex_zeroes + 1
    leading_zeroes = 4*leading_hex_zeroes + (6-len(bin(int(hex_data[leading_hex_zeroes], 16))))
         
    return "0"*leading_zeroes + binary_data


def sum_versions(packets):
    version_sum = 0
    for packet in packets:
        version_sum = version_sum + packet.packet_version + sum_versions(packet.get_subpackets())
    return version_sum
    
    
with open(sys.argv[1]) as f:
    for line in f:
        data = to_binary(line.strip())
        parser = Parser(data, len(data))
        packet = parser.parse()

        print(packet.calculate())
