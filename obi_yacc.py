# Yacc example
 
import ply.yacc as yacc
 
# Get the token map from the lexer.  This is required.
from obi_lex import tokens

def p_programa(p):
    '''programa : PROGRAM ID class context
                | PROGRAM ID context'''
    print("Apropiado")


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
                    | IF LPAREN expresion RPAREN bloque ELIF LPAREN expresion RPAREN bloque'''

def p_ciclo(p):
    '''ciclo : WHILE LPAREN expresion RPAREN bloque'''

def p_constructor(p):
    '''constructor : PUBLIC ID LPAREN param RPAREN bloque'''

def p_bloque(p):
    '''bloque : LBRACE aux5 RBRACE'''

def p_funcion(p):
    '''funcion : scope DEF ID LPAREN param RPAREN contexto_func'''

def p_contexto_func(p):
    '''contexto_func : LBRACE aux5 RBRACE
                        | LBRACE aux5 RETURN INT ID RBRACE
                        | LBRACE aux5 RETURN FLOAT ID RBRACE'''

def p_aux5(p):
    '''aux5 : vars
            | estatuto
            | vars aux5
            | estatuto aux5'''

def p_param(p):
    '''param : tipo_simple ID
                | tipo_simple ID COMMA param'''

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

def p_lectura(p):
    '''lectura : READ LPAREN aux4 RPAREN'''

def p_aux4(p):
    '''aux4 : ID
            | objeto_aAcceso
            | ID COMMA aux4
            | objeto_aAcceso COMMA aux4'''

def p_escritura(p):
    '''escritura : PRINT LPAREN aux3 RPAREN'''

def p_aux3(p):
    '''aux3 : expresion
            | llamada_func
            | objeto_metodo
            | CSTRING
            | expresion COMMA aux3
            | llamada_func COMMA aux3
            | objeto_metodo COMMA aux3
            | CSTRING COMMA aux3'''

def p_vars(p):
    '''vars : VAR aux2 COLON tipo_simple
            | VAR aux2 COLON tipo_compuesto
            | VAR ID LBRACKET cint RBRACKET COLON tipo_simple
            | VAR ID LBRACKET cint RBRACKET COLON tipo_compuesto
            | VAR ID LBRACKET cint RBRACKET LBRACKET cint RBRACKET COLON tipo_simple
            | VAR ID LBRACKET cint RBRACKET LBRACKET cint RBRACKET COLON tipo_compuesto'''
    
def p_aux2(p):
    '''aux2 : ID
            | ID COMMA aux2'''
    
def p_tipo_simple(p):
    '''tipo_simple : INT
                    | FLOAT'''

def p_tipo_compuesto(p):
    '''tipo_compuesto : ID'''

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
    
def p_exp_bool(p):
    '''exp_bool : TRUE
                | FALSE
                | exp'''

def p_exp(p):
    '''exp : termino
            | exp PLUS termino
            | exp MINUS termino'''

def p_termino(p):
    '''termino : factor
                | termino TIMES factor
                | termino DIVIDE factor
                | termino MODULO factor'''

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

def p_cint(p):
    'cint : CINT'

def p_cfloat(p):
    'cfloat : NUMBER'

def p_rel_op(p):
    '''rel_op : LT
                | LE
                | GT
                | GE
                | EQ
                | NE'''

def p_objeto_aAcceso(p):
    '''objeto_aAcceso : ID PERIOD ID'''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()


with open('ejemplo.txt') as f:
    contents = f.read()

parser.parse(contents)
    #result = parser.parse(s)
    #print(result)