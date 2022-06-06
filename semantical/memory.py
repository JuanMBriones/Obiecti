from abc import abstractmethod
from semantical.data_types import DataType

"""
This file contains the memory methods and the segments that are used in the semnatical part of the compiler.
"""
class Segment:
    def __init__(self, lower_bound, upper_bound):
        self.segment = [lower_bound, upper_bound]

    def requestSpace(self):
        if self.segment[0] >= self.segment[1] + 1:
            print("Too many variables")
            exit(-1)
        else:
            address = self.segment[0]
            return address

    def move_next_direction(self):
        self.segment[0] += 1

class Memory:
    @abstractmethod
    def requestSpace(self, type):
        pass

    @abstractmethod
    def move_next_direction(self, type):
        pass


class GlobalMemory(Memory):
    def __init__(self):
        self.int_segment = Segment(0, 99999)
        self.float_segment = Segment(100000, 199999)
        self.char_segment = Segment(200000, 299999)
        self.string_segment = Segment(300000, 399999)
        self.bool_segment = Segment(400000, 499999)

    def requestSpace(self, type):
        try:
            if type == DataType.INT:
                return self.int_segment.requestSpace()
            elif type == DataType.FLOAT:
                return self.float_segment.requestSpace()
            elif type == DataType.CHAR:
                return self.char_segment.requestSpace()
            elif type == DataType.STRING:
                return self.string_segment.requestSpace()
            elif type == DataType.BOOL:
                return self.bool_segment.requestSpace()
            return None
        except:
            print("Too many variables") 

    def move_next_direction(self, type):
        if type == DataType.INT:
            self.int_segment.move_next_direction()
        elif type == DataType.FLOAT:
            self.float_segment.move_next_direction()
        elif type == DataType.CHAR:
            self.char_segment.move_next_direction()
        elif type == DataType.STRING:
            self.string_segment.move_next_direction()
        elif type == DataType.BOOL:
            self.bool_segment.move_next_direction()
            
class LocalMemory(Memory):
    def __init__(self, name):
        if name == "global":
            self.int_segment = Segment(0, 99999)
            self.float_segment = Segment(100000, 199999)
            self.char_segment = Segment(200000, 299999)
            self.string_segment = Segment(300000, 399999)
            self.bool_segment = Segment(400000, 499999)
        else:
            self.int_segment = Segment(500000, 599999)
            self.float_segment = Segment(600000, 699999)
            self.char_segment = Segment(700000, 799999)
            self.string_segment = Segment(800000, 899999)
            self.bool_segment = Segment(900000, 999999)

    def requestSpace(self, type):
        try:
            if type == DataType.INT:
                return self.int_segment.requestSpace()
            elif type == DataType.FLOAT:
                return self.float_segment.requestSpace()
            elif type == DataType.CHAR:
                return self.char_segment.requestSpace()
            elif type == DataType.STRING:
                return self.string_segment.requestSpace()
            elif type == DataType.BOOL:
                return self.bool_segment.requestSpace()
        except:
            print("Too many variables")

    def move_next_direction(self, type):
        if type == DataType.INT:
            self.int_segment.move_next_direction()
        elif type == DataType.FLOAT:
            self.float_segment.move_next_direction()
        elif type == DataType.CHAR:
            self.char_segment.move_next_direction()
        elif type == DataType.STRING:
            self.string_segment.move_next_direction()
        elif type == DataType.BOOL:
            self.bool_segment.move_next_direction()

class TemporalMemory(Memory):
    def __init__(self):
        self.int_segment = Segment(1000000, 1099999)
        self.float_segment = Segment(1100000, 1199999)
        self.char_segment = Segment(1200000, 1299999)
        self.string_segment = Segment(1300000, 1399999)
        self.bool_segment = Segment(1400000, 1499999)
        self.pointer_segment = Segment(1500000, 1599999)

    def requestSpace(self, type):
        try:
            if type == DataType.INT:
                return self.int_segment.requestSpace()
            elif type == DataType.FLOAT:
                return self.float_segment.requestSpace()
            elif type == DataType.CHAR:
                return self.char_segment.requestSpace()
            elif type == DataType.STRING:
                return self.string_segment.requestSpace()
            elif type == DataType.BOOL:
                return self.bool_segment.requestSpace()
            elif type == DataType.POINTER:
                return self.pointer_segment.requestSpace()
            return None
        except:
            print("Too many variables or type doesn't exist")

    def move_next_direction(self, type):
        if type == DataType.INT:
            self.int_segment.move_next_direction()
        elif type == DataType.FLOAT:
            self.float_segment.move_next_direction()
        elif type == DataType.CHAR:
            self.char_segment.move_next_direction()
        elif type == DataType.STRING:
            self.string_segment.move_next_direction()
        elif type == DataType.BOOL:
            self.bool_segment.move_next_direction()
        elif type == DataType.POINTER:
            self.pointer_segment.move_next_direction()

class ConstantsMemory(Memory):
    def __init__(self):
        self.int_segment = Segment(1600000, 1699999)
        self.float_segment = Segment(1700000, 1799999)
        self.char_segment = Segment(1800000, 1899999)
        self.string_segment = Segment(1900000, 1999999)
        self.bool_segment = Segment(2000000, 2099999)

    def requestSpace(self, type):
        try:
            if type == DataType.INT:
                return self.int_segment.requestSpace()
            elif type == DataType.FLOAT:
                return self.float_segment.requestSpace()
            elif type == DataType.CHAR:
                return self.char_segment.requestSpace()
            elif type == DataType.STRING:
                return self.string_segment.requestSpace()
            elif type == DataType.BOOL:
                return self.bool_segment.requestSpace()
            return None
        except:
            print("Too many variables or type doesn't exist")

    def move_next_direction(self, type):
        if type == DataType.INT:
            self.int_segment.move_next_direction()
        elif type == DataType.FLOAT:
            self.float_segment.move_next_direction()
        elif type == DataType.CHAR:
            self.char_segment.move_next_direction()
        elif type == DataType.STRING:
            self.string_segment.move_next_direction()
        elif type == DataType.BOOL:
            self.bool_segment.move_next_direction()
