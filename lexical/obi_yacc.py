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
from lexical.lexical_analyzer import LexicalAnalyzer
from semantical.operations_codes import OperationCodes
 
# Get the token map from the lexer.  This is required.
from .obi_lex import tokens

lexical_analyzer = LexicalAnalyzer()

def p_programa(p):
    '''programa : PROGRAM ID aux_program class context
                | PROGRAM ID aux_program context'''
    global compile_status
    compile_status = "Apropiado"

    lexical_analyzer.generate_object_file()

    print(lexical_analyzer.human_quadruples.get_quadruples())


def p_aux_program(p):
    '''aux_program :'''
    lexical_analyzer.generate_quadruple(operation=int(OperationCodes.GOTO), left_operand=int(OperationCodes.NONE), right_operand=int(OperationCodes.NONE), result=int(OperationCodes.NONE))

def p_class(p):
    '''class : scope CLASS ID
                | scope CLASS ID COLON ID'''


def p_context(p):
    '''context : LBRACE aux6 RBRACE'''
    lexical_analyzer.functions_stack_pop()

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
    lexical_analyzer.calculate_if_jumps()

def p_elif(p):
    '''elif : aux_elif ELIF LPAREN gotoF RPAREN bloque
                | aux_elif ELIF LPAREN gotoF RPAREN bloque elif'''

def p_aux_elif(p):
    '''aux_elif :'''
    lexical_analyzer.calculate_if_false_jumps()
    
def p_ciclo(p):
    '''ciclo : aux_ciclo WHILE LPAREN gotoF RPAREN bloque'''
    lexical_analyzer.calculate_while_jump()
     
def p_aux_ciclo(p):
    '''aux_ciclo :'''
    lexical_analyzer.jumps_stack_add()

def p_constructor(p):
    '''constructor : PUBLIC ID LPAREN param RPAREN bloque'''

def p_bloque(p):
    '''bloque : LBRACE aux5 RBRACE'''

def p_funcion(p):
    '''funcion : scope type DEF id LPAREN param aux_param RPAREN contexto_func
                | scope VOID DEF id LPAREN param aux_param RPAREN contexto_func'''
    lexical_analyzer.create_function(p)

def p_id(p):
    '''id : ID'''
    lexical_analyzer.add_id(p)
    
def p_type(p):
    '''type : INT
            | FLOAT
            | CHAR
            | STRING
            | BOOL'''
    lexical_analyzer.identify_type(p)

def p_contexto_func(p):
    '''contexto_func : LBRACE aux_contexto_func RBRACE'''

def p_aux_contexto_func(p):
    '''aux_contexto_func :  vars
                            | estatuto
                            | ciclo
                            | condicion
                            | RETURN exp_cond aux_return
                            | vars aux_contexto_func
                            | estatuto aux_contexto_func
                            | ciclo aux_contexto_func
                            | condicion aux_contexto_func
                            | RETURN exp_cond aux_return aux_contexto_func'''

def p_aux_return(p):
    '''aux_return :'''
    lexical_analyzer.return_var()

def p_aux5(p):
    '''aux5 : estatuto
            | RETURN exp_cond aux_return
            | estatuto aux5
            | RETURN exp_cond aux_return aux5'''

def p_param(p):
    '''param : 
                | tipo_simple ID
                | tipo_simple ID COMMA param'''
    lexical_analyzer.add_operand(p, 2)

def p_aux_param(p):
    '''aux_param :'''
    lexical_analyzer.add_function_parameters()

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
    lexical_analyzer.generate_multiple_quadruples(operation=int(OperationCodes.READ))

def p_aux4(p):
    '''aux4 : ID
            | objeto_aAcceso
            | ID COMMA aux4
            | objeto_aAcceso COMMA aux4'''
    lexical_analyzer.add_operand(p, 1)
    

def p_escritura(p):
    '''escritura : PRINT LPAREN aux3 RPAREN'''
    lexical_analyzer.generate_multiple_quadruples(operation=int(OperationCodes.PRINT))

def p_aux3(p):
    '''aux3 : expresion
            | objeto_metodo
            | CSTRING
            | expresion COMMA aux3
            | objeto_metodo COMMA aux3
            | CSTRING COMMA aux3'''
    lexical_analyzer.add_expression_print(p)

def p_vars(p):
    '''vars : VAR aux2 COLON tipo_simple
            | VAR aux2 COLON tipo_compuesto
            | VAR ID LBRACKET cint RBRACKET COLON tipo_simple
            | VAR ID LBRACKET cint RBRACKET COLON tipo_compuesto
            | VAR ID LBRACKET cint RBRACKET LBRACKET cint RBRACKET COLON tipo_simple
            | VAR ID LBRACKET cint RBRACKET LBRACKET cint RBRACKET COLON tipo_compuesto'''
    lexical_analyzer.declare_var(p)
    

