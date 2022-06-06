from enum import Enum

"""
This class is a representation of the data types in the language. Using Enum
"""
class DataType(Enum):
    INT = 'int'
    FLOAT = 'float'
    BOOL = 'bool'
    STRING = 'string'
    VOID = 'void'
    CHAR = 'char'
    POINTER = 'pointer'
    