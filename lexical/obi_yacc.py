# Yacc example
 
from ast import operator
from asyncio import constants
from audioop import add
from html.entities import name2codepoint
from turtle import goto
from typing import Set
from unittest import result
from xml.etree.ElementPath import get_parent_map
import ply.yacc as yacc
from semantical.data_types import DataType
from semantical.quadruples import Quadruples, Quadruple
from semantical.semantic_cube import SemanticCube
from semantical.symbol_tables import ConstantTable, ProcedureSymbol, SymbolTable
 
# Get the token map from the lexer.  This is required.
from .obi_lex import tokens

compile_status = ''
operands_stack = []
operators_stack = []
types_stack = []
jumps_stack = []
params_stack = []
functions_stack = ["global"]
local_variables_segments = [0, 10000, 20000]
constants_segments = [30000, 35000, 40000, 45000]
quadruples = Quadruples()
function_table = ProcedureSymbol()
constants_table = ConstantTable()
semantic_cube = SemanticCube()
rel_op = set(['==', '!=', '>', '<', '>=', '<='])
param_count = 1
paramater = None

#   Se usa esta tabla de simbolos para pruebas
tabla_prueba = SymbolTable()

def p_programa(p):
    '''programa : PROGRAM ID aux_program class context
                | PROGRAM ID aux_program context'''
    print("Apropiado")
    
    global compile_status
    compile_status = "Apropiado"

    with open("object.txt", "w") as object_file:
        for key in function_table.get_methods_names():
            name_func = key
            initial_address = function_table.get_initial_address(name_func)
            data_type = function_table.get_func_data_type(name_func)
            size = function_table.get_size(name_func)
            param_table = function_table.get_param_table(name_func)
            object_file.write(f"{name_func}; {data_type}; {initial_address}; ")
            object_file.write(f"{size}; {param_table}\n")

        object_file.write("%%\n")

        for key in constants_table.get_all_constants_values():
            object_file.write(f"{key}\n")

        object_file.write("%%\n")

        for key, value in quadruples.get_quadruples().items():
            object_file.write(f"{value}\n")
    print("Archivo object (.txt) escrito. Listo para ejecutar")


def p_aux_program(p):
    '''aux_program :'''
    quadruple = Quadruple(operation=2100014, left_operand=2100022, right_operand=2100022, result=2100022)
    quadruples.add_quadruple(quadruple=quadruple)

def p_class(p):
    '''class : scope CLASS ID
                | scope CLASS ID COLON ID'''


def p_context(p):
    '''context : LBRACE aux6 RBRACE'''
    functions_stack.pop()

def p_aux6(p):
    '''aux6 : vars
            | constructor
            | funcion
            | estatuto
            | condicion
            | ciclo
            | vars aux6
            | constructor aux6
            | funcion aux6
            | estatuto aux6
            | condicion aux6
            | ciclo aux6'''

def p_condicion(p):
    '''condicion : IF LPAREN gotoF RPAREN bloque
                    | IF LPAREN gotoF RPAREN bloque elif'''
    end = jumps_stack.pop()
    quadruples.quadruples[end].result = len(quadruples.quadruples)
    while jumps_stack:
        end = jumps_stack.pop()
        quadruples.quadruples[end].result = len(quadruples.quadruples)

def p_elif(p):
    '''elif : aux_elif ELIF LPAREN gotoF RPAREN bloque
                | aux_elif ELIF LPAREN gotoF RPAREN bloque elif'''

def p_aux_elif(p):
    '''aux_elif :'''
    false = jumps_stack.pop()
    quadruple = Quadruple(operation=2100014, left_operand=2100022, right_operand=2100022, result=2100022)
    quadruples.add_quadruple(quadruple=quadruple)
    jumps_stack.append(len(quadruples.quadruples) - 1)
    quadruples.quadruples[false].result = len(quadruples.quadruples)


def p_ciclo(p):
    '''ciclo : aux_ciclo WHILE LPAREN gotoF RPAREN bloque'''
    end = jumps_stack.pop()
    jump_index = jumps_stack.pop()
    quadruple = Quadruple(operation=2100014, left_operand=2100022, right_operand=2100022, result=jump_index)
    quadruples.add_quadruple(quadruple=quadruple)
    quadruples.quadruples[end].result = len(quadruples.quadruples)
    
