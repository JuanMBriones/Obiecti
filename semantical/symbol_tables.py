from asyncio import constants
import gc
from pydoc import classname
from semantical.data_types import DataType
from semantical.errors_exceptions import TypeMismatchError
from semantical.memory import ConstantsMemory, GlobalMemory, LocalMemory, TemporalMemory
from semantical.semantic_cube import SemanticCube

class Symbol:
    def __init__(self, name, data_type, scope, address, d1=None, d2=None, m1=None, size=None):
        self.name = name
        self.data_type = data_type
        self.scope = scope
        self.address = address
        self.d1 = d1
        self.d2 = d2
        self.m1 = m1
        self.size = size
    
    def get(self, description=None):
        if description:
            if self.d2:
                return {"name": self.name, "data_type": self.data_type, "scope": self.scope, "address": self.address, "dim1": self.d1, "dim2": self.d2, "m1": self.m1, "size": self.size}
            if self.d1:
                return {"name": self.name, "data_type": self.data_type, "scope": self.scope, "address": self.address, "dim1": self.d1, "size": self.size}
            return {"name": self.name, "data_type": self.data_type, "scope": self.scope, "address": self.address}
        if self.d2:
            return (self.name, self.data_type, self.scope, self.address, self.d1, self.d2, self.m1, self.size)
        if self.d1:
            return (self.name, self.data_type, self.scope, self.address, self.d1, self.size)
        return (self.name, self.data_type, self.scope, self.address)

    def __eq__(self, __o) -> bool:
        if (self.name == __o.name and self.data_type == __o.data_type and 
            self.scope == __o.scope and self.address == __o.address):
            return True
        
        return False
    
    def __ne__(self, __o: object) -> bool:
        return not self.__eq__(__o)


class SymbolTable(Symbol):
    def __init__(self, name):
        self.symbols = {}
        self.local_memory = LocalMemory(name)
        self.temporal_memory = TemporalMemory()
        self.temporal_addresses = []

    def add(self, name, data_type, scope, d1=None, d2=None, m1=None, size=None):
        try:
            if name in self.symbols:
                raise Exception("Symbol already exists")
            else:
                if not d1: # not an array
                    address = self.local_memory.requestSpace(data_type)
                    self.symbols[name] = Symbol(name, data_type, scope, address)
                    return True
                else:
                    address = self.local_memory.requestSpace(data_type)
                    self.symbols[name] = Symbol(name, data_type, scope, address, d1, d2, m1, size)
                    return True
        except:
            return None

    def add_temporal_variable(self, data_type):
        temporal_address = self.temporal_memory.requestSpace(data_type)
        self.temporal_addresses.append({"type": data_type, "address": temporal_address})
        return temporal_address #self.temporal_memory.requestSpace(data_type)

    def move_temporal_next_direction(self, data_type):
        self.temporal_memory.move_next_direction(data_type)

    def move_local_next_direction(self, data_type, jump=1):
        self.local_memory.move_next_direction(data_type, jump)

    def get(self, name):
        if name in self.symbols:
            return self.symbols[name]

    def get_address(self, name):
        return self.get(name).get()[3]

    def get_type(self, name):
        return self.get(name).data_type

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
    def __init__(self, name, data_type):
        self.name = name
        self.data_type = data_type
        self.initial_address = None
        self.size = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]      #[int, float, char, string, bool, temp_int, temp_float, temp_char, temp_string, temp_bool]
        self.symbol_table = SymbolTable(name)
        self.param_table = []
        self.counter = 0

    def get(self):
        return (self.data_type, self.initial_address, self.size, self.symbol_table, self.param_table)

    def get_data_type(self):
        return self.data_type

    def add_param(self, param):
        self.param_table.append(param)
        
    def add_var_count(self, position, slots=1):
        self.size[position] += slots

    def add_param_count(self, position):
        self.size[position] += 1

    def set_address(self, address):
        self.initial_address = address

    def add_variable(self, name, data_type, scope, d1=None, d2=None, m1=None, size=None):
        return self.symbol_table.add(name, data_type, scope, d1, d2, m1, size)

    def add_temporal_variable(self, data_type):
        return self.symbol_table.add_temporal_variable(data_type)

    def move_temporal_next_direction(self, data_type):
        self.symbol_table.move_temporal_next_direction(data_type)

    def move_local_next_direction(self, data_type, jump=1):
        self.symbol_table.move_local_next_direction(data_type, jump)

    def find_variable(self, name):
        return self.symbol_table.find_variable(name)

    def get_virtual_address(self, name):
        return self.symbol_table.get_address(name)

    def get_variable_type(self, name):
        return self.symbol_table.get_type(name)

    def get_initial_address(self):
        return self.initial_address

    def get_temporal_address(self):
        return self.symbol_table.temporal_addresses

    def get_all_variables(self):
        return self.symbol_table.get_all_variables_names()

    def delete_table(self):
        #del self.symbol_table
        #print('ya se borro')
        gc.collect()

