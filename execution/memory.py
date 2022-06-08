class Memory:
    
    def __init__(self, int, float, char, string, boolean):
        self.ints = [None for i in range(int)]
        self.floats = [None for i in range(float)]
        self.chars = [None for i in range(char)]
        self.string = [None for i in range(string)]
        self.booleans = [None for i in range(boolean)]

        self.debug_ints = [None for i in range(int)]
        self.debug_floats = [None for i in range(float)]
        self.debug_chars = [None for i in range(char)]
        self.debug_string = [None for i in range(string)]
        self.debug_booleans = [None for i in range(boolean)]

    def debug(self):
        return {
            'int': [{'index': index, 'value': self.debug_ints[index]} for index in range(len(self.debug_ints))],
            'float': [{'index': index, 'value': self.debug_floats[index]} for index in range(len(self.debug_floats))],
            'char': [{'index': index, 'value': self.debug_chars[index]} for index in range(len(self.debug_chars))],
            'string': [{'index': index, 'value': self.debug_string[index]} for index in range(len(self.debug_string))],
            'bool': [{'index': index, 'value': self.debug_booleans[index]} for index in range(len(self.debug_booleans))]
        }

    def access_int(self, address):
        #print("Access int:", address)
        #print("Access int self.ints[address]:", self.ints[address])
        return self.ints[address]

    def assign_int(self, address, value, original_address=None):
        #print("Assign int self.ints[address]:", self.ints[address])
        self.debug_ints[address] = {'fixed_address': address, 'original_address': original_address, 'value': value}
        self.ints[address] = value

    def access_float(self, address):
        return self.floats[address]
    
    def assign_float(self, address, value, original_address=None):
        self.debug_floats[address] = {'fixed_address': address, 'original_address': original_address, 'value': value}
        self.floats[address] = value

    def access_char(self, address):
        return self.chars[address]

    def assign_char(self, address,  value, original_address=None):
        self.debug_chars[address] = {'fixed_address': address, 'original_address': original_address, 'value': value}
        self.chars[address] = value

    def access_boolean(self, address):
        return self.booleans[address]

    def assign_boolean(self, address, value, original_address=None):
        self.debug_booleans[address] = {'fixed_address': address, 'original_address': original_address, 'value': value}
        self.booleans[address] = value

class TemporalMemory(Memory):
    def __init__(self, int, float, char, string, boolean):
        super().__init__(int, float, char, string, boolean)
        self.pointers = []
    
    def debug(self):
        vars = super().debug()
        vars['pointers'] = self.pointers
        return vars