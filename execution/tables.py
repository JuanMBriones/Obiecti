import string
from execution.memory import Memory, TemporalMemory
from semantical.data_types import DataType

class Function:
    def __init__(self, name, data_type, initial_address, size, param_table):
        self.name = name
        self.data_type = data_type
        self.initial_address = initial_address
        self.size = size     #[int, float, char, temp_int, temp_float, temp_char]
        self.param_table = param_table
        self.local_memory = Memory(self.size[0], self.size[1], self.size[2], self.size[3], self.size[4])
        self.temp_memory = TemporalMemory(self.size[5], self.size[6], self.size[7], self.size[8], self.size[9])
    
    def debug(self):
        return {
            'initial_address': self.initial_address,
            'size': self.size,
            'params': self.param_table,
            'local_memory': self.local_memory.debug(),
            'temp_memory': self.temp_memory.debug()
        }

    def set_value(self, address, value):
        '''Asigna un valor a una dirección en memoria. Se realiza
        asociando una dirección virtual a una dirección real
        
        La asociación es la siguiente:
        - Si es una dirección menor a 500000, es una variable global:
            - Si es una dirección entre 0 y 100000, es una variable int
            - Si es una dirección entre 100000 y 200000, es una variable float
            - Si es una dirección entre 200000 y 300000, es una variable char
            - Si es una dirección entre 300000 y 400000, es una variable string
            - Si es una dirección entre 400000 y 500000, es una variable bool
        - Si es una dirección entre 500000 y 1000000, es una variable local:
            - Si es una dirección entre 500000 y 600000, es una variable int
            - Si es una dirección entre 600000 y 700000, es una variable float
            - Si es una dirección entre 700000 y 800000, es una variable char
            - Si es una dirección entre 800000 y 900000, es una variable string
            - Si es una dirección entre 900000 y 1000000, es una variable bool
        - Si es una dirección entre 1000000 y 1600000, es una variable temporal:
            - Si es una dirección entre 1000000 y 1100000, es una variable int
            - Si es una dirección entre 1100000 y 1200000, es una variable float
            - Si es una dirección entre 1200000 y 1300000, es una variable char
            - Si es una dirección entre 1300000 y 1400000, es una variable string
            - Si es una dirección entre 1400000 y 1500000, es una variable bool
            - Si es una dirección entre 1500000 y 1600000, es una variable pointer
        '''
        if address < 500000:        #   Variable global
            if address >= 0 and address < 100000:
                self.local_memory.assign_int(address, value, address)
            elif address >= 100000 and address < 200000:
                real_address = address - 100000
                self.local_memory.assign_float(real_address, value, address)
            elif address >= 200000 and address < 300000:
                real_address = address - 200000
                self.local_memory.assign_char(real_address, value, address)
            elif address >= 400000 and address < 500000:
                real_address = address - 400000
                self.local_memory.assign_boolean(real_address, value, address)
        elif address < 1000000:     #   Variable local
            if address >= 500000 and address < 600000:
                real_address = address - 500000
                self.local_memory.assign_int(real_address, value, address)
            elif address >= 600000 and address < 700000:
                real_address = address - 600000
                self.local_memory.assign_float(real_address, value, address)
            elif address >= 700000 and address < 800000:
                real_address = address - 700000
                self.local_memory.assign_char(real_address, value, address)
            elif address >= 900000 and address < 1000000:
                real_address = address - 900000
                self.local_memory.assign_boolean(real_address, value, address)
        elif address < 1600000:     #   Variable temporal
            if address >= 1000000 and address < 1100000:
                real_address = address - 1000000
                self.temp_memory.assign_int(real_address, value, address)
            elif address >= 1100000 and address < 1200000:
                real_address = address - 1100000
                self.temp_memory.assign_float(real_address, value, address)
            elif address >= 1200000 and address < 1300000:
                real_address = address - 1200000
                self.temp_memory.assign_char(real_address, value, address)
            elif address >= 1400000 and address < 1500000:
                real_address = address - 1400000
                self.temp_memory.assign_boolean(real_address, value, address)

    def get_value(self, address):
        '''Obtiene el valor de una dirección virtual dentro de una función
        o dentro de la memoria global'''
        #print("Get value address:", address)
        if address < 500000:
            if address >= 0 and address < 100000:
                return self.local_memory.access_int(address)
            elif address >= 100000 and address < 200000:
                real_address = address - 100000
                return self.local_memory.access_float(real_address)
            elif address >= 200000 and address < 300000:
                real_address = address - 200000
                return self.local_memory.access_char(real_address)
            elif address >= 400000 and address < 500000:
                real_address = address - 400000
                return self.local_memory.access_boolean(real_address)
        elif address < 1000000:
            if address >= 500000 and address < 600000:
                real_address = address - 500000
                #print("Real address:", real_address)
                return self.local_memory.access_int(real_address)
            elif address >= 600000 and address < 700000:
                real_address = address - 600000
                return self.local_memory.access_float(real_address)
            elif address >= 700000 and address < 800000:
                real_address = address - 700000
                return self.local_memory.access_char(real_address)
            elif address >= 900000 and address < 1000000:
                real_address = address - 900000
                return self.local_memory.access_boolean(real_address)
        elif address < 1600000:
            if address >= 1000000 and address < 1100000:
                real_address = address - 1000000
                return self.temp_memory.access_int(real_address)
            elif address >= 1100000 and address < 1200000:
                real_address = address - 1100000
                return self.temp_memory.access_float(real_address)
            elif address >= 1200000 and address < 1300000:
                real_address = address - 1200000
                return self.temp_memory.access_char(real_address)
            elif address >= 1400000 and address < 1500000:
                real_address = address - 1400000
                return self.temp_memory.access_boolean(real_address)
    

    def is_var_global(self, address):
        '''Auxiliar para las funciones que busca si una variable existe en la
        memoria global'''
        if address >= 0 and address < 100000:
            return self.local_memory.access_int(address)
        elif address >= 100000 and address < 200000:
            real_address = address - 100000
            return self.local_memory.access_float(real_address)
        elif address >= 200000 and address < 300000:
            real_address = address - 200000
            return self.local_memory.access_char(real_address)
        elif address >= 400000 and address < 500000:
            real_address = address - 400000
            return self.local_memory.access_boolean(real_address)
        return None