class ProcedureSymbol():

    methods = {}
    global_scope = 'global'
    def __init__(self): #name, data_type, scope, params = []):
        self.methods["global"] = Function("global", DataType.VOID)
    

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
            self.methods[name] = Function(name, data_type)

    def get_methods_names(self):
        return self.methods.keys()
    
    def get_global_variable(self, name):
        return self.get_variable("global", name)

    def get_variable(self, name_function, name_variable):
        try:
            return self.get_method(name_function).find_variable(name_variable)
        except:
            return None

    def add_global_variable(self, name, data_type):
        added = self.get_method("global").add_variable(name, data_type, "global")
        if added != None:
            self.move_local_next_direction("global", data_type)
        else:
            print(f"Variable {name} already defined")
            exit(-1)

    def add_variable(self, name_func, name_var, data_type, d1=None, d2=None, m1=None, size=None):
        is_global = self.get_global_variable(name_var)
        if is_global:
            print(f"Variable {name_var} already defined")
            exit(-1)
        else:
            added = self.get_method(name_func).add_variable(name_var, data_type, "local", d1, d2, m1, size)
            if added != None:
                jump = int(1)
                if d1:
                    jump *= d1
                if d2:
                    jump *= d2
                #print("ddwefe", type(jump))
                self.move_local_next_direction(name_func, data_type, int(jump))
            else:
                print(f"Variable {name_var} already defined")
                exit(-1)

    
    def add_temporal_variable(self, name_func, data_type):
        return self.get_method(name_func).add_temporal_variable(data_type)

    def move_temporal_next_direction(self, name_func, data_type):
        self.get_method(name_func).move_temporal_next_direction(data_type)

    def move_local_next_direction(self, name_func, data_type, jump=1):
        self.get_method(name_func).move_local_next_direction(data_type, jump)

    def get_param(self, name_func, position):
        try:
            return self.get_method(name_func).param_table[position]
        except:
            return None

    def get_len_param(self, name_func):
        return len(self.get_method(name_func).param_table)
    
    def get_counter(self, name_func):
        return self.get_method(name_func).counter

    def set_counter(self, name_func, cont):
        self.get_method(name_func).counter = cont

    def reset_counter(self, name_func):
        self.set_counter(name_func, 0)
        
    def delete_table(self, name_func):
        self.get_method(name_func).delete_table()

    def add_param_count(self, name_func, position):
        self.get_method(name_func).add_param_count(position)

    def add_var_count(self, name_func, position, slots=1):
        self.get_method(name_func).add_var_count(position, slots)

    def get_variable_address(self, name_function, name_variable):
        return self.get_method(name_function).get_virtual_address(name_variable)

    def get_variable_type(self, name_function, name_variable):
        return self.get_method(name_function).get_variable_type(name_variable)

    def get_all_variables(self, name_function):
        return self.get_method(name_function).get_all_variables()

    def get_func_data_type(self, name_function):
        return self.get_method(name_function).get_data_type()

    def set_initial_address(self, name_func, address):
        self.get_method(name_func).set_address(address)

    def get_initial_address(self, name_func):
        return self.get_method(name_func).initial_address

    def get_size(self, name_func):
        return self.get_method(name_func).size

    def get_param_table(self, name_func):
        return self.get_method(name_func).param_table

    def get_func_type(self, name_func):
        return self.get_method(name_func).data_type

            
    def __eq__(self, __o: Symbol) -> bool:
        bitmask_temp = super().__eq__(__o)

        if bitmask_temp and __o.params == self.params and __o.locals == self.locals:
            return True
        
    def get_status(self):
        for key, value in self.methods.items():
            print(f"{key}: {value.get_status()}")
    
    def debug(self):
        """
         print('ffff', self.function_table.get_method(self.functions_stack[-1]).get_all_variables())
            print('methods names', self.function_table.get_methods_names())
            print('currently in method', self.functions_stack[-1])
            for var in self.function_table.get_method(self.functions_stack[-1]).get_all_variables():
                print(var, self.function_table.get_method(self.functions_stack[-1]).find_variable(var).get()) #get(var))

        
        """
        print('----DEBUG-----')
        for method_name in self.methods:
            print(f"SCOPE: {method_name}")
            print('\tVARS')
            for variable in self.get_method(method_name).get_all_variables():
                print(f"\t\t{variable} -> {self.get_method(method_name).find_variable(variable).get(description=True)}")
            print(f"\tTEMP")
            #print(f"\t\t{self.get_method(method_name).get_temporal_address()}")
            for temporal_variable in self.get_method(method_name).get_temporal_address():
                print(f"\t\t{temporal_variable}, ")

        print('----END DEBUG-----')

class Constant:
    def __init__(self, value, address):
        self.value = value
        self.address = address
    
    def get(self, description=None):
        if description:
            return {"value": self.value, "address": self.address}
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
        self.constants_memory = ConstantsMemory()

    def add(self, value, type):
        try:
            if value in self.constants:
                raise Exception("Constant already exists")
            else:
                address = self.constants_memory.requestSpace(type)
                self.constants[value] = Constant(value, address)
                self.constants_memory.move_next_direction(type)
                return True
        except:
            return False
    
    def get(self, value):
        return self.constants.get(value, False)

    def get_address(self, value):
        return self.get(value).get()[1]
    
    def get_all_constants_values(self):
        return self.constants.keys()
    
    def debug(self):
        print('----DEBUG-----')
        print(f"\tCONSTANTS")
        for constant in self.constants:
            print(f"\t\t{constant} -> {self.constants[constant].get(description=True)}")
        print('----END DEBUG-----')