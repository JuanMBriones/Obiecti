import ply.lex as lex

reserved = {
    'if' : 'IF', 'elif' : 'ELIF',
    'public' : 'PUBLIC', 'private' : 'PRIVATE', 'protected' : 'PROTECTED',
    'int' : 'INT', 'float' : 'FLOAT', 'var' : 'VAR', 'char' : 'CHAR', 
    'bool' : 'BOOL', 'string' : 'STRING',
    'program' : 'PROGRAM', 'class' : 'CLASS', 'def' : 'DEF', 'void' : 'VOID',
    'return' : 'RETURN', 'and' : 'AND', 
    'or' : 'OR', 'while' : 'WHILE',
    'print' : 'PRINT', 'read' : 'READ',
    'True' : 'TRUE', 'False': 'FALSE', 'sort': 'SORT', 'find': 'FIND'
 }

tokens = [
    'NUMBER', 'CSTRING', 'CCHAR',
    'PLUS', 'MODULO', 'MINUS', 
    'TIMES', 'DIVIDE', 'EQUALS',
    'CINT',
    'LT', 'LE', 'GT', 
    'GE', 'EQ', 'NE',
    'LPAREN', 'RPAREN', 'LBRACKET', 
    'RBRACKET', 'LBRACE', 'RBRACE',
    'COMMA', 'PERIOD', 'COLON', 
    'ID', 
] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_PERIOD = r'\.'
t_COLON = r':'
t_CINT = r'\d+'
t_NUMBER = r'[-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)'
t_CCHAR = r'(\')([A-Za-z0-9]|[ \t\n]|(\()|(\)))(\')'
t_CSTRING = r'(\")([A-Za-z0-9:+-ñ!#$%&/=?]|[ \t\n]|(\()|(\)))+(\")'
t_EQUALS = r'='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='
t_MODULO = r'%'

# A regular expression rule with some action code
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words   
    return t
 
# Define a rule so we can track line numbers
#def t_newline(t):
#   r'\n+'
#    t.lexer.lineno += len(t.value)
 
# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t\n'
 
# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
 
# Build the lexer
lexer = lex.lex()
