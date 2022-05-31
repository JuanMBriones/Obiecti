class Memory:
    def __init__(self):
        self.ints = []
        self.floats = []
        self.chars = []
        self.booleans = []

    def accessInt(self, address):
        return self.ints[address]

    def addInt(self, value):
        self.ints.append(value)

    def accessFloat(self, address):
        return self.floats[address]
    
    def addFloat(self, value):
        self.floats.append(value)

    def accessChar(self, address):
        return self.chars[address]

    def addChars(self, value):
        self.chars.append(value)

    def accessBoolean(self, address):
        return self.booleans[address]

    def addBoolean(self, value):
        self.booleans.append(value)