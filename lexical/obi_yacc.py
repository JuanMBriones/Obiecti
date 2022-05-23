# Yacc example
 
from ast import operator
from asyncio import constants
from turtle import goto
from typing import Set
from unittest import result
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
functions_stack = ["global"]
local_variables_segments = [0, 10000, 20000]
constants_segments = [30000, 35000, 40000, 45000]
quadruples = Quadruples()
function_table = ProcedureSymbol()
constants_table = ConstantTable()
semantic_cube = SemanticCube()
rel_op = set(['==', '!=', '>', '<', '>=', '<='])

#   Se usa esta tabla de simbolos para pruebas
tabla_prueba = SymbolTable()

def p_programa(p):
    '''programa : PROGRAM ID aux_program class context
                | PROGRAM ID aux_program context'''
    print("Apropiado")
    
    global compile_status
    compile_status = "Apropiado"

    for key, value in quadruples.get_quadruples().items():
        print(f"{key}: {value}")
    print('Uff✨')

def p_aux_program(p):
    '''aux_program :'''
    quadruple = Quadruple(operation='GOTO', left_operand='Main', right_operand=None, result=None)
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
    quadruple = Quadruple(operation='GOTO', left_operand=None, right_operand=None, result=None)
    quadruples.add_quadruple(quadruple=quadruple)
    jumps_stack.append(len(quadruples.quadruples) - 1)
    quadruples.quadruples[false].result = len(quadruples.quadruples)


def p_ciclo(p):
    '''ciclo : aux_ciclo WHILE LPAREN gotoF RPAREN bloque'''
    end = jumps_stack.pop()
    jump_index = jumps_stack.pop()
    quadruple = Quadruple(operation='GOTO', left_operand=None, right_operand=None, result=jump_index)
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
    functions_stack.pop()
    quadruple = Quadruple(operation='ENDFUNC', left_operand=None, right_operand=None, result=None)
    quadruples.add_quadruple(quadruple=quadruple)

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
            add_global_variable(name_method, type_method)
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
        print(operands_stack)
        name_func = operands_stack[0]
        name_var = operands_stack.pop()
        data_type = types_stack.pop()
        add_local_variable(name_func, name_var, data_type)
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
        quadruple = Quadruple(operation='read', left_operand=None, right_operand=None, result=operands_stack.pop())
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
        quadruple = Quadruple(operation='print', left_operand=None, right_operand=None, result=operands_stack.pop())
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
        add_constant(p[1], "string")
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
                add_local_variable(name_function, name_variable, type_variable)
                address_variable = function_table.get_variable_address(name_function, name_variable)
                add_var_func_size(name_function, type_variable)
            else:
                add_global_variable(name_variable, type_variable)
                add_var_func_size("global", type_variable)
                address_variable = function_table.get_variable_address("global", name_variable)
            quadruple = Quadruple(operation='DECLARE_VAR', left_operand=None, right_operand=None, result=address_variable)
            quadruples.add_quadruple(quadruple=quadruple)

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
                operand = operands_stack.pop()
                operand2 = operands_stack.pop()
                result_type = semantic_cube.validate(operator, types_stack.pop(), types_stack.pop())
                if result_type != None:
                    quadruple = Quadruple(operation=operator, left_operand=operand, right_operand=None, result=operand2)
                    quadruples.add_quadruple(quadruple=quadruple)
                else:
                    print("Type mismatch")
                    exit(-1)

def p_objeto_metodo(p):
    '''objeto_metodo : ID PERIOD llamada_func'''

def p_llamada_func(p):
    '''llamada_func : ID LPAREN aux RPAREN'''
    

def p_aux(p):
    '''aux : exp
            | exp COMMA aux'''
    

def p_gotoF(p):
    '''gotoF : exp_cond'''
    
    if len(p) >= 2:
        operand = operands_stack.pop()
        quadruple = Quadruple(operation="GOTOF", left_operand=operand, right_operand=None, result=None)
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
            right_operand = operands_stack.pop()
            left_operand = operands_stack.pop()
            result_type = semantic_cube.validate(operator, types_stack.pop(), types_stack.pop())
            if result_type != None:
                quadruple = Quadruple(operation=operator, left_operand=left_operand, right_operand=right_operand, result=quadruples.get_current())
                quadruples.add_quadruple(quadruple=quadruple)
                types_stack.append(result_type)
                add_temp_func_size(functions_stack[-1], result_type)
                operands_stack.append(quadruples.get_current())
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
                right_operand = operands_stack.pop()
                left_operand = operands_stack.pop()
                result_type = semantic_cube.validate(operator, types_stack.pop(), types_stack.pop())
                if result_type != None:
                    quadruple = Quadruple(operation=operator, left_operand=left_operand, right_operand=right_operand, result=quadruples.get_current())
                    quadruples.add_quadruple(quadruple=quadruple)
                    types_stack.append(result_type)
                    add_temp_func_size(functions_stack[-1], result_type)
                    operands_stack.append(quadruples.get_current())
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
            right_operand = operands_stack.pop()
            left_operand = operands_stack.pop()
            result_type = semantic_cube.validate(operator, types_stack.pop(), types_stack.pop())
            if result_type != None:
                quadruple = Quadruple(operation=operator, left_operand=left_operand, right_operand=right_operand, result=quadruples.get_current())
                quadruples.add_quadruple(quadruple=quadruple)
                types_stack.append(result_type)
                add_temp_func_size(functions_stack[-1], result_type)
                operands_stack.append(quadruples.get_current())
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
            right_operand = operands_stack.pop()
            left_operand = operands_stack.pop()
            result_type = semantic_cube.validate(operator, types_stack.pop(), types_stack.pop())
            if result_type != None:
                quadruple = Quadruple(operation=operator, left_operand=left_operand, right_operand=right_operand, result=quadruples.get_current())
                quadruples.add_quadruple(quadruple=quadruple)
                types_stack.append(result_type)
                add_temp_func_size(functions_stack[-1], result_type)
                operands_stack.append(quadruples.get_current())
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
    add_constant(p[1], "int")
    operands_stack.append(constants_table.get_address(p[1]))
    types_stack.append(DataType.INT)


