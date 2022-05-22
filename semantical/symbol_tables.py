from asyncio import constants
from pydoc import classname
from semantical.errors_exceptions import TypeMismatchError
from semantical.semantic_cube import SemanticCube

class Symbol:
    def __init__(self, name, data_type, scope, address):
        self.name = name
        self.data_type = data_type
        self.scope = scope
        self.address = address
    
    def get(self):
        return (self.name, self.data_type, self.scope, self.address)

    def __eq__(self, __o) -> bool:
        if (self.name == __o.name and self.data_type == __o.data_type and 
            self.scope == __o.scope and self.address == __o.address):
            return True
        
        return False
    
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)



class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class SymbolTable(Symbol):
    def __init__(self):
        self.symbols = {}

    def add(self, name, data_type, scope, address):
        try:
            if name in self.symbols:
                raise Exception("Symbol already exists")
            else:
                self.symbols[name] = Symbol(name, data_type, scope, address)
                return True
        except:
            return None

    def get(self, name):
        if name in self.symbols:
            return self.symbols[name]

    def get_address(self, name):
        return self.get(name).get()[3]

    def get_type(self, name):
        return self.get(name).get()[1]

    def find_variable(self, name):
        return self.symbols.get(name, False)

    def get_all_variables_names(self):
        return self.symbols.keys() # .values()

    def free_all_variables(self):
        self.symbols = {}
    
    def free_variable(self, name):
        if name in self.symbols:
            del self.symbols[name]
    
    def get_status(self):
        response = {}
        for key, value in self.symbols.items():
            response[key] = value.get()

        return response

class Function:
    def __init__(self, data_type):
        self.data_type = data_type
        self.initial_address = None
        self.size = [0, 0, 0, 0, 0, 0]      #[int, float, char, temp_int, temp_float, temp_char]
        self.symbol_table = SymbolTable()
        self.param_table = ()

    def get(self):
        return (self.data_type, self.initial_address, self.size, self.symbol_table, self.param_table)

    def set_params(self, params):
        self.param_table = params
        
    def set_size(self, size):
        self.size = size

    def set_address(self, address):
        self.initial_address = address

    def add_variable(self, name, data_type, scope, address):
        return self.symbol_table.add(name, data_type, scope, address)

    def find_variable(self, name):
        return self.symbol_table.find_variable(name)

    def get_virtual_address(self, name):
        return self.symbol_table.get_address(name)

    def get_variable_type(self, name):
        return self.symbol_table.get_type(name)

    def get_initial_address(self):
        return self.initial_address

    def get_all_variables(self):
        return self.symbol_table.get_all_variables_names()

class ProcedureSymbol(metaclass=SingletonMeta):
    # __metaclass__ = SingletonMeta

    methods = {}
    global_scope = 'global'
    def __init__(self): #name, data_type, scope, params = []):
        self.methods["global"] = Function("void")

    

        """ self.params = params

            if not name in self.methods:
                self.methods[name] = SymbolTable()

        self.locals = []

        if not self.global_scope in self.methods:
            self.methods[self.global_scope] = SymbolTable() """
        
        #print(self.methods)

    def get_method(self, name):
        return self.methods.get(name, False)

    def add_method(self, name, data_type):
        if not name in self.methods:
            self.methods[name] = Function(data_type)

    def get_methods_names(self):
        return self.methods.keys()
    
    def get_global_variable(self, name):
        return self.get_variable("global", name)

    def get_variable(self, name_function, name_variable):
        try:
            return self.get_method(name_function).find_variable(name_variable)
        except:
            return None

    def add_global_variable(self, name, data_type, address):
        try:
            return self.get_method("global").add_variable(name, data_type, "global", address)
        except:
            return None

    def get_variable_address(self, name_function, name_variable):
        return self.get_method(name_function).get_virtual_address(name_variable)

    def get_variable_type(self, name_function, name_variable):
        return self.get_method(name_function).get_variable_type(name_variable)

    def get_all_variables(self, name_function):
        print(name_function)
        return self.get_method(name_function).get_all_variables()
    
    def __eq__(self, __o: Symbol) -> bool:
        bitmask_temp = super().__eq__(__o)

        if bitmask_temp and __o.params == self.params and __o.locals == self.locals:
            return True
        
    def get_status(self):
        for key, value in self.methods.items():
            print(f"{key}: {value.get_status()}")

class Constant:
    def __init__(self, value, address):
        self.value = value
        self.address = address
    
    def get(self):
        return (self.value, self.address)

    def __eq__(self, __o) -> bool:
        if self.value == __o.value and self.address == __o.address:
            return True
        
        return False
    
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)

class ConstantTable(Constant):
    def __init__(self):
        self.constants = {}

    def add(self, value, address):
        try:
            if value in self.constants:
                raise Exception("Constant already exists")
            else:
                self.constants[value] = Constant(value, address)
                return True
        except:
            return False
    
    def get(self, value):
        return self.constants.get(value, False)

    def get_address(self, value):
        return self.get(value).get()[1]
    
    def get_all_constants_values(self):
        return self.constants.keys()