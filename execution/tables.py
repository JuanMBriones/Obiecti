from semantical.data_types import DataType

class Function:
    def __init__(self, data_type, initial_address, size, param_table):
        self.data_type = data_type
        self.initial_address = initial_address
        self.size = size     #[int, float, char, temp_int, temp_float, temp_char]
        self.param_table = param_table
        print(self.size, self.param_table)

class ProcedureSymbol():
    methods = {}

    def __init__(self, size):
        self.size_good = self.string_to_int_list(size)
        self.param_table = []
        self.methods['global'] = Function(DataType.VOID, None, self.size_good, self.param_table)


    def string_to_int_list(self, string):
        string_split = string.strip().strip('[]').split(',')
        new_list = []
        for number in string_split:
            new_list.append(int(number))
        return new_list

