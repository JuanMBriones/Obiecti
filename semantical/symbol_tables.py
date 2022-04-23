class Symbol:
    def __init__(self, name, data_type, scope):
        self.name = name
        self.data_type = data_type
        self.scope = scope

    def __eq__(self, __o) -> bool:
        if __o.name == self.name and __o.data_type == self.data_type and __o.scope == self.scope:
            return True
        
        return False

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
