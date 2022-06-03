from semantical.data_types import DataType

class SemanticCube:
    semantic_cube = {
        '+': {
            (DataType.INT, DataType.INT): DataType.INT,
            (DataType.INT, DataType.FLOAT): DataType.FLOAT,
            (DataType.FLOAT, DataType.INT): DataType.FLOAT,
            (DataType.FLOAT, DataType.FLOAT): DataType.FLOAT,
            (DataType.CHAR, DataType.CHAR): DataType.CHAR
        },
        '-': {
            (DataType.INT, DataType.INT): DataType.INT,
            (DataType.INT, DataType.FLOAT): DataType.FLOAT,
            (DataType.FLOAT, DataType.INT): DataType.FLOAT,
            (DataType.FLOAT, DataType.FLOAT): DataType.FLOAT
        },
        '*': {
            (DataType.INT, DataType.INT): DataType.INT,
            (DataType.INT, DataType.FLOAT): DataType.FLOAT,
            (DataType.FLOAT, DataType.INT): DataType.FLOAT,
            (DataType.FLOAT, DataType.FLOAT): DataType.FLOAT
        },
        '/': {
            (DataType.INT, DataType.INT): DataType.FLOAT,
            (DataType.INT, DataType.FLOAT): DataType.FLOAT,
            (DataType.FLOAT, DataType.INT): DataType.FLOAT,
            (DataType.FLOAT, DataType.FLOAT): DataType.FLOAT
        },
        '%': {
            (DataType.INT, DataType.INT): DataType.INT,
            (DataType.FLOAT, DataType.FLOAT): DataType.FLOAT
        },
        '=': {
            (DataType.INT, DataType.INT): DataType.INT,
            (DataType.FLOAT, DataType.FLOAT): DataType.FLOAT,
            (DataType.FLOAT, DataType.INT): DataType.FLOAT,
            (DataType.CHAR, DataType.CHAR): DataType.CHAR
        },
        '>': {
            (DataType.INT, DataType.INT): DataType.BOOL,
            (DataType.FLOAT, DataType.FLOAT): DataType.BOOL,
            (DataType.INT, DataType.FLOAT): DataType.BOOL,
            (DataType.FLOAT, DataType.INT): DataType.BOOL
        },
        '<': {
            (DataType.INT, DataType.INT): DataType.BOOL,
            (DataType.FLOAT, DataType.FLOAT): DataType.BOOL,
            (DataType.INT, DataType.FLOAT): DataType.BOOL,
            (DataType.FLOAT, DataType.INT): DataType.BOOL
        },
        '<=': {
            (DataType.INT, DataType.INT): DataType.BOOL,
            (DataType.FLOAT, DataType.FLOAT): DataType.BOOL,
            (DataType.INT, DataType.FLOAT): DataType.BOOL,
            (DataType.FLOAT, DataType.INT): DataType.BOOL
        },
        '>=': {
            (DataType.INT, DataType.INT): DataType.BOOL,
            (DataType.FLOAT, DataType.FLOAT): DataType.BOOL,
            (DataType.INT, DataType.FLOAT): DataType.BOOL,
            (DataType.FLOAT, DataType.INT): DataType.BOOL
        },
        '==': {
            (DataType.INT, DataType.INT): DataType.BOOL,
            (DataType.FLOAT, DataType.FLOAT): DataType.BOOL,
            (DataType.INT, DataType.FLOAT): DataType.BOOL,
            (DataType.FLOAT, DataType.INT): DataType.BOOL,
            (DataType.BOOL, DataType.BOOL): DataType.BOOL
        },
        '!=': {
            (DataType.INT, DataType.INT): DataType.BOOL,
            (DataType.FLOAT, DataType.FLOAT): DataType.BOOL,
            (DataType.INT, DataType.FLOAT): DataType.BOOL,
            (DataType.FLOAT, DataType.INT): DataType.BOOL,
            (DataType.BOOL, DataType.BOOL): DataType.BOOL
        },
        'and': {
            (DataType.BOOL, DataType.BOOL): DataType.BOOL
        },
        'or': {
            (DataType.BOOL, DataType.BOOL): DataType.BOOL
        } 
    }

    def validate(self, operator, type1, type2):
        try:
            if operator in self.semantic_cube:
                return self.semantic_cube[operator][(type1, type2)] 
            else:
                raise Exception("Invalid combination")
        except:
            return None