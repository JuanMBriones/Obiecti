from semantical.data_types import DataType

class SemanticCube:
    semantic_cube = {
        'sum': {
            (DataType.INT, DataType.INT): DataType.INT,
            (DataType.INT, DataType.FLOAT): DataType.FLOAT,
            (DataType.FLOAT, DataType.INT): DataType.FLOAT,
            (DataType.FLOAT, DataType.FLOAT): DataType.FLOAT
        },
        'sub': {
            (DataType.INT, DataType.INT): DataType.INT,
            (DataType.INT, DataType.FLOAT): DataType.FLOAT,
            (DataType.FLOAT, DataType.INT): DataType.FLOAT,
            (DataType.FLOAT, DataType.FLOAT): DataType.FLOAT
        },
        'mul': {
            (DataType.INT, DataType.INT): DataType.INT,
            (DataType.INT, DataType.FLOAT): DataType.FLOAT,
            (DataType.FLOAT, DataType.INT): DataType.FLOAT,
            (DataType.FLOAT, DataType.FLOAT): DataType.FLOAT
        },
        'div': {
            (DataType.INT, DataType.INT): DataType.FLOAT,
            (DataType.INT, DataType.FLOAT): DataType.FLOAT,
            (DataType.FLOAT, DataType.INT): DataType.FLOAT,
            (DataType.FLOAT, DataType.FLOAT): DataType.FLOAT
        }
    }