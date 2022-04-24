from semantical.errors_exceptions import TypeMismatchError
from semantical.semantic_cube import SemanticCube

class Symbol:
    def __init__(self, name, data_type, scope, value=None):
        self.name = name
        self.data_type = data_type
        self.scope = scope
        self.value = value

    def __eq__(self, __o) -> bool:
        if self.value == __o.value:
            return True
        
        return False
    
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)

    def __gt__(self, __o) -> bool:
        if __o.data_type != self.data_type:
            raise TypeMismatchError(self, __o)
            return None
        
        if self.value > __o.value:
            return True

        return False

    def __lt__(self, __o) -> bool:
        if __o.data_type != self.data_type:
            raise TypeMismatchError(self, __o)
            return None
        
        if self.value < __o.value:
            return True

        return False

    def __le__(self, __o) -> bool:
        return self.__eq__(__o) or self.__lt__(__o)

    def __ge__(self, __o) -> bool:
        return self.__eq__(__o) or self.__gt__(__o)
    
    """
    
    'sum': {
            ('int', 'int'): 'int',
            ('int', 'float'): 'float',
            ('float', 'int'): 'float',
            ('float', 'float'): 'float',
        },
    """
    def __add__(self, __o):
        type = SemanticCube.semantic_cube['sum'][(self.data_type, __o.data_type)]
        if not type:
            raise TypeMismatchError(self, __o)
        if type == 'int':
            return int(self.value + __o.value)
        return float(self.value + __o.value)


class ProcedureSymbol(Symbol):
    def __init__(self, name, data_type, scope, params = []):
        super().__init__(name, data_type, scope)
        self.params = params
        self.locals = []
    
    def __eq__(self, __o: Symbol) -> bool:
        bitmask_temp = super().__eq__(__o)

        if bitmask_temp and __o.params == self.params and __o.locals == self.locals:
            return True

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


class SymbolTable(metaclass=SingletonMeta):
    def __init__(self):
        self.symbols = {}

    def add(self, name, data_type, type, scope, params = []):
        try:
            if name in self.symbols:
                raise Exception("Symbol already exists")
            if type == "procedure":
                self.symbols[name] = ProcedureSymbol(name, data_type, scope, params)
            else:
                self.symbols[name] = Symbol(name, data_type, scope)
        except:
            return None

    def get(self, name):
        if name in self.symbols:
            return self.symbols[name]
        return None

    def get_all_variables_names(self):
        return self.symbols.keys() # .values()

    def free_all_variables(self):
        self.symbols = {}
    
    def free_variable(self, name):
        if name in self.symbols:
            del self.symbols[name]