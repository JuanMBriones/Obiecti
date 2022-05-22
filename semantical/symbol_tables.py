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

class ProcedureSymbol(Symbol, metaclass=SingletonMeta):
    # __metaclass__ = SingletonMeta

    methods = {}
    global_scope = 'global'
    def __init__(self, *args): #name, data_type, scope, params = []):
        if len(args) == 4:
            name, data_type, address, scope, params, *rest = args
            super().__init__(name, data_type, scope, address)
            self.params = params

            if not name in self.methods:
                self.methods[name] = SymbolTable()

        self.locals = []

        if not self.global_scope in self.methods:
            self.methods[self.global_scope] = SymbolTable()
        
        print(self.methods)
    
    def add_method(self, name, data_type, scope, params):
        if not name in self.methods:
            self.methods[name] = SymbolTable()

    def get_method(self, name):
        try:
            return self.methods[name]
        except:
            return None

    def get_methods_names(self):
        return self.methods.keys()
    
    def get_global_variable(self, name):
        try:
            return self.methods[self.global_scope][name]
        except:
            return None

    def __eq__(self, __o: Symbol) -> bool:
        bitmask_temp = super().__eq__(__o)

        if bitmask_temp and __o.params == self.params and __o.locals == self.locals:
            return True
        
    def get_status(self):
        for key, value in self.methods.items():
            print(f"{key}: {value.get_status()}")

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
        else:
            procedureSymbol = ProcedureSymbol(None, None, None)
            return procedureSymbol.get_global_variable(name)

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

class Constant():
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