def p_aux_ciclo(p):
    '''aux_ciclo :'''
    jumps_stack.append(len(quadruples.quadruples))

def p_constructor(p):
    '''constructor : PUBLIC ID LPAREN param RPAREN bloque'''

def p_bloque(p):
    '''bloque : LBRACE aux5 RBRACE'''

def p_funcion(p):
    '''funcion : scope type DEF id LPAREN param aux_param RPAREN contexto_func
                | scope VOID DEF id LPAREN param aux_param RPAREN contexto_func'''
    function_table.delete_table(functions_stack[-1])
    name_function = functions_stack.pop()
    quadruple = Quadruple(operation=2100019, left_operand=2100022, right_operand=2100022, result=2100022)
    quadruples.add_quadruple(quadruple=quadruple)
    if name_function == "main":
        address = function_table.get_initial_address(name_function)
        quadruples.quadruples[0].result = address

def p_id(p):
    '''id : ID'''
    is_var_global = function_table.get_global_variable(p[1])
    is_func_global = function_table.get_method(p[1])
    if is_var_global or is_func_global:
        print(f'{p[1]} is already defined')
        exit(-1)
    else:
        if len(types_stack) > 0:
            name_method = p[1]
            type_method = types_stack.pop()
            function_table.add_method(name_method, type_method)
            function_table.add_global_variable(name_method, type_method)
        else:
            function_table.add_method(p[1], DataType.VOID)
        operands_stack.append(p[1])
        functions_stack.append(p[1])
    

def p_type(p):
    '''type : INT
            | FLOAT
            | CHAR'''
    if p[1] == "int":
        types_stack.append(DataType.INT)
    elif p[1] == "float":
        types_stack.append(DataType.FLOAT)
    elif p[1] == "char":
        types_stack.append(DataType.CHAR)

def p_contexto_func(p):
    '''contexto_func : LBRACE aux5 RBRACE
                        | LBRACE aux5 RETURN ID RBRACE'''


def p_aux5(p):
    '''aux5 : vars
            | estatuto
            | vars aux5
            | estatuto aux5'''

def p_param(p):
    '''param : 
                | tipo_simple ID
                | tipo_simple ID COMMA param'''
    if len(p) >= 3 and p[2]:
        operands_stack.append(p[2])

def p_aux_param(p):
    '''aux_param :'''
    while len(operands_stack) > 1:
        name_func = operands_stack[0]
        name_var = operands_stack.pop()
        data_type = types_stack.pop()
        function_table.add_variable(name_func, name_var, data_type)
        add_param(name_func, data_type)
    function_table.set_initial_address(operands_stack.pop(), len(quadruples.quadruples))

def p_scope(p):
    '''scope : 
                | PRIVATE
                | PUBLIC
                | PROTECTED'''

def p_estatuto(p):
    '''estatuto : asignacion
                | escritura
                | llamada_func
                | objeto_metodo
                | lectura'''

def p_lectura(p):
    '''lectura : READ LPAREN aux4 RPAREN'''
    while operands_stack:
        quadruple = Quadruple(operation=2100021, left_operand=2100022, right_operand=2100022, result=operands_stack.pop())
        quadruples.add_quadruple(quadruple=quadruple)

def p_aux4(p):
    '''aux4 : ID
            | objeto_aAcceso
            | ID COMMA aux4
            | objeto_aAcceso COMMA aux4'''
    
    if p[1]:
        operands_stack.append(p[1])
    

def p_escritura(p):
    '''escritura : PRINT LPAREN aux3 RPAREN'''
    while operands_stack:
        quadruple = Quadruple(operation=2100020, left_operand=2100022, right_operand=2100022, result=operands_stack.pop())
        quadruples.add_quadruple(quadruple=quadruple)

def p_aux3(p):
    '''aux3 : expresion
            | llamada_func
            | objeto_metodo
            | CSTRING
            | expresion COMMA aux3
            | llamada_func COMMA aux3
            | objeto_metodo COMMA aux3
            | CSTRING COMMA aux3'''

    if p[1]:
        constants_table.add(p[1], DataType.STRING)
        operands_stack.append(constants_table.get_address(p[1]))