class ProcedureSymbol():
    methods = {}

    def __init__(self, size):
        self.size_good = self.string_to_int_list(size)
        self.param_table = []
        self.methods['global'] = Function("global", DataType.VOID, None, self.size_good, self.param_table)

    def get_method(self, name):
        '''Regresa el objeto de la función solicitada'''
        return self.methods[name]
    
    def add_method(self, name, data_type, initial_address, size, param_table):
        '''Añade una función al directorio de funciones

        Parametros
        ------------------------
        name : str
            Nombre de la función

        data_type : str
            Tipo de la función

        initial_address : str
            Dirección del cuádruplo donde empieza la función

        size : str
            Tamaño de la función

        param_table : str
            Tabla con parámetros de la función
        '''
        data_type_good = self.string_to_data_type(data_type)
        initial_address_good = int(initial_address)
        size_good = self.string_to_int_list(size)
        param_table_good = self.string_to_param_table(param_table)
        self.methods[name] = Function(name, data_type_good, initial_address_good, size_good, param_table_good)

    def get_all_methods(self):
        for key, value in self.methods.items():
            print(f"{key}: {value}")

    def debug(self):
        return { key: value.debug() for key, value in self.methods.items()}

    def get_all_func_directions(self):
        '''Regresa todas las direcciones iniciales de las funciones'''
        directions_list = []
        for key in self.methods.keys():
            directions_list.append(self.methods[key].initial_address)
        return directions_list

    #def get_func_type_address(self, name_func):
        

    def get_name_func(self, address):
        for key in self.methods.keys():
            if self.methods[key].initial_address == None:
                continue
            if address == self.methods[key].initial_address:
                return key
        return "global"


    def string_to_int_list(self, string):
        '''Convierte texto a una lista de enteros'''
        string_split = string.strip().strip('[]').split(',')
        new_list = []
        for number in string_split:
            new_list.append(int(number))
        return new_list

    def string_to_data_type(self, string):
        '''Convierte texto al tipo de dato que regresa una función'''
        string_stripped = string.strip()
        if string_stripped == 'DataType.VOID':
            return DataType.VOID
        elif string_stripped == 'DataType.INT':
            return DataType.INT
        elif string_stripped == 'DataType.CHAR':
            return DataType.CHAR
        elif string_stripped == 'DataType.STRING':
            return DataType.STRING
        elif string_stripped == 'DataType.BOOL':
            return DataType.BOOL
    
    def string_to_param_table(self, string):
        '''Convierte el texto en una tabla de parámetros'''
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
                elif type.strip() == '<DataType.STRING: \'string\'>':
                    new_list.append(DataType.STRING)
                elif type.strip() == '<DataType.BOOL: \'bool\'>':
                    new_list.append(DataType.BOOL)
                
            return new_list
    
    def set_value(self, name_func, address, value):
        '''Asigna un valor a la dirección virtual de la memoria de una función
        
        Parámetros
        ---------------
        name_func : str
            Nombre de la función donde se va a realizar la asignación
            
        address : int
            Dirección virtual de donde se asignara el valor
            
        value : Any
            Valor que se va a asignar'''            
        self.methods[name_func].set_value(address, value)

    def get_value(self, name_func, address):
        return self.methods[name_func].get_value(address)

    def is_var_global(self, address):
        return self.methods["global"].is_var_global(address)

    def print_func_size(self, name_func):
        '''Despliega el tamaño de una función'''
        print('El tamaño de la funcion', name_func, 'es:', self.methods[name_func].size)

class Constant:
    def __init__(self, value, address):
        self.value = value
        self.address = address
    
    def get(self):
        return {"address": self.address, "value": self.value}

class ConstantTable(Constant):
    def __init__(self):
        self.constants = {}
        
    def add(self, value, address):
        self.constants[int(address)] = Constant(value, int(address))

    def get(self, value):
        return self.constants.get(value).value

    def get_all_constants(self):
        for key, value in self.constants.items():
            print(f"{key}: {value}")
    
    def debug(self):
        return { key: value.get() for key, value in self.constants.items()}