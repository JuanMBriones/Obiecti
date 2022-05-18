# Yacc example
 
from turtle import goto
import ply.yacc as yacc
from semantical.quadruples import Quadruples, Quadruple
from semantical.symbol_tables import ProcedureSymbol, SymbolTable
 
# Get the token map from the lexer.  This is required.
from .obi_lex import tokens

compile_status = ''
operands_stack = []
operators_stack = []
types_stack = []
jumps_stack = []
quadruples = Quadruples()
function_table = ProcedureSymbol()

def p_programa(p):
    '''programa : PROGRAM ID class context
                | PROGRAM ID context'''
    print("Apropiado")
    #print(p[:])
    
    global compile_status
    compile_status = "Apropiado"
    
    for key, value in quadruples.get_quadruples().items():
        print(f"{key}: {value}")
    print(operands_stack)
    print(operators_stack)

    print(function_table.get_methods_names())
    print(function_table.get_method('global').symbols)
    function_table.get_status()
    print('Uff✨')

def p_class(p):
    '''class : scope CLASS ID
                | scope CLASS ID COLON ID'''


def p_context(p):
    '''context : LBRACE aux6 RBRACE'''

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
    '''condicion : IF LPAREN expresion RPAREN bloque
                    | IF LPAREN expresion RPAREN bloque elif
                    | IF LPAREN expresion RPAREN bloque elif else'''
    
    #quadruple = Quadruple(operation='GOTO', left_operand=None, right_operand=None, result=None)
    #quadruples.add_quadruple(quadruple=quadruple)

def p_elif(p):
    '''elif : 
            | ELIF LPAREN expresion RPAREN bloque elif
    '''

def p_else(p):
    '''else : ELSE bloque'''

def p_ciclo(p):
    '''ciclo : WHILE LPAREN expresion RPAREN bloque'''
    jump_index = jumps_stack.pop()
    quadruple = Quadruple(operation='GOTO', left_operand=None, right_operand=None, result=jump_index)
    quadruples.add_quadruple(quadruple=quadruple)

    if jumps_stack:
        quadruple_goto_f = jumps_stack.pop()
        jump_index = len(quadruples.quadruples)
        quadruples.quadruples[quadruple_goto_f].result = jump_index
        print('🥭🥭🥭🥭🥭🥭'+str(quadruple_goto_f))

def p_constructor(p):
    '''constructor : PUBLIC ID LPAREN param RPAREN bloque'''

def p_bloque(p):
    '''bloque : LBRACE aux5 RBRACE'''

def p_funcion(p):
    '''funcion : scope DEF ID LPAREN param RPAREN contexto_func'''
    print('paso1')
    function_table.add_method(name=p[3], data_type=None, scope=p[1], params=p[4])

def p_contexto_func(p):
    '''contexto_func : LBRACE aux5 RBRACE
                        | LBRACE aux5 RETURN INT ID RBRACE
                        | LBRACE aux5 RETURN FLOAT ID RBRACE'''
    print('paso2')
    print('f', p[:])
    if len(p) > 4:

        if operands_stack:
            operands_stack.pop()
        # quadruple = Quadruple(operation='RETURN', left_operand=None, right_operand=None, result=p[4])


def p_aux5(p):
    '''aux5 : vars
            | estatuto
            | vars aux5
            | estatuto aux5'''

def p_param(p):
    '''param : 
                | tipo_simple ID
                | tipo_simple ID COMMA param'''
    print('param', p[:])

def p_scope(p):
    '''scope : PRIVATE
                | PUBLIC
                | PROTECTED'''

def p_estatuto(p):
    '''estatuto : asignacion
                | escritura
                | llamada_func
                | objeto_metodo
                | lectura'''
    """while operators_stack:
        operator = operators_stack.pop()
        if operator == '=':
            operand = operands_stack.pop()
            operand2 = operands_stack.pop()
            
            quadruple = Quadruple(operation=operator, left_operand=operand, right_operand=operand2, result='👾')
            quadruples.add_quadruple(quadruple=quadruple)

            operands_stack.append(quadruple.left_operand)
        else:
            operand = operands_stack.pop()
            operand2 = operands_stack.pop()
            quadruple = Quadruple(operation=operator, left_operand=operand, right_operand=operand2, result='👽')
            quadruples.add_quadruple(quadruple=quadruple)
            operands_stack.append(quadruple)
            #operators_stack.append(operator)"""
            

def p_lectura(p):
    '''lectura : READ LPAREN aux4 RPAREN'''

def p_aux4(p):
    '''aux4 : ID
            | objeto_aAcceso
            | ID COMMA aux4
            | objeto_aAcceso COMMA aux4'''

def p_escritura(p):
    '''escritura : PRINT LPAREN aux3 RPAREN'''
    print('escritura', p[:])

def p_aux3(p):
    '''aux3 : expresion
            | llamada_func
            | objeto_metodo
            | CSTRING
            | expresion COMMA aux3
            | llamada_func COMMA aux3
            | objeto_metodo COMMA aux3
            | CSTRING COMMA aux3'''
    print('aux3', p[:])
    if not p[1]:
        operands_stack.pop(0)