def p_vars(p):
    '''vars : VAR aux2 COLON tipo_simple
            | VAR aux2 COLON tipo_compuesto
            | VAR ID LBRACKET cint RBRACKET COLON tipo_simple
            | VAR ID LBRACKET cint RBRACKET COLON tipo_compuesto
            | VAR ID LBRACKET cint RBRACKET LBRACKET cint RBRACKET COLON tipo_simple
            | VAR ID LBRACKET cint RBRACKET LBRACKET cint RBRACKET COLON tipo_compuesto'''
    
    if len(p) == 5:
        while operands_stack:
            name_variable = operands_stack.pop()
            type_variable = types_stack[-1]
            if len(functions_stack) > 1:
                name_function = functions_stack[-1]
                function_table.add_variable(name_function, name_variable, type_variable)
                address_variable = function_table.get_variable_address(name_function, name_variable)
                add_var_func_size(name_function, type_variable)
            else:
                function_table.add_global_variable(name_variable, type_variable)
                add_var_func_size("global", type_variable)
                address_variable = function_table.get_variable_address("global", name_variable)
            #quadruple = Quadruple(operation='DECLARE_VAR', left_operand=None, right_operand=None, result=address_variable)
            #quadruples.add_quadruple(quadruple=quadruple)

        types_stack.pop()

def p_aux2(p):
    '''aux2 : ID
            | ID COMMA aux2'''
    operands_stack.append(p[1])

    
def p_tipo_simple(p):
    '''tipo_simple : INT
                    | FLOAT
                    | CHAR'''
    if p[1] == "int":
        types_stack.append(DataType.INT)
    elif p[1] == "float":
        types_stack.append(DataType.FLOAT)
    elif p[1] == "char":
        types_stack.append(DataType.CHAR)

def p_tipo_compuesto(p):
    '''tipo_compuesto : ID'''
    types_stack.append(p[1])

def p_asignacion(p):
    '''asignacion : ID EQUALS expresion
                    | ID EQUALS llamada_func
                    | ID EQUALS objeto_metodo
                    | objeto_aAcceso EQUALS expresion
                    | objeto_aAcceso EQUALS llamada_func
                    | objeto_aAcceso EQUALS objeto_metodo
                    | ID LBRACKET exp RBRACKET EQUALS expresion
                    | ID LBRACKET exp RBRACKET EQUALS llamada_func
                    | ID LBRACKET exp RBRACKET EQUALS objeto_metodo
                    | objeto_aAcceso LBRACKET exp RBRACKET EQUALS expresion
                    | objeto_aAcceso LBRACKET exp RBRACKET EQUALS llamada_func
                    | objeto_aAcceso LBRACKET exp RBRACKET EQUALS objeto_metodo
                    | ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS expresion
                    | ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS llamada_func
                    | ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS objeto_metodo
                    | objeto_aAcceso LBRACKET LBRACKET exp RBRACKET exp RBRACKET EQUALS expresion
                    | objeto_aAcceso LBRACKET LBRACKET exp RBRACKET exp RBRACKET EQUALS llamada_func
                    | objeto_aAcceso LBRACKET LBRACKET exp RBRACKET exp RBRACKET EQUALS objeto_metodo'''
    if len(p)==4:
        if len(functions_stack) > 1:
            name_function = functions_stack[-1]
            if (not function_table.get_global_variable(p[1]) and 
                not function_table.get_variable(name_function, p[1])):
                    print(f"Variable {p[1]} not defined")
                    exit(-1)
            
            if function_table.get_global_variable(p[1]):
                operands_stack.append(function_table.get_variable_address("global", p[1]))
                types_stack.append(function_table.get_variable_type("global", p[1]))

            if function_table.get_variable(name_function, p[1]):
                operands_stack.append(function_table.get_variable_address(name_function, p[1]))
                types_stack.append(function_table.get_variable_type(name_function, p[1]))
        else:
            if (not function_table.get_global_variable(p[1])):
                print(f"Variable {p[1]} not defined")
                exit(-1)
            operands_stack.append(function_table.get_variable_address("global", p[1]))
            types_stack.append(function_table.get_variable_type("global", p[1]))

        operators_stack.append(p[2])

        while operators_stack:
            operator = operators_stack.pop()
            if operator == '=':
                right_operand = operands_stack.pop()
                left_operand = operands_stack.pop()
                result_type = semantic_cube.validate(operator, types_stack.pop(), types_stack.pop())
                if result_type != None:
                    quadruple = Quadruple(operation=2100005, left_operand=left_operand, right_operand=2100022, result=right_operand)
                    quadruples.add_quadruple(quadruple=quadruple)
                else:
                    print("Type mismatch")
                    exit(-1)

