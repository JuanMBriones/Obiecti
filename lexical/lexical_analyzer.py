from audioop import add
from pydoc import doc
from semantical.data_types import DataType
from semantical.quadruples import Quadruples, Quadruple
from semantical.semantic_cube import SemanticCube
from semantical.symbol_tables import ConstantTable, ProcedureSymbol, SymbolTable
from semantical.operations_codes import OperationCodes
from lexical.arrays import Array, ArrayList

class LexicalAnalyzer:
    def __init__(self, object_file_name="object.txt"):
        self.compile_status = ''
        self.operands_stack = []
        self.operators_stack = []
        self.types_stack = []
        self.jumps_stack = []
        self.params_stack = []
        self.functions_stack = ["global"]
        self.local_variables_segments = [0, 10000, 20000]
        self.constants_segments = [30000, 35000, 40000, 45000]
        self.quadruples = Quadruples()
        self.function_table = ProcedureSymbol()
        self.constants_table = ConstantTable()
        self.semantic_cube = SemanticCube()
        self.rel_op = set(['==', '!=', '>', '<', '>=', '<='])
        self.param_count = 1
        self.paramater = None
        self.object_file_name = object_file_name

        self.human_quadruples = Quadruples()
        self.human_operands_stack = []
        self.human_operators_stack = []


    """
    The following methods helps to generate the pbject file
    """

    def generate_object_file(self):
        with open(self.object_file_name, "w") as object_file:
            for key in self.function_table.get_methods_names():
                name_func = key
                initial_address = self.function_table.get_initial_address(name_func)
                data_type = self.function_table.get_func_data_type(name_func)
                size = self.function_table.get_size(name_func)
                param_table = self.function_table.get_param_table(name_func)
                object_file.write(f"{name_func}; {data_type}; {initial_address}; ")
                object_file.write(f"{size}; {param_table}\n")

            object_file.write("%%\n")

            for key in self.constants_table.get_all_constants_values():
                value = key
                address = self.constants_table.get_address(value)
                object_file.write(f"{key}, {address}\n")

            object_file.write("%%\n")

            for key, value in self.quadruples.get_quadruples().items():
                object_file.write(f"{value}\n")
            
    
    """
    The following methods helps to generate the quadruples
    """
    def generate_quadruple(self, operation, left_operand, right_operand, result, type=None):
        quadruple = Quadruple(operation=operation, left_operand=left_operand, right_operand=right_operand, result=result)

        if type:
            self.human_quadruples.add_quadruple(quadruple=quadruple)
        else:
            self.quadruples.add_quadruple(quadruple=quadruple)
    
    def quadruples_size(self):
        return len(self.quadruples.quadruples)

    """
    The following methods helps to controll the flow of the non linear instructions, suc as if and while
    Like the jumps and the GOTO statements
    """

    def calculate_if_jumps(self):
        #print(self.jumps_stack[:])
        end = self.jumps_stack.pop()
        self.quadruples.quadruples[end].result = self.quadruples_size()
        while self.jumps_stack:
            end = self.jumps_stack.pop()
            self.quadruples.quadruples[end].result = self.quadruples_size()
    
    def calculate_if_false_jumps(self):
        false = self.jumps_stack.pop()
        self.generate_quadruple(operation=int(OperationCodes.GOTO), left_operand=int(OperationCodes.NONE), right_operand=int(OperationCodes.NONE), result=int(OperationCodes.NONE))        
        self.generate_quadruple(operation="GOTO", left_operand="", right_operand="", result="", type=True)
        self.jumps_stack.append(self.quadruples_size() - 1)
        self.quadruples.quadruples[false].result = self.quadruples_size()
    
    def calculate_while_jump(self):
        end = self.jumps_stack.pop()
        jump_index = self.jumps_stack.pop()
        self.generate_quadruple(operation=int(OperationCodes.GOTO), left_operand=int(OperationCodes.NONE), right_operand=int(OperationCodes.NONE), result=jump_index)
        self.generate_quadruple(operation="GOTO", left_operand="", right_operand="", result=jump_index, type=True)
        self.quadruples.quadruples[end].result = self.quadruples_size()
    
    def jumps_stack_add(self):
        self.jumps_stack.append(len(self.quadruples.quadruples))


    
    def add_id(self, p):
        is_var_global = self.function_table.get_global_variable(p[1])
        is_func_global = self.function_table.get_method(p[1])
        if is_var_global or is_func_global:
            print(f'{p[1]} is already defined')
            exit(-1)
        else:
            name_method = p[1]
            type_method = self.types_stack.pop()
            self.function_table.add_method(name_method, type_method)
            self.function_table.add_global_variable(name_method, type_method)
            self.add_var_func_size("global", type_method)
            self.operands_stack.append(p[1])
            self.human_operands_stack.append(p[1])
            self.functions_stack.append(p[1])


    def add_id_void(self, p):
        is_var_global = self.function_table.get_global_variable(p[1])
        is_func_global = self.function_table.get_method(p[1])
        if is_var_global or is_func_global:
            print(f'{p[1]} is already defined')
            exit(-1)
        else:
            self.function_table.add_method(p[1], DataType.VOID)
            self.operands_stack.append(p[1])
            self.human_operands_stack.append(p[1])
            self.functions_stack.append(p[1])

    
    def identify_type(self, p):
        if p[1] == "int":
            self.types_stack.append(DataType.INT)
        elif p[1] == "float":
            self.types_stack.append(DataType.FLOAT)
        elif p[1] == "char":
            self.types_stack.append(DataType.CHAR)
        elif p[1] == "string":
            self.types_stack.append(DataType.STRING)
        elif p[1] == "bool":
            self.types_stack.append(DataType.BOOL)
        #print("Identify type operands stack:", self.operands_stack)
        #print("Identify type types stack:", self.types_stack)
    
    def add_operand(self, p, index):
        if len(p) >= index + 1 and p[index]:
            self.operands_stack.append(p[index]) 
            self.human_operands_stack.append(p[index])

    def generate_multiple_quadruples(self, operation):
        while self.operands_stack:
            self.generate_quadruple(operation=operation, left_operand=int(OperationCodes.NONE), right_operand=int(OperationCodes.NONE), result=self.operands_stack.pop())
            self.generate_quadruple(operation=OperationCodes.name(int(operation)), left_operand="", right_operand="", result=self.human_operands_stack.pop(), type=True)

    def add_expression_print(self, p): 
        if p[1]:
            self.constants_table.add(p[1], DataType.STRING)
            self.operands_stack.append(self.constants_table.get_address(p[1]))
            self.human_operands_stack.append(p[1])
    
    def declare_array(self, p):
        """| VAR ID LBRACKET cint RBRACKET COLON tipo_simple
            | VAR ID LBRACKET cint RBRACKET COLON tipo_compuesto
            | VAR ID LBRACKET cint RBRACKET LBRACKET cint RBRACKET COLON tipo_simple
            | VAR ID LBRACKET cint RBRACKET LBRACKET cint RBRACKET COLON tipo_compuesto'''"""
        #print(self.human_operators_stack[:])
        if len(p) == 8:
            # 1D
            name_var = p[2]
            
            type_var = self.types_stack.pop() #p[7]
            dim_1 = self.operands_stack.pop() #p[4]
            dim_1_h = self.human_operands_stack.pop()

            #print(name_var, type_var, dim_1)
            #print(name_var, type_var, dim_1_h)
        else:
            #2D
            name_var = p[2]
            #print('4', self.human_operands_stack.pop())
            type_var = self.types_stack.pop() #p[10]
            dim_1 = self.operands_stack.pop() #p[4]
            dim_2 = self.operands_stack.pop() #p[7]

            dim_1_h = self.human_operands_stack.pop()
            dim_2_h = self.human_operands_stack.pop()

            #print(name_var, type_var, dim_1, dim_2)



    def declare_var(self, p):
        if len(p) == 5:
            while self.operands_stack:
                name_variable = self.operands_stack.pop()
                self.human_operands_stack.pop()
                type_variable = self.types_stack[-1]
                if len(self.functions_stack) > 1:
                    name_function = self.functions_stack[-1]
                    self.function_table.add_variable(name_function, name_variable, type_variable)
                    address_variable = self.function_table.get_variable_address(name_function, name_variable)
                    self.add_var_func_size(name_function, type_variable)
                else:
                    self.function_table.add_global_variable(name_variable, type_variable)
                    self.add_var_func_size("global", type_variable)
                    address_variable = self.function_table.get_variable_address("global", name_variable)

                #quadruple = Quadruple(operation='DECLARE_VAR', left_operand=None, right_operand=None, result=address_variable)
                #quadruples.add_quadruple(quadruple=quadruple)

            self.types_stack.pop()
        elif len(p) > 5:
            self.declare_array(p)

    def add_type(self, p, index):
        if len(p) >= index + 1 and p[index]:
            self.types_stack.append(p[index])  

    def add_exp_bool(self, p):
        if p[1]:
            self.add_constant(p, DataType.BOOL)

    
    """
    The following methods helps to assign all the expression to a certain variable
    """

    def assign_operators(self, p):
        if len(p)==4:
            if len(self.functions_stack) > 1:
                name_function = self.functions_stack[-1]
                if (not self.function_table.get_global_variable(p[1]) and 
                    not self.function_table.get_variable(name_function, p[1])):
                        print(f"Variable {p[1]} not defined")
                        exit(-1)
                
                if self.function_table.get_global_variable(p[1]):
                    self.operands_stack.append(self.function_table.get_variable_address("global", p[1]))
                    self.human_operands_stack.append(p[1])
                    self.types_stack.append(self.function_table.get_variable_type("global", p[1]))

                if self.function_table.get_variable(name_function, p[1]):
                    self.operands_stack.append(self.function_table.get_variable_address(name_function, p[1]))
                    self.human_operands_stack.append(p[1])
                    self.types_stack.append(self.function_table.get_variable_type(name_function, p[1]))
            else:
                if (not self.function_table.get_global_variable(p[1])):
                    print(f"Variable {p[1]} not defined")
                    exit(-1)
                self.operands_stack.append(self.function_table.get_variable_address("global", p[1]))
                self.human_operands_stack.append(p[1])
                self.types_stack.append(self.function_table.get_variable_type("global", p[1]))

            self.operators_stack.append(p[2])
            self.human_operators_stack.append(p[2])

            while self.operators_stack:
                operator = self.operators_stack.pop()
                self.human_operators_stack.pop()
                if operator == '=':
                    right_operand = self.operands_stack.pop()
                    left_operand = self.operands_stack.pop()

                    right_operand_human = self.human_operands_stack.pop()
                    left_operand_human = self.human_operands_stack.pop()

                    result_type = self.semantic_cube.validate(operator, self.types_stack.pop(), self.types_stack.pop())
                    if result_type != None:
                        self.generate_quadruple(operation=int(OperationCodes.ASSIGN), left_operand=left_operand, right_operand=int(OperationCodes.NONE), result=right_operand)                        
                        self.generate_quadruple(operation="=", left_operand=left_operand_human, right_operand="", result=right_operand_human, type=True)                        
                    else:
                        print("Type mismatch")
                        exit(-1)
        elif len(p) > 4:
            # arrays
            """
            | ID LBRACKET exp RBRACKET EQUALS exp_cond
            | ID LBRACKET exp RBRACKET EQUALS objeto_metodo
            | objeto_aAcceso LBRACKET exp RBRACKET EQUALS exp_cond
            | objeto_aAcceso LBRACKET exp RBRACKET EQUALS objeto_metodo
            | ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS exp_cond
            | ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS objeto_metodo
            | objeto_aAcceso LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS exp_cond
            | objeto_aAcceso LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS objeto_metodo'''
            """
            if len(p) == 7:
                print(f"{p[1]}[{self.human_operands_stack[-2]}] = {self.human_operands_stack[-1]}")
                self.generate_quadruple(operation="VER", left_operand=self.human_operands_stack[-2], right_operand=0, result="SIZE-1", type=True)
                self.generate_quadruple(operation="+", left_operand=self.human_operands_stack[-2], right_operand="DIRB", result=self.quadruples.get_current(), type=True)
                self.generate_quadruple(operation="=", left_operand=self.human_operands_stack[-1], right_operand="", result=f"({self.quadruples.get_current()})", type=True)
                self.quadruples.increment_current()
            else:
                print(f"{p[1]}[{self.human_operands_stack[-3]}][{self.human_operands_stack[-2]}] = {self.human_operands_stack[-1]}")
                dim_1 = self.human_operands_stack[-3]
                dim_2 = self.human_operands_stack[-2]
                self.generate_quadruple(operation="VER", left_operand=dim_1, right_operand=0, result="SIZE-1", type=True)
                self.generate_quadruple(operation="*", left_operand=dim_1, right_operand="M1", result=self.quadruples.get_current(), type=True)
                quadruple_sum = self.quadruples.get_current()
                self.quadruples.increment_current()
                self.generate_quadruple(operation="VER", left_operand=dim_2, right_operand=0, result="SIZE-1", type=True)
                self.generate_quadruple(operation="+", left_operand=quadruple_sum, right_operand=dim_2, result=self.quadruples.get_current(), type=True)
                current_dir = self.quadruples.get_current()
                self.quadruples.increment_current()
                self.generate_quadruple(operation="+", left_operand=current_dir, right_operand="DIRB", result=self.quadruples.get_current(), type=True)
                self.generate_quadruple(operation="=", left_operand=self.human_operands_stack[-1], right_operand="", result=f"({self.quadruples.get_current()})", type=True)
            print('s',self.human_operands_stack[:])
            
    

    """
    The following methods helps to the function section and its neural points
    """
    def functions_stack_pop(self, index=None):
        if index:
            self.functions_stack.pop(index)
        else:
            self.functions_stack.pop()

    
    def create_function(self, p):
        self.generate_quadruple(operation=int(OperationCodes.ENDFUNC), left_operand=int(OperationCodes.NONE), right_operand=int(OperationCodes.NONE), result=int(OperationCodes.NONE))
        self.generate_quadruple(operation="ENDFUNC", left_operand="", right_operand="", result="", type=True)

        self.function_table.delete_table(self.functions_stack[-1])
        name_function = self.functions_stack.pop()

        if name_function == "main":
            address = self.function_table.get_initial_address(name_function)
            self.quadruples.quadruples[0].result = address
            self.human_quadruples.quadruples[0].result = "main"

    def return_var(self):
        func_address = self.function_table.get_variable_address("global", self.functions_stack[-1])
        result = self.operands_stack.pop()
        result_human = self.human_operands_stack.pop()
        self.generate_quadruple(operation=int(OperationCodes.RETURN), left_operand=func_address, right_operand=int(OperationCodes.NONE), result=result)
        self.generate_quadruple(operation="RETURN", left_operand=func_address, right_operand="", result=result_human, type=True)


    def function_calling(self):
        name_function = self.operands_stack.pop()
        self.human_operands_stack.pop()
        address_function = self.function_table.get_variable_address("global", name_function)
        ip = self.function_table.get_initial_address(name_function)
        
        self.generate_quadruple(operation=int(OperationCodes.GOSUB), left_operand=address_function, right_operand=int(OperationCodes.NONE), result=ip)
        self.generate_quadruple(operation="GOSUB", left_operand=address_function, right_operand="", result=name_function, type=True)

        type_function = self.function_table.get_func_data_type(name_function)
        if type_function != DataType.VOID:
            address = self.function_table.add_temporal_variable(self.functions_stack[-1], type_function)            
            self.generate_quadruple(operation=int(OperationCodes.ASSIGN), left_operand=address_function, right_operand=int(OperationCodes.NONE), result=address)
            self.generate_quadruple(operation="=", left_operand=address_function, right_operand="", result=self.functions_stack[-1], type=True)

            self.types_stack.append(type_function)
            self.add_temp_func_size(self.functions_stack[-1], type_function)
            self.operands_stack.append(address)
            self.human_operands_stack.append(self.functions_stack[-1])

            self.function_table.move_temporal_next_direction(self.functions_stack[-1], type_function)
            self.quadruples.increment_current()
        else:
            self.operands_stack.append(address_function)
            self.human_operands_stack.append(name_function)
            self.types_stack.append(self.function_table.get_func_data_type(name_function)) 
    
    def function_call_id(self, p):
        if not self.function_table.get_method(p[1]):
            print(f"{p[1]} is not defined")
            exit(-1)
        self.operands_stack.append(p[1])
        self.human_operands_stack.append(p[1])

    def function_call_neural_point_arg(self):
        name_function = self.operands_stack[-1]
        address_function = self.function_table.get_initial_address(name_function)
        self.generate_quadruple(operation=int(OperationCodes.ERA), left_operand=int(OperationCodes.NONE), right_operand=int(OperationCodes.NONE), result=address_function)
        self.generate_quadruple(operation="ERA", left_operand="", right_operand="", result=name_function, type=True)

        self.function_table.reset_counter(name_function)
        counter = self.function_table.get_counter(self.operands_stack[-1])
        self.params_stack.append(self.function_table.get_param(name_function, counter))
        #print(paramater)
    
    def function_call_neural_point_arg_end(self, p):
        name_function = self.operands_stack[-1]
        counter = self.function_table.get_counter(name_function)
        length_param = self.function_table.get_len_param(name_function)
        if len(p) > 2:
            if counter + 1 != length_param:
                print(f"Expected {length_param} arguments but instead {counter + 1} were given")
                exit(-1)
        else:
            if counter != length_param:
                print(f"Expected {length_param} arguments but instead {counter} were given")
                exit(-1)

    def add_param(self, name_func, type):
        self.function_table.get_method(name_func).add_param(type)

        # array with index to refactor this
        if type == DataType.INT:
            self.function_table.add_param_count(name_func, 0)
        elif type == DataType.FLOAT:
            self.function_table.add_param_count(name_func, 1)
        elif type == DataType.CHAR:
            self.function_table.add_param_count(name_func, 2)

    def add_function_parameters(self):
        while len(self.operands_stack) > 1:
            name_func = self.operands_stack[0]
            name_var = self.operands_stack.pop()
            self.human_operands_stack.pop() # human
            data_type = self.types_stack.pop()
            self.function_table.add_variable(name_func, name_var, data_type)
            self.add_param(name_func, data_type)
        
        self.human_operands_stack.pop() # human
        self.function_table.set_initial_address(self.operands_stack.pop(), self.quadruples_size())

    
    def function_args_neural_point(self):
        argument = self.operands_stack.pop()
        argument_human = self.human_operands_stack.pop()
        argument_type = self.types_stack.pop()
        current_param = self.params_stack.pop()
        if current_param:
            if argument_type != current_param:
                expected = current_param.value
                argument = argument_type.value
                print(f"Expected argument of type {expected.upper()} but instead {argument.upper()} were given")
                exit(-1)
            name_function = self.operands_stack[-1]
            counter = self.function_table.get_counter(name_function)
            self.generate_quadruple(operation=int(OperationCodes.PARAM), left_operand=argument, right_operand=int(OperationCodes.NONE), result=counter)
            self.generate_quadruple(operation="PARAM", left_operand=argument_human, right_operand="", result=counter, type=True)
    
    def add_extra_arguments(self):
        name_function = self.operands_stack[-1]
        counter = self.function_table.get_counter(name_function)
        self.function_table.set_counter(name_function, counter + 1)
        self.params_stack.append(self.function_table.get_param(name_function, counter))

    # Function size assignation
    def add_var_func_size(self, name_func, type):
        if type == DataType.INT:
            self.function_table.add_var_count(name_func, 0)
        elif type == DataType.FLOAT:
            self.function_table.add_var_count(name_func, 1)
        elif type == DataType.CHAR:
            self.function_table.add_var_count(name_func, 2)
        elif type == DataType.STRING:
            self.function_table.add_var_count(name_func, 3)
        elif type == DataType.BOOL:
            self.function_table.add_var_count(name_func, 4)

    def add_temp_func_size(self, name_func, type):
        if type == DataType.INT:
            self.function_table.add_var_count(name_func, 5)
        elif type == DataType.FLOAT:
            self.function_table.add_var_count(name_func, 6)
        elif type == DataType.CHAR:
            self.function_table.add_var_count(name_func, 7)
        elif type == DataType.STRING:
            self.function_table.add_var_count(name_func, 8)
        elif type == DataType.BOOL:
            self.function_table.add_var_count(name_func, 9)

    """
    The following methods helps to the GOTOF nerual point
    """

    def calculate_goto_false(self, p):
        if len(p) >= 2:
            operand = self.operands_stack.pop()
            operand_human = self.human_operands_stack.pop()
            
            self.generate_quadruple(operation=int(OperationCodes.GOTOF), left_operand=operand, right_operand=int(OperationCodes.NONE), result=int(OperationCodes.NONE))
            self.generate_quadruple(operation="GOTOF", left_operand=operand_human, right_operand="", result="", type=True)

            self.jumps_stack.append(len(self.quadruples.quadruples) - 1)
    

    """
    The following methods helps to solve expressions using the stack of operands and operators and generate its quadruples
    """

    def generate_bool_expression(self, p):
        if len(p) >= 3 and p[2]:
            self.operators_stack.append(p[2])
            self.human_operators_stack.append(p[2])

            if self.operators_stack[-1] == 'and' or self.operators_stack[-1] == 'or':
                operator = self.operators_stack.pop()
                self.human_operators_stack.pop()

                address_operator = 0
                if operator == 'and':
                    address_operator = int(OperationCodes.AND)
                elif operator == 'or':
                    address_operator = int(OperationCodes.OR)

                right_operand = self.operands_stack.pop()
                left_operand = self.operands_stack.pop()
                right_operand_human = self.human_operands_stack.pop()
                left_operand_human = self.human_operands_stack.pop()
                
                result_type = self.semantic_cube.validate(operator, self.types_stack.pop(), self.types_stack.pop())
                if result_type != None:
                    address = self.function_table.add_temporal_variable(self.functions_stack[-1], result_type)
                    
                    self.generate_quadruple(operation=address_operator, left_operand=left_operand, right_operand=right_operand, result=address)
                    self.generate_quadruple(operation=operator, left_operand=left_operand_human, right_operand=right_operand_human, result=f"t{self.quadruples.get_current()}", type=True)

                    self.types_stack.append(result_type)
                    self.add_temp_func_size(self.functions_stack[-1], result_type)
                    self.operands_stack.append(address)
                    self.human_operands_stack.append(f"t{self.quadruples.get_current()}")
                    self.function_table.move_temporal_next_direction(self.functions_stack[-1], result_type)
                    self.quadruples.increment_current()
            else:
                print("Type mismatch")
                exit(-1)

    def evaluate_expression_bool(self, p):
        if len(p) >= 3 and p[2]:
            self.operators_stack.append(p[2])
            self.human_operators_stack.append(p[2])

            if (self.operators_stack[-1] in self.rel_op):
                    operator = self.operators_stack.pop()
                    self.human_operators_stack.pop()

                    address_operator = 0
                    
                    operation_relation = {
                        '<':  int(OperationCodes.LT),
                        '>':  int(OperationCodes.GT),
                        '<=': int(OperationCodes.LE),
                        '>=': int(OperationCodes.GE),
                        '==': int(OperationCodes.EQ),
                        '!=': int(OperationCodes.NE)
                    }

                    address_operator = operation_relation[operator]
                    right_operand = self.operands_stack.pop()
                    left_operand = self.operands_stack.pop()
                    right_operand_human = self.human_operands_stack.pop()
                    left_operand_human = self.human_operands_stack.pop()

                    result_type = self.semantic_cube.validate(operator, self.types_stack.pop(), self.types_stack.pop())
                    if result_type != None:
                        address = self.function_table.add_temporal_variable(self.functions_stack[-1], result_type)
                        
                        self.generate_quadruple(operation=address_operator, left_operand=left_operand, right_operand=right_operand, result=address)
                        self.generate_quadruple(operation=operator, left_operand=left_operand_human, right_operand=right_operand_human, result=f"t{self.quadruples.get_current()}", type=True)

                        self.types_stack.append(result_type)
                        self.add_temp_func_size(self.functions_stack[-1], result_type)
                        self.operands_stack.append(address)
                        self.human_operands_stack.append(f"t{self.quadruples.get_current()}")
                        self.function_table.move_temporal_next_direction(self.functions_stack[-1], result_type)
                        self.quadruples.increment_current()
                    else:
                        print("Type mismatch")
                        exit(-1)
    

    def expressions_add_sub(self, p):
        if len(p) >= 3 and p[2]:
            self.operators_stack.append(p[2])
            self.human_operators_stack.append(p[2])

            if self.operators_stack[-1] == "+" or self.operators_stack[-1] == "-":

                operator = self.operators_stack.pop()
                self.human_operators_stack.pop()

                address_operator = 0
                if operator == "+":
                    address_operator = int(OperationCodes.SUM)
                elif operator == "-":
                    address_operator = int(OperationCodes.MINUS)

                right_operand = self.operands_stack.pop()
                left_operand = self.operands_stack.pop()
                right_operand_human = self.human_operands_stack.pop()
                left_operand_human = self.human_operands_stack.pop()

                result_type = self.semantic_cube.validate(operator, self.types_stack.pop(), self.types_stack.pop())
                if result_type != None:
                    address = self.function_table.add_temporal_variable(self.functions_stack[-1], result_type)
                    self.generate_quadruple(operation=address_operator, left_operand=left_operand, right_operand=right_operand, result=address)
                    self.generate_quadruple(operation=operator, left_operand=left_operand_human, right_operand=right_operand_human, result=f"t{self.quadruples.get_current()}", type=True)

                    self.types_stack.append(result_type)
                    self.add_temp_func_size(self.functions_stack[-1], result_type)
                    self.operands_stack.append(address)
                    self.human_operands_stack.append(f"t{self.quadruples.get_current()}")
                    self.function_table.move_temporal_next_direction(self.functions_stack[-1], result_type)
                    self.quadruples.increment_current()
                else:
                    print("Type mismatch")
                    exit(-1)
                

    def expression_mult(self, p):
        if len(p) >= 3 and p[2]:
            self.operators_stack.append(p[2])
            self.human_operators_stack.append(p[2])

            if self.operators_stack[-1] == "*" or self.operators_stack[-1] == "/" or self.operators_stack[-1] == "%":
                operator = self.operators_stack.pop()
                address_operator = 0
                if operator == "*":
                    address_operator = int(OperationCodes.MULT)
                elif operator == "/":
                    address_operator = int(OperationCodes.DIV)
                elif operator == "%":
                    address_operator = int(OperationCodes.MOD)


                right_operand = self.operands_stack.pop()
                left_operand = self.operands_stack.pop()

                right_operand_human = self.human_operands_stack.pop()
                left_operand_human = self.human_operands_stack.pop()

                result_type = self.semantic_cube.validate(operator, self.types_stack.pop(), self.types_stack.pop())
                if result_type != None:
                    address = self.function_table.add_temporal_variable(self.functions_stack[-1], result_type)
                    self.generate_quadruple(operation=address_operator, left_operand=left_operand, right_operand=right_operand, result=address)
                    self.generate_quadruple(operation=operator, left_operand=left_operand_human, right_operand=right_operand_human, result=f"t{self.quadruples.get_current()}", type=True)

                    self.types_stack.append(result_type)
                    self.add_temp_func_size(self.functions_stack[-1], result_type)
                    self.operands_stack.append(address)
                    self.human_operands_stack.append(f"t{self.quadruples.get_current()}")
                    self.function_table.move_temporal_next_direction(self.functions_stack[-1], result_type)
                    self.quadruples.increment_current()
                else:
                    print("Type mismatch")
                    exit(-1) 

    """
    The following methods helps to push the operands to the stack as well as the constants
    """

    def add_var(self, p):
        if p[1]:
            if len(self.functions_stack) > 1:
                name_function = self.functions_stack[-1]
                if (not self.function_table.get_global_variable(p[1]) and 
                    not self.function_table.get_variable(name_function, p[1])):
                        print(f"Variable {p[1]} not defined")
                        exit(-1)
                if self.function_table.get_global_variable(p[1]):
                    self.operands_stack.append(self.function_table.get_variable_address("global", p[1]))
                    self.human_operands_stack.append(p[1])
                    self.types_stack.append(self.function_table.get_variable_type("global", p[1]))

                if self.function_table.get_variable(name_function, p[1]):
                    self.operands_stack.append(self.function_table.get_variable_address(name_function, p[1]))
                    self.human_operands_stack.append(p[1])
                    self.types_stack.append(self.function_table.get_variable_type(name_function, p[1]))

            else:
                if (not self.function_table.get_global_variable(p[1])):
                    print(f"Variable {p[1]} not defined")
                    exit(-1)
                self.operands_stack.append(self.function_table.get_variable_address("global", p[1]))
                self.human_operands_stack.append(p[1])
                self.types_stack.append(self.function_table.get_variable_type("global", p[1]))

    def add_constant(self, p, type):
        self.constants_table.add(p[1], type)
        self.operands_stack.append(self.constants_table.get_address(p[1]))
        self.human_operands_stack.append(p[1])
        self.types_stack.append(type)
    
    def add_int_constant(self, p):
        self.add_constant(p, DataType.INT)
    
    def add_char_constant(self, p):
        self.add_constant(p, DataType.CHAR)

    def add_float_constant(self, p):
        self.add_constant(p, DataType.FLOAT)

    def add_bool_constant(self, p):
        self.add_constant(p, DataType.BOOL)

    def print_func_all_variables(self):
        print(self.function_table.get_all_variables("global"))