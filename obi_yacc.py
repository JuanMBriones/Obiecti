# Yacc example
 
import ply.yacc as yacc
 
# Get the token map from the lexer.  This is required.
from obi_lex import tokens



def p_vars(p):
    '''vars : vars vars
            | VAR aux'''

def p_aux(p):
    '''aux : aux aux
            | ID COLON tipo_simple
            | ID COLON tipo_compuesto
            | ID LBRACKET cint RBRACKET LBRACKET cint RBRACKET COLON tipo_simple
            | ID LBRACKET cint RBRACKET LBRACKET cint RBRACKET COLON tipo_compuesto
            | ID LBRACKET cint RBRACKET COLON tipo_simple
            | ID LBRACKET cint RBRACKET COLON tipo_compuesto
            | ID aux2 COLON tipo_simple
            | ID aux2 COLON tipo_compuesto'''

def p_aux2(p):
    '''aux2 :  aux2 aux2
            | COMMA ID'''

def p_tipo_simple(p):
    '''tipo_simple : INT
                    | FLOAT'''

def p_tipo_compuesto(p):
    '''tipo_compuesto : ID'''

def p_asignacion(p):
    '''asignacion : ID LBRACKET cint RBRACKET LBRACKET cint RBRACKET EQUALS expresion
                    | ID LBRACKET cint RBRACKET EQUALS expresion
                    | ID EQUALS expresion '''
    print(p[1])
    print(p[2])

def p_expresion(p):
    '''expresion : exp_bool
                    | exp_bool rel_op exp_bool
                    | expresion AND exp_bool
                    | expresion OR exp_bool
                    | expresion AND exp_bool rel_op exp_bool
                    | expresion OR exp_bool rel_op exp_bool'''

def p_exp_bool(p):
    '''exp_bool : TRUE
                | FALSE
                | exp'''

def p_exp(p):
    '''exp : termino
            | exp PLUS termino
            | exp MINUS termino'''
    print(p[1])

def p_termino(p):
    '''termino : factor
                | termino TIMES factor
                | termino DIVIDE factor
                | termino MODULO factor'''
    print(p[1])

def p_factor(p):
    '''factor : LPAREN expresion RPAREN
                | var
                | PLUS var
                | MINUS var'''
    print(p[1])

def p_var(p):
    '''var : ID
            | cint
            | cfloat'''
    print(p[1])

def p_cint(p):
    'cint : CINT'
    print(p[1])

def p_cfloat(p):
    'cfloat : NUMBER'
    print(p[1])

def p_rel_op(p):
    '''rel_op : LT
                | LE
                | GT
                | GE
                | EQ
                | NE'''

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()
 
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    parser.parse(s)
    #result = parser.parse(s)
    #print(result)