def p_aux2(p):
    '''aux2 : ID
            | ID COMMA aux2'''
    lexical_analyzer.add_operand(p, 1)
    
def p_tipo_simple(p):
    '''tipo_simple : INT
                    | FLOAT
                    | CHAR
                    | BOOL'''
    lexical_analyzer.identify_type(p)

def p_tipo_compuesto(p):
    '''tipo_compuesto : ID'''
    lexical_analyzer.add_type(p, 1)

def p_asignacion(p):
    '''asignacion : ID EQUALS exp_cond
                    | ID EQUALS objeto_metodo
                    | objeto_aAcceso EQUALS exp_cond
                    | objeto_aAcceso EQUALS objeto_metodo
                    | ID LBRACKET exp RBRACKET EQUALS exp_cond
                    | ID LBRACKET exp RBRACKET EQUALS objeto_metodo
                    | objeto_aAcceso LBRACKET exp RBRACKET EQUALS exp_cond
                    | objeto_aAcceso LBRACKET exp RBRACKET EQUALS objeto_metodo
                    | ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS exp_cond
                    | ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS objeto_metodo
                    | objeto_aAcceso LBRACKET LBRACKET exp RBRACKET exp RBRACKET EQUALS exp_cond
                    | objeto_aAcceso LBRACKET LBRACKET exp RBRACKET exp RBRACKET EQUALS objeto_metodo'''
    lexical_analyzer.assign_operators(p)

def p_objeto_metodo(p):
    '''objeto_metodo : ID PERIOD llamada_func'''

def p_llamada_func(p):
    '''llamada_func : llamada_id llamada_lparen llamada_rparen'''
    lexical_analyzer.function_calling()
    
def p_llamada_id(p):
    '''llamada_id : ID'''
    lexical_analyzer.function_call_id(p)

def p_llamada_lparen(p):
    '''llamada_lparen : LPAREN'''
    lexical_analyzer.function_call_neural_point_arg()


def p_llamada_rparen(p):
    '''llamada_rparen : aux RPAREN
                        | RPAREN'''
    lexical_analyzer.function_call_neural_point_arg_end(p)

def p_aux(p):
    '''aux : exp aux_exp
            | exp aux_exp aux_comma aux'''

def p_aux_exp(p):
    '''aux_exp :'''
    lexical_analyzer.function_args_neural_point()

def p_aux_comma(p):
    '''aux_comma : COMMA'''
    lexical_analyzer.add_extra_arguments()

def p_gotoF(p):
    '''gotoF : exp_cond'''
    lexical_analyzer.calculate_goto_false(p)
    
def p_exp_cond(p):
    '''exp_cond : exp_bool
                | exp_bool AND exp_cond
                | exp_bool OR exp_cond'''
    lexical_analyzer.generate_bool_expression(p)

def p_exp_bool(p):
    '''exp_bool : TRUE
                | FALSE
                | expresion'''
    lexical_analyzer.add_exp_bool(p)

def p_expresion(p):
    '''expresion : exp
                    | exp LT expresion
                    | exp GT expresion
                    | exp GE expresion
                    | exp LE expresion
                    | exp EQ expresion
                    | exp NE expresion'''
    lexical_analyzer.evaluate_expression_bool(p)

def p_exp(p):
    '''exp : termino
            | exp PLUS termino
            | exp MINUS termino'''
    lexical_analyzer.expressions_add_sub(p)

def p_termino(p):
    '''termino : factor
                | termino TIMES factor
                | termino DIVIDE factor
                | termino MODULO factor'''
    lexical_analyzer.expression_mult(p)
    
    
def p_factor(p):
    '''factor : LPAREN exp_cond RPAREN
                | PLUS objeto_aAcceso
                | MINUS objeto_aAcceso
                | PLUS var
                | MINUS var
                | var
                | objeto_aAcceso
                | llamada_func'''

def p_var(p):
    '''var : ID
            | cint
            | cfloat
            | cchar'''
    lexical_analyzer.add_var(p)

def p_cint(p):
    'cint : CINT'
    lexical_analyzer.add_int_constant(p)

def p_cfloat(p):
    'cfloat : NUMBER'
    lexical_analyzer.add_float_constant(p)

def p_cchar(p):
    'cchar : CCHAR'
    lexical_analyzer.add_char_constant(p)

def p_objeto_aAcceso(p):
    '''objeto_aAcceso : ID PERIOD ID'''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    global compile_status
    compile_status = "Syntax error in input!"
    exit(-1)

def validate_syntax(file: str):
    # Build the parser
    parser = yacc.yacc()
    
    with open(file) as f:
        contents = f.read()

    parser.parse(contents)

    return compile_status
    