def p_cfloat(p):
    'cfloat : NUMBER'
    add_constant(p[1], "float")
    operands_stack.append(constants_table.get_address(p[1]))
    types_stack.append(DataType.FLOAT)

def p_cchar(p):
    'cchar : CCHAR'
    add_constant(p[1], "char")
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


def add_constant(valor, type):
    if type == "int":
        if constants_segments[0] + 1 >= 35000:
            print("Too many INT constants")
            exit(-1)
        else:
            added = constants_table.add(valor, constants_segments[0])
            if added:
                constants_segments[0] += 1
    elif type == "float":
        if constants_segments[1] + 1 >= 40000:
            print("Too many FLOAT constants")
            exit(-1)
        else:
            added = constants_table.add(valor, constants_segments[1])
            if added:
                constants_segments[1] += 1
    elif type == "char":
        if constants_segments[2] + 1 >= 45000:
            print("Too many CHAR constants")
            exit(-1)
        else:
            added = constants_table.add(valor, constants_segments[2])
            if added:
                constants_segments[2] += 1
    elif type == "string":
        if constants_segments[3] + 1 >= 50000:
            print("Too many STRING constants")
            exit(-1)
        else:
            added = constants_table.add(valor, constants_segments[3])
            if added:
                constants_segments[3] += 1

def add_global_variable(valor, type):
    if type == DataType.INT:
        if local_variables_segments[0] + 1 >= 10000:
            print("Too many INT variables")
            exit(-1)
        else:
            added = function_table.add_global_variable(valor, DataType.INT, local_variables_segments[0])
            if added != None:
                local_variables_segments[0] += 1
            else:
                print(f"Variable {valor} already defined")
                exit(-1)
    elif type == DataType.FLOAT:
        if local_variables_segments[1] + 1 >= 20000:
            print("Too many FLOAT variables")
            exit(-1)
        else:
            added = function_table.add_global_variable(valor, DataType.FLOAT, local_variables_segments[1])
            if added != None:
                local_variables_segments[1] += 1
            else:
                print(f"Variable {valor} already defined")
                exit(-1)
    elif type == DataType.CHAR:
        if local_variables_segments[2] + 1 >= 30000:
            print("Too many CHAR variables")
            exit(-1)
        else:
            added = function_table.add_global_variable(valor, DataType.CHAR, local_variables_segments[2])
            if added != None:
                local_variables_segments[2] += 1
            else:
                print(f"Variable {valor} already defined")
                exit(-1)


def add_local_variable(name_func, valor, type):
    if type == DataType.INT:
        if local_variables_segments[0] + 1 >= 10000:
            print("Too many INT variables")
            exit(-1)
        else:
            is_global = function_table.get_global_variable(valor)
            if is_global:
                print(f"Variable {valor} already defined")
                exit(-1)
            else:
                added = function_table.add_variable(name_func, valor, type, local_variables_segments[0])
                if added != None:
                    local_variables_segments[0] += 1
                else:
                    print(f"Variable {valor} already defined")
                    exit(-1)
    elif type == DataType.FLOAT:
        if local_variables_segments[1] + 1 >= 20000:
            print("Too many FLOAT variables")
            exit(-1)
        else:
            is_global = function_table.get_global_variable(valor)
            if is_global:
                print(f"Variable {valor} already defined")
                exit(-1)
            else:
                added = function_table.add_variable(name_func, valor, type, local_variables_segments[1])
                if added != None:
                    local_variables_segments[1] += 1
                else:
                    print(f"Variable {valor} already defined")
                    exit(-1)
    elif type == DataType.CHAR:
        if local_variables_segments[2] + 1 >= 30000:
            print("Too many CHAR variables")
            exit(-1)
        else:
            is_global = function_table.get_global_variable(valor)
            if is_global:
                print(f"Variable {valor} already defined")
                exit(-1)
            else:
                added = function_table.add_variable(name_func, valor, type, local_variables_segments[2])
                if added != None:
                    local_variables_segments[2] += 1
                else:
                    print(f"Variable {valor} already defined")
                    exit(-1)
    
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