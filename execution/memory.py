class Memory:
    
    def __init__(self, int, float, char, string, boolean):
        self.ints = [None for i in range(int)]
        self.floats = [None for i in range(float)]
        self.chars = [None for i in range(char)]
        self.string = [None for i in range(string)]
        self.booleans = [None for i in range(boolean)]

    def access_int(self, address):
        #print("Access int:", address)
        #print("Access int self.ints[address]:", self.ints[address])
        return self.ints[address]

    def assign_int(self, address, value):
        #print("Assign int self.ints[address]:", self.ints[address])
        self.ints[address] = value

    def access_float(self, address):
        return self.floats[address]
    
    def assign_float(self, address, value):
        self.floats[address] = value

    def access_char(self, address):
        return self.chars[address]

    def assign_char(self, address,  value):
        self.chars[address] = value

    def access_boolean(self, address):
        return self.booleans[address]

    def assign_boolean(self, address, value):
        self.booleans[address] = value

class TemporalMemory(Memory):
    def __init__(self, int, float, char, string, boolean):
        super().__init__(int, float, char, string, boolean)
        self.pointers = []
