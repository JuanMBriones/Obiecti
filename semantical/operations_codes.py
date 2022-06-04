from abc import abstractmethod
from enum import Enum

class OperationCodes(Enum):
    SUM = 2100000
    MINUS = 2100001
    MULT = 2100002
    DIV = 2100003
    MOD = 2100004
    ASSIGN = 2100005
    LT = 2100006
    GT = 2100007
    LE = 2100008
    GE = 2100009
    EQ = 2100010
    NE = 2100011
    AND = 2100012
    OR = 2100013
    GOTO = 2100014
    GOTOF = 2100015
    ERA = 2100016
    PARAM = 2100017
    GOSUB = 2100018
    ENDFUNC = 2100019
    PRINT = 2100020
    READ = 2100021
    NONE = 2100022
    RETURN = 2100023

    def __new__(cls, value):
        member = object.__new__(cls)
        member._value_ = value

        return member

    def __int__(self):
        return self.value
    
    @classmethod
    def name(cls, val):
        res = [e for e in OperationCodes if e.value == int(val)]
        if res:
            print(res[0].name)
            return res[0]
        else:
            return None

class OperationCodesX:
    @abstractmethod
    def operation_code():
        return {
            '+': 2100000,
            '-': 2100001,
            '*': 2100002,
            '/': 2100003,
            '%': 2100004,
            '=': 2100005,
            '<': 2100006,
            '>': 2100007,
            '<=': 2100008,
            '>=': 2100009,
            '==': 2100010,
            '!=': 2100011,
            '&&': 2100012,
            '||': 2100013,
            'GOTO': 2100014,
            'GOTOF': 2100015,
            'ERA': 2100016,
            'PARAM': 2100017,
            'GOSUB': 2100018,
            'ENDFUNC': 2100019,
            'PRINT': 2100020,
            'READ': 2100021,
            'NONE': 2100022,
            'RETURN': 2100023
        }

    def __init__(self):
        pass
    
    @staticmethod
    def get_op_code(operation):
        codes = OperationCodes.operation_code()
        return codes[operation]
    
    @staticmethod
    def get_operation(op_code):
        print(op_code)
        codes = OperationCodes.operation_code()
        return list(codes.keys())[list(codes.values()).index(op_code)]
