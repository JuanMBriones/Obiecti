class Symbol:
    def __init__(self, name, data_type, scope):
        self.name = name
        self.data_type = data_type
        self.scope = scope

class ProcedureSymbol(Symbol):
    def __init__(self, name, data_type, scope):
        super().__init__(name, data_type, scope)
        self.params = []
        self.locals = []
        
class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add(self, name, data_type, type, scope):
        if name in self.symbols:
            raise Exception("Symbol already exists")
        if type == "procedure":
            self.symbols[name] = ProcedureSymbol(name, data_type, scope)
        else:
            self.symbols[name] = Symbol(name, data_type, scope)

    def get(self, name):
        if name in self.symbols:
            return self.symbols[name]
        return None

    def get_all(self):
        return self.symbols.values()