def p_objeto_metodo(p):
    '''objeto_metodo : ID PERIOD llamada_func'''

def p_llamada_func(p):
    '''llamada_func : llamada_id llamada_lparen aux llamada_rparen'''
    name_function = operands_stack.pop()
    address_function = function_table.get_variable_address("global", name_function)
    ip = function_table.get_initial_address(name_function)
    quadruple = Quadruple(operation=2100018, left_operand=address_function, right_operand=2100022, result=ip)
    quadruples.add_quadruple(quadruple=quadruple)
    operands_stack.append(address_function)
    types_stack.append(function_table.get_func_data_type(name_function))
    
def p_llamada_id(p):
    '''llamada_id : ID'''
    if not function_table.get_method(p[1]):
        print(f"{p[1]} is not defined")
        exit(-1)
    operands_stack.append(p[1])

def p_llamada_lparen(p):
    '''llamada_lparen : LPAREN'''
    name_function = operands_stack[-1]
    address_function = function_table.get_variable_address("global", name_function)
    quadruple = Quadruple(operation=2100016, left_operand=2100022, right_operand=2100022, result=address_function)
    quadruples.add_quadruple(quadruple=quadruple)
    function_table.reset_counter(name_function)
    counter = function_table.get_counter(operands_stack[-1])
    params_stack.append(function_table.get_param(name_function, counter))
    #print(paramater)


def p_llamada_rparen(p):
    '''llamada_rparen : RPAREN'''
    name_function = operands_stack[-1]
    counter = function_table.get_counter(name_function)
    length_param = function_table.get_len_param(name_function)
    if counter + 1 > length_param:
        print(f"Expected {length_param} arguments but instead {counter + 1} were given")
        exit(-1)

def p_aux(p):
    '''aux : exp aux_exp
            | exp aux_exp aux_comma aux'''

def p_aux_exp(p):
    '''aux_exp :'''
    argument = operands_stack.pop()
    argument_type = types_stack.pop()
    current_param = params_stack.pop()
    if current_param:
        if argument_type != current_param:
            expected = current_param.value
            argument = argument_type.value
            print(f"Expected argument of type {expected.upper()} but instead {argument.upper()} were given")
            exit(-1)
        name_function = operands_stack[-1]
        counter = function_table.get_counter(name_function)
        quadruple = Quadruple(operation=2100017, left_operand=argument, right_operand=2100022, result=counter)
        quadruples.add_quadruple(quadruple=quadruple)

def p_aux_comma(p):
    '''aux_comma : COMMA'''
    name_function = operands_stack[-1]
    counter = function_table.get_counter(name_function)
    function_table.set_counter(name_function, counter + 1)
    params_stack.append(function_table.get_param(name_function, counter))

def p_gotoF(p):
    '''gotoF : exp_cond'''
    
    if len(p) >= 2:
        operand = operands_stack.pop()
        quadruple = Quadruple(operation=2100015, left_operand=operand, right_operand=2100022, result=2100022)
        quadruples.add_quadruple(quadruple=quadruple)
        jumps_stack.append(len(quadruples.quadruples) - 1)

