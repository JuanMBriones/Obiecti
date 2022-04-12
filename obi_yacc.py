# Yacc example
 
import ply.yacc as yacc
 
# Get the token map from the lexer.  This is required.
from obi_lex import tokens

def p_programa(p):
    '''programa : PROGRAM ID class
                | PROGRAM ID context'''
    print("Apropiado")

def p_class(p):
    '''class : scope CLASS ID context
                | scope CLASS ID COLON ID context'''

def p_context(p):
    '''context : LBRACE aux6 RBRACE'''

def p_aux6(p):
    '''aux6 : aux6 aux6
            | funcion
            | vars
            | estatuto
            | constructor'''

def p_constructor(p):
    '''constructor : PUBLIC ID LPAREN param RPAREN contexto_const'''

def p_contexto_const(p):
    '''contexto_const : LBRACE vars RBRACE
                        | LBRACE estatuto RBRACE
                        | LBRACE vars estatuto RBRACE'''

def p_estatuto(p):
    '''estatuto : asignacion
                | llamada_func
                | objeto_metodo
                | condicion
                | lectura
                | escritura
                | ciclo
                | estatuto asignacion
                | estatuto llamada_func
                | estatuto objeto_metodo
                | estatuto condicion
                | estatuto lectura
                | estatuto escritura
                | estatuto ciclo'''

def p_ciclo(p):
    '''ciclo : WHILE LPAREN expresion RPAREN bloque'''

def p_condicion(p):
    '''condicion : IF LPAREN expresion RPAREN bloque
                    | IF LPAREN expresion RPAREN bloque ELIF LPAREN expresion RPAREN bloque'''

def p_bloque(p):
    '''bloque : LBRACE estatuto RBRACE'''

def p_lectura(p):
    '''lectura : READ LPAREN ID RPAREN
                | READ LPAREN objeto_aAcceso RPAREN'''

def p_escritura(p):
    '''escritura : PRINT LPAREN aux5 RPAREN'''

def p_aux5(p):
    '''aux5 : expresion
            | llamada_func
            | objeto_metodo
            | CSTRING
            | aux5 COMMA expresion
            | aux5 COMMA llamada_func
            | aux5 COMMA objeto_metodo
            | aux5 COMMA CSTRING'''

def p_llamada_func(p):
    '''llamada_func : ID LPAREN aux3 RPAREN'''

def p_aux3(p):
    '''aux3 : exp
            | aux3 COMMA exp'''

def p_funcion(p):
    '''funcion : scope DEF ID LPAREN param RPAREN contexto_func'''

def p_contexto_func(p):
    '''contexto_func : LBRACE vars RBRACE
                        | LBRACE estatuto RBRACE
                        | LBRACE vars estatuto RBRACE
                        | LBRACE vars RETURN INT ID RBRACE
                        | LBRACE vars RETURN FLOAT ID RBRACE
                        | LBRACE estatuto RETURN INT ID RBRACE
                        | LBRACE estatuto RETURN FLOAT ID RBRACE
                        | LBRACE vars estatuto RETURN INT ID RBRACE
                        | LBRACE vars estatuto RETURN FLOAT ID RBRACE'''

def p_param(p):
    '''param : aux4'''

def p_aux4(p):
    '''aux4 : tipo_simple ID
            | aux4 COMMA tipo_simple ID'''

def p_scope(p):
    '''scope : PRIVATE
                | PUBLIC
                | PROTECTED'''

def p_vars(p):
    '''vars : VAR aux
            | vars VAR aux'''

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
    '''aux2 : aux2 aux2
            | COMMA ID'''

def p_tipo_simple(p):
    '''tipo_simple : INT
                    | FLOAT'''

def p_tipo_compuesto(p):
    '''tipo_compuesto : ID'''

def p_asignacion(p):
    '''asignacion : objeto_aAcceso LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS expresion
                    | objeto_aAcceso LBRACKET exp RBRACKET EQUALS expresion
                    | objeto_aAcceso EQUALS expresion
                    | ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS expresion
                    | ID LBRACKET exp RBRACKET EQUALS expresion
                    | ID EQUALS expresion
                    | objeto_aAcceso LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS llamada_func
                    | objeto_aAcceso LBRACKET exp RBRACKET EQUALS llamada_func
                    | objeto_aAcceso EQUALS llamada_func
                    | ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS llamada_func
                    | ID LBRACKET exp RBRACKET EQUALS llamada_func
                    | ID EQUALS llamada_func
                    | objeto_aAcceso LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS objeto_metodo
                    | objeto_aAcceso LBRACKET exp RBRACKET EQUALS objeto_metodo
                    | objeto_aAcceso EQUALS objeto_metodo
                    | ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS objeto_metodo
                    | ID LBRACKET exp RBRACKET EQUALS objeto_metodo
                    | ID EQUALS objeto_metodo'''

def p_objeto_metodo(p):
    '''objeto_metodo : ID PERIOD llamada_func'''

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