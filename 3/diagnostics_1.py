import sys

class Diagnostics:
    def __init__(self):
        self.initialized = False
        self.bit_count = []
        self.length = 0

    def initialize(self, data):
        if self.initialized:
            return
        self.initialized = True
        self.bit_count = [0]*len(data)
        self.length = 0

    def process_data(self, data):
        self.initialize(data)
        for i in range(0,len(data)):
            if data[i]=='1':
                self.bit_count[len(data)-i-1] = self.bit_count[len(data)-i-1] + 1
        self.length = self.length + 1

    def get_diagnostics(self):
        gamma = 0
        epsilon = 0
        for i in range(0,len(self.bit_count)):
            bit_value = 1 if self.bit_count[i] > self.length/2 else 0
            if bit_value:
                gamma = gamma + 2**i
            else:
                epsilon = epsilon + 2**i
        return gamma, epsilon

diagnostics = Diagnostics()

with open(sys.argv[1]) as f:
    for line in f:
        diagnostics.process_data(line.strip())


gamma, epsilon = diagnostics.get_diagnostics()
print(f"solution={gamma*epsilon}")