def p_exp_cond(p):
    '''exp_cond : exp_bool
                | exp_bool AND exp_cond
                | exp_bool OR exp_cond'''
    if len(p) >= 3 and p[2]:
        operators_stack.append(p[2])
        if operators_stack[-1] == 'and' or operators_stack[-1] == 'or':
            operator = operators_stack.pop()
            address_operator = 0
            if operator == 'and':
                address_operator = 2100012
            elif operator == 'or':
                address_operator = 2100013

            right_operand = operands_stack.pop()
            left_operand = operands_stack.pop()
            result_type = semantic_cube.validate(operator, types_stack.pop(), types_stack.pop())
            if result_type != None:
                address = function_table.add_temporal_variable(functions_stack[-1], result_type)
                quadruple = Quadruple(operation=address_operator, left_operand=left_operand, right_operand=right_operand, result=address)
                quadruples.add_quadruple(quadruple=quadruple)
                types_stack.append(result_type)
                add_temp_func_size(functions_stack[-1], result_type)
                operands_stack.append(address)
                function_table.move_temporal_next_direction(functions_stack[-1], result_type)
                quadruples.increment_current()
        else:
            print("Type mismatch")
            exit(-1)

def p_exp_bool(p):
    '''exp_bool : TRUE
                | FALSE
                | expresion'''
    if p[1]:
        operands_stack.append(p[1])
        #print(operands_stack)
        types_stack.append(DataType.BOOL)

def p_expresion(p):
    '''expresion : exp
                    | exp LT expresion
                    | exp GT expresion
                    | exp GE expresion
                    | exp LE expresion
                    | exp EQ expresion
                    | exp NE expresion'''
    if len(p) >= 3 and p[2]:
        operators_stack.append(p[2])
        if (operators_stack[-1] in rel_op):
                operator = operators_stack.pop()
                address_operator = 0
                if operator == '<':
                    address_operator = 2100006
                elif operator == '>':
                    address_operator = 2100007
                elif operator == '<=':
                    address_operator = 2100008
                elif operator == '>=':
                    address_operator = 2100009
                elif operator == '==':
                    address_operator = 2100010
                elif operator == '!=':
                    address_operator = 2100011

                right_operand = operands_stack.pop()
                left_operand = operands_stack.pop()
                result_type = semantic_cube.validate(operator, types_stack.pop(), types_stack.pop())
                if result_type != None:
                    address = function_table.add_temporal_variable(functions_stack[-1], result_type)
                    quadruple = Quadruple(operation=address_operator, left_operand=left_operand, right_operand=right_operand, result=address)
                    quadruples.add_quadruple(quadruple=quadruple)
                    types_stack.append(result_type)
                    add_temp_func_size(functions_stack[-1], result_type)
                    operands_stack.append(address)
                    function_table.move_temporal_next_direction(functions_stack[-1], result_type)
                    quadruples.increment_current()
                else:
                    print("Type mismatch")
                    exit(-1)

def p_exp(p):
    '''exp : termino
            | exp PLUS termino
            | exp MINUS termino'''
    if len(p) >= 3 and p[2]:
        operators_stack.append(p[2])
        if operators_stack[-1] == "+" or operators_stack[-1] == "-":

            operator = operators_stack.pop()
            address_operator = 0
            if operator == "+":
                address_operator = 2100000
            elif operator == "-":
                address_operator = 2100001

            right_operand = operands_stack.pop()
            left_operand = operands_stack.pop()
            result_type = semantic_cube.validate(operator, types_stack.pop(), types_stack.pop())
            if result_type != None:
                address = function_table.add_temporal_variable(functions_stack[-1], result_type)
                quadruple = Quadruple(operation=address_operator, left_operand=left_operand, right_operand=right_operand, result=address)
                quadruples.add_quadruple(quadruple=quadruple)
                types_stack.append(result_type)
                add_temp_func_size(functions_stack[-1], result_type)
                operands_stack.append(address)
                function_table.move_temporal_next_direction(functions_stack[-1], result_type)
                quadruples.increment_current()
            else:
                print("Type mismatch")
                exit(-1)
            


