import string
from semantical.data_types import DataType

class Function:
    def __init__(self, data_type, initial_address, size, param_table):
        self.data_type = data_type
        self.initial_address = initial_address
        self.size = size     #[int, float, char, temp_int, temp_float, temp_char]
        self.param_table = param_table

class ProcedureSymbol():
    methods = {}

    def __init__(self, size):
        self.size_good = self.string_to_int_list(size)
        self.param_table = []
        self.methods['global'] = Function(DataType.VOID, None, self.size_good, self.param_table)

    
    def add_method(self, name, data_type, initial_address, size, param_table):
        data_type_good = self.string_to_data_type(data_type)
        initial_address_good = int(initial_address)
        size_good = self.string_to_int_list(size)
        param_table_good = self.string_to_param_table(param_table)
        self.methods[name] = Function(data_type_good, initial_address_good, size_good, param_table_good)

    def get_all_methods(self):
        for key, value in self.methods.items():
            print(f"{key}: {value}")

    def string_to_int_list(self, string):
        string_split = string.strip().strip('[]').split(',')
        new_list = []
        for number in string_split:
            new_list.append(int(number))
        return new_list

    def string_to_data_type(self, string):
        string_stripped = string.strip()
        if string_stripped == 'DataType.VOID':
            return DataType.VOID
        elif string_stripped == 'DataType.INT':
            return DataType.INT
        elif string_stripped == 'DataType.CHAR':
            return DataType.CHAR
    
    def string_to_param_table(self, string):
        string_split = string.strip().strip('[]').split(',')
        if len(string_split) <= 1:
            return []
        else:
            new_list = []
            for type in string_split:
                if type.strip() == '<DataType.INT: \'int\'>':
                    new_list.append(DataType.INT)
                elif type.strip() == '<DataType.FLOAT: \'float\'>':
                    new_list.append(DataType.FLOAT)
                elif type.strip() == '<DataType.CHAR: \'char\'>':
                    new_list.append(DataType.CHAR)
            return new_list

class Constant:
    def __init__(self, value, address):
        self.value = value
        self.address = address

class ConstantTable(Constant):
    def __init__(self):
        self.constants = {}
        
    def add(self, value):
        self.constants[value] = Constant(value, None)

    def get(self, value):
        return self.constants.get(value)

    def get_all_constants(self):
        for key, value in self.constants.items():
            print(f"{key}: {value}")