def p_vars(p):
    '''vars : VAR aux2 COLON tipo_simple
            | VAR aux2 COLON tipo_compuesto
            | VAR ID LBRACKET cint RBRACKET COLON tipo_simple
            | VAR ID LBRACKET cint RBRACKET COLON tipo_compuesto
            | VAR ID LBRACKET cint RBRACKET LBRACKET cint RBRACKET COLON tipo_simple
            | VAR ID LBRACKET cint RBRACKET LBRACKET cint RBRACKET COLON tipo_compuesto'''
    print('alm',p[:])
    print('ALSO')
    print(operands_stack)
    print(operators_stack)
    print('nOALSO')

    to_eliminate = list(p).count('[')

    for i in range(to_eliminate):
        operands_stack.pop()

    
    if len(p) == 5:
        print(f"var {operands_stack[-1]} : {types_stack[-1]}")
        quadruple = Quadruple(operation='DECLARE_VAR', left_operand=None, right_operand=None, result=operands_stack[-1])
        quadruples.add_quadruple(quadruple=quadruple)

        table = function_table.get_method('global')
        table.add(operands_stack[-1], types_stack[-1], 'global')

        operands_stack.pop()
        types_stack.pop()

        

def p_aux2(p):
    '''aux2 : ID
            | ID COMMA aux2'''
    operands_stack.append(p[1])

    
def p_tipo_simple(p):
    '''tipo_simple : INT
                    | FLOAT'''
    types_stack.append(p[1])

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
        operands_stack.insert(0, p[1])
        operators_stack.insert(0, p[2])
        print(p[:])
        print(operands_stack)
        print(operators_stack)
        while operators_stack:
            operator = operators_stack.pop()
            if operator == '=':
                operand = operands_stack.pop()
                operand2 = operands_stack.pop()
                quadruple = Quadruple(operation=operator, left_operand=operand, right_operand=None, result=operand2)
                quadruples.add_quadruple(quadruple=quadruple)
                #operands_stack.append(quadruple.result)
                #operators_stack.append(operator)
            else:
                operand = operands_stack.pop()
                operand2 = operands_stack.pop()
                quadruple = Quadruple(operation=operator, left_operand=operand, right_operand=operand2, result=quadruples.get_current())
                quadruples.add_quadruple(quadruple=quadruple)
                operands_stack.append(quadruples.get_current())
                quadruples.increment_current()

                if operator == '<' or operator == '>' or operator == '<=' or operator == '>=' or operator == '==' or operator == '!=':
                    operand = operands_stack.pop()
                    quadruple = Quadruple(operation="GOTOF", left_operand=operand, right_operand=None, result=None)
                    jumps_stack.append(len(quadruples.quadruples))
                    jumps_stack.append(len(quadruples.quadruples))
                    quadruples.add_quadruple(quadruple=quadruple)
                    
    else:
        print('este', p[:])     
            


def p_objeto_metodo(p):
    '''objeto_metodo : ID PERIOD llamada_func'''

def p_llamada_func(p):
    '''llamada_func : ID LPAREN aux RPAREN'''
    

def p_aux(p):
    '''aux : exp
            | exp COMMA aux'''
    


def p_expresion(p):
    '''expresion : exp_bool
                    | exp_bool rel_op exp_bool
                    | exp_bool AND expresion
                    | exp_bool OR expresion
                    | exp_bool rel_op exp_bool AND expresion
                    | exp_bool rel_op exp_bool OR expresion'''
    print(p[:])

def p_exp_bool(p):
    '''exp_bool : TRUE
                | FALSE
                | exp'''
    

def p_exp(p):
    '''exp : termino
            | exp PLUS termino
            | exp MINUS termino'''
    #operators_stack.append(p[2])
    if len(p) >= 3 and p[2]:
        operators_stack.insert(0, p[2])


def p_termino(p):
    '''termino : factor
                | termino TIMES factor
                | termino DIVIDE factor
                | termino MODULO factor'''

    if len(p) >= 3 and p[2]:
        operators_stack.insert(0, p[2])

    """print('de ntro au')
    while operators_stack:
        operator = operators_stack.pop()
        if operands_stack:
            operand = operands_stack.pop()
            if operands_stack:
                operand2 = operands_stack.pop()

                quadruple = Quadruple(operation=operator, left_operand=operand, right_operand=operand2, result='👺')
                quadruples.add_quadruple(quadruple=quadruple)
                operators_stack.append(quadruple)
            else:
                operands_stack.append(operand)
                operators_stack.append(operator)
                break
        else:
            operators_stack.append(operator)
            break
    print(quadruples.get_quadruples())"""

    
def p_factor(p):
    '''factor : LPAREN expresion RPAREN
                | PLUS objeto_aAcceso
                | MINUS objeto_aAcceso
                | PLUS var
                | MINUS var
                | var
                | objeto_aAcceso'''

def p_var(p):
    '''var : ID
            | cint
            | cfloat'''
    
    if p[1]:
        operands_stack.insert(0, p[1])
    

def p_cint(p):
    'cint : CINT'
    operands_stack.insert(0, p[1])
    """

    while operators_stack:
        operator = operators_stack.pop()
        if operator != '=':
            operand = operands_stack.pop()
            operand2 = operands_stack.pop()
            quadruple = Quadruple(operation=operator, left_operand=operand, right_operand=operand2, result='👽')
            quadruples.add_quadruple(quadruple=quadruple)
            operands_stack.append(quadruple.left_operand)
            #operators_stack.append(operator)
        else:
            operators_stack.append(operator)
            break"""


def p_cfloat(p):
    'cfloat : NUMBER'
    operands_stack.insert(0, p[1])
    """

    while operators_stack:
        operator = operators_stack.pop()
        if operator != '=':
            operand = operands_stack.pop()
            operand2 = operands_stack.pop()
            quadruple = Quadruple(operation=operator, left_operand=operand, right_operand=operand2, result='👽')
            quadruples.add_quadruple(quadruple=quadruple)
            operands_stack.append(quadruple.left_operand)
            #operators_stack.append(operator)
        else:
            operators_stack.append(operator)
            break"""


def p_rel_op(p):
    '''rel_op : LT
                | LE
                | GT
                | GE
                | EQ
                | NE'''
    operators_stack.insert(0, p[1])



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
    #result = parser.parse(s)
    #print(result)