def p_termino(p):
    '''termino : factor
                | termino TIMES factor
                | termino DIVIDE factor
                | termino MODULO factor'''
    
    if len(p) >= 3 and p[2]:
        operators_stack.append(p[2])
        if operators_stack[-1] == "*" or operators_stack[-1] == "/" or operators_stack[-1] == "%":
            operator = operators_stack.pop()
            address_operator = 0
            if operator == "*":
                address_operator = 2100002
            elif operator == "/":
                address_operator = 2100003
            elif operator == "%":
                address_operator = 2100004


            right_operand = operands_stack.pop()
            left_operand = operands_stack.pop()
            result_type = semantic_cube.validate(operator, types_stack.pop(), types_stack.pop())
            if result_type != None:
                address = function_table.add_temporal_variable(functions_stack[-1], result_type)
                quadruple = Quadruple(operation=address_operator, left_operand=left_operand, right_operand=right_operand, result=address)
                quadruples.add_quadruple(quadruple=quadruple)
                types_stack.append(result_type)
                add_temp_func_size(functions_stack[-1], result_type)
                operands_stack.append(address)
                function_table.move_temporal_next_direction(functions_stack[-1], result_type)
                quadruples.increment_current()
            else:
                print("Type mismatch")
                exit(-1) 

    
def p_factor(p):
    '''factor : LPAREN exp_cond RPAREN
                | PLUS objeto_aAcceso
                | MINUS objeto_aAcceso
                | PLUS var
                | MINUS var
                | var
                | objeto_aAcceso'''

def p_var(p):
    '''var : ID
            | cint
            | cfloat
            | cchar'''
    
    if p[1]:
        if len(functions_stack) > 1:
            name_function = functions_stack[-1]
            if (not function_table.get_global_variable(p[1]) and 
                not function_table.get_variable(name_function, p[1])):
                    print(f"Variable {p[1]} not defined")
                    exit(-1)
            if function_table.get_global_variable(p[1]):
                operands_stack.append(function_table.get_variable_address("global", p[1]))
                types_stack.append(function_table.get_variable_type("global", p[1]))

            if function_table.get_variable(name_function, p[1]):
                operands_stack.append(function_table.get_variable_address(name_function, p[1]))
                types_stack.append(function_table.get_variable_type(name_function, p[1]))

        else:
            if (not function_table.get_global_variable(p[1])):
                print(f"Variable {p[1]} not defined")
                exit(-1)
            operands_stack.append(function_table.get_variable_address("global", p[1]))
            types_stack.append(function_table.get_variable_type("global", p[1]))
    

def p_cint(p):
    'cint : CINT'
    constants_table.add(p[1], DataType.INT)
    operands_stack.append(constants_table.get_address(p[1]))
    types_stack.append(DataType.INT)


def p_cfloat(p):
    'cfloat : NUMBER'
    constants_table.add(p[1], DataType.FLOAT)
    operands_stack.append(constants_table.get_address(p[1]))
    types_stack.append(DataType.FLOAT)

def p_cchar(p):
    'cchar : CCHAR'
    constants_table.add(p[1], DataType.CHAR)
    operands_stack.append(constants_table.get_address(p[1]))
    types_stack.append(DataType.CHAR)

def p_objeto_aAcceso(p):
    '''objeto_aAcceso : ID PERIOD ID'''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    global compile_status
    compile_status = "Syntax error in input!"

def validate_syntax(file: str):
    # Build the parser
    parser = yacc.yacc()
    
    with open(file) as f:
        contents = f.read()

    parser.parse(contents)

    return compile_status
    
def add_param(name_func, type):
    function_table.get_method(name_func).add_param(type)
    if type == DataType.INT:
        function_table.add_param_count(name_func, 0)
    elif type == DataType.FLOAT:
        function_table.add_param_count(name_func, 1)
    elif type == DataType.CHAR:
        function_table.add_param_count(name_func, 2)

def add_var_func_size(name_func, type):
    if type == DataType.INT:
        function_table.add_var_count(name_func, 0)
    elif type == DataType.FLOAT:
        function_table.add_var_count(name_func, 1)
    elif type == DataType.CHAR:
        function_table.add_var_count(name_func, 2)

def add_temp_func_size(name_func, type):
    if type == DataType.INT:
        function_table.add_var_count(name_func, 3)
    elif type == DataType.FLOAT:
        function_table.add_var_count(name_func, 4)
    elif type == DataType.CHAR:
        function_table.add_var_count(name_func, 5)