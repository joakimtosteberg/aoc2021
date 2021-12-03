import sys

class Diagnostics:
    def __init__(self):
        self.initialized = False
        self.data = []

    def process_data(self, data):
        self.data.append(data)

    def get_bit_count(self, data):
        bit_count = [0]*len(data[0])
        for row in data:
            for i in range(0,len(row)):
                if row[i]=='1':
                    bit_count[len(row)-i-1] = bit_count[len(row)-i-1] + 1
        return bit_count

    def get_power_diagnostics(self):
        gamma = 0
        epsilon = 0
        bit_count = self.get_bit_count(self.data)
        for i in range(0,len(bit_count)):
            bit_value = self.most_common_value(len(self.data), i, bit_count)
            if bit_value:
                gamma = gamma + 2**i
            else:
                epsilon = epsilon + 2**i
        return gamma, epsilon

    def get_life_support_diagnostics(self):
        oxygen = self.filter_values(data=self.data,
                                    bit_pos=0,
                                    filter_func=self.most_common_value)
        co2 = self.filter_values(data=self.data,
                                 bit_pos=0,
                                 filter_func=self.least_common_value)

        return int(oxygen,2),int(co2,2)

    def most_common_value(self, data_size, bit_pos, bit_count):
        return 1 if bit_count[bit_pos] >= data_size/2 else 0
    
    def least_common_value(self, data_size, bit_pos, bit_count):
        return 0 if bit_count[bit_pos] >= data_size/2 else 1

    def filter_values(self, data, bit_pos, filter_func):
        new_data = []
        bit_count = self.get_bit_count(data)
        bit_value = filter_func(len(data),
                                len(bit_count)-bit_pos-1,
                                bit_count)
        for row in data:
            if int(row[bit_pos]) == bit_value:
                new_data.append(row)
        if len(new_data) == 1:
            return  new_data[0]
        elif not new_data:
            return None
        else:
            return self.filter_values(data=new_data,
                                      bit_pos=bit_pos+1,
                                      filter_func=filter_func)
            

diagnostics = Diagnostics()

with open(sys.argv[1]) as f:
    for line in f:
        diagnostics.process_data(line.strip())


gamma, epsilon = diagnostics.get_power_diagnostics()
print(f"power={gamma*epsilon}")

oxygen, co2 = diagnostics.get_life_support_diagnostics()
print(f"life_support={oxygen*co2}")
