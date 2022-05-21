
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CCHAR CINT CLASS COLON COMMA CSTRING DEF DIVIDE ELIF EQ EQUALS FALSE FLOAT GE GT ID IF INT LBRACE LBRACKET LE LPAREN LT MINUS MODULO NE NUMBER OR PERIOD PLUS PRINT PRIVATE PROGRAM PROTECTED PUBLIC RBRACE RBRACKET READ RETURN RPAREN TIMES TRUE VAR WHILEprograma : PROGRAM ID class context\n                | PROGRAM ID contextclass : scope CLASS ID\n                | scope CLASS ID COLON IDcontext : LBRACE aux6 RBRACEaux6 : vars\n            | constructor\n            | funcion\n            | estatuto\n            | condicion\n            | ciclo\n            | vars aux6\n            | constructor aux6\n            | funcion aux6\n            | estatuto aux6\n            | condicion aux6\n            | ciclo aux6condicion : IF LPAREN expresion RPAREN bloque\n                    | IF LPAREN expresion RPAREN bloque elifelif : aux_elif ELIF LPAREN expresion RPAREN bloque\n                | aux_elif ELIF LPAREN expresion RPAREN bloque elifaux_elif :ciclo : aux_ciclo WHILE LPAREN expresion RPAREN bloqueaux_ciclo :constructor : PUBLIC ID LPAREN param RPAREN bloquebloque : LBRACE aux5 RBRACEfuncion : scope DEF ID LPAREN param RPAREN contexto_funccontexto_func : LBRACE aux5 RBRACE\n                        | LBRACE aux5 RETURN INT ID RBRACE\n                        | LBRACE aux5 RETURN FLOAT ID RBRACEaux5 : vars\n            | estatuto\n            | vars aux5\n            | estatuto aux5param : \n                | tipo_simple ID\n                | tipo_simple ID COMMA paramscope : PRIVATE\n                | PUBLIC\n                | PROTECTEDestatuto : asignacion\n                | escritura\n                | llamada_func\n                | objeto_metodo\n                | lecturalectura : READ LPAREN aux4 RPARENaux4 : ID\n            | objeto_aAcceso\n            | ID COMMA aux4\n            | objeto_aAcceso COMMA aux4escritura : PRINT LPAREN aux3 RPARENaux3 : expresion\n            | llamada_func\n            | objeto_metodo\n            | CSTRING\n            | expresion COMMA aux3\n            | llamada_func COMMA aux3\n            | objeto_metodo COMMA aux3\n            | CSTRING COMMA aux3vars : VAR aux2 COLON tipo_simple\n            | VAR aux2 COLON tipo_compuesto\n            | VAR ID LBRACKET cint RBRACKET COLON tipo_simple\n            | VAR ID LBRACKET cint RBRACKET COLON tipo_compuesto\n            | VAR ID LBRACKET cint RBRACKET LBRACKET cint RBRACKET COLON tipo_simple\n            | VAR ID LBRACKET cint RBRACKET LBRACKET cint RBRACKET COLON tipo_compuestoaux2 : ID\n            | ID COMMA aux2tipo_simple : INT\n                    | FLOATtipo_compuesto : IDasignacion : ID EQUALS expresion\n                    | ID EQUALS llamada_func\n                    | ID EQUALS objeto_metodo\n                    | objeto_aAcceso EQUALS expresion\n                    | objeto_aAcceso EQUALS llamada_func\n                    | objeto_aAcceso EQUALS objeto_metodo\n                    | ID LBRACKET exp RBRACKET EQUALS expresion\n                    | ID LBRACKET exp RBRACKET EQUALS llamada_func\n                    | ID LBRACKET exp RBRACKET EQUALS objeto_metodo\n                    | objeto_aAcceso LBRACKET exp RBRACKET EQUALS expresion\n                    | objeto_aAcceso LBRACKET exp RBRACKET EQUALS llamada_func\n                    | objeto_aAcceso LBRACKET exp RBRACKET EQUALS objeto_metodo\n                    | ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS expresion\n                    | ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS llamada_func\n                    | ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS objeto_metodo\n                    | objeto_aAcceso LBRACKET LBRACKET exp RBRACKET exp RBRACKET EQUALS expresion\n                    | objeto_aAcceso LBRACKET LBRACKET exp RBRACKET exp RBRACKET EQUALS llamada_func\n                    | objeto_aAcceso LBRACKET LBRACKET exp RBRACKET exp RBRACKET EQUALS objeto_metodoobjeto_metodo : ID PERIOD llamada_funcllamada_func : ID LPAREN aux RPARENaux : exp\n            | exp COMMA auxexpresion : exp_bool\n                    | exp_bool rel_op exp_bool\n                    | exp_bool AND expresion\n                    | exp_bool OR expresion\n                    | exp_bool rel_op exp_bool AND expresion\n                    | exp_bool rel_op exp_bool OR expresionexp_bool : TRUE\n                | FALSE\n                | expexp : termino\n            | exp PLUS termino\n            | exp MINUS terminotermino : factor\n                | termino TIMES factor\n                | termino DIVIDE factor\n                | termino MODULO factorfactor : LPAREN expresion RPAREN\n                | PLUS objeto_aAcceso\n                | MINUS objeto_aAcceso\n                | PLUS var\n                | MINUS var\n                | var\n                | objeto_aAccesovar : ID\n            | cint\n            | cfloat\n            | ccharcint : CINTcfloat : NUMBERcchar : CCHARrel_op : LT\n                | LE\n                | GT\n                | GE\n                | EQ\n                | NEobjeto_aAcceso : ID PERIOD ID'
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,5,11,35,],[0,-2,-1,-5,]),'ID':([2,7,12,14,15,16,17,18,19,20,22,24,25,26,27,28,44,45,46,47,49,50,52,53,54,55,56,57,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,85,86,90,91,92,93,94,105,106,107,108,109,113,114,115,116,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,133,135,136,138,144,145,146,147,148,149,150,151,153,154,155,156,157,158,159,160,161,162,163,164,169,170,172,173,181,182,183,185,186,187,188,191,194,195,196,198,199,200,202,203,204,205,208,209,211,216,218,219,220,221,222,223,224,227,228,229,230,231,232,233,237,238,239,240,],[3,21,34,21,21,21,21,21,21,43,48,-41,-42,-43,-44,-45,60,81,81,85,88,81,60,81,60,102,104,109,111,-116,-71,-72,-73,-93,81,-99,-100,-101,-102,130,130,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-89,81,-74,-75,-76,81,-60,-61,-68,-69,-70,81,81,81,-123,-124,-125,-126,-127,-128,81,81,81,81,81,-110,-112,-116,-111,-113,162,-90,81,167,-51,60,60,60,60,-46,102,102,-94,-95,-96,-109,-103,-104,-106,-107,-108,-129,81,60,-18,21,81,60,109,81,81,-77,-78,-79,-25,-19,21,21,-23,-80,-81,-82,-62,-63,-97,-98,-27,21,-26,60,81,60,109,-83,-84,-85,-28,-86,-87,-88,-64,-65,235,236,-20,-29,-30,-21,]),'LBRACE':([3,4,34,104,140,166,171,190,234,],[7,7,-3,-4,170,170,170,209,170,]),'PRIVATE':([3,7,14,15,16,17,18,19,24,25,26,27,28,60,61,62,63,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,85,86,91,92,93,105,106,107,108,109,128,129,130,131,132,135,144,149,153,154,155,156,157,158,159,160,161,162,169,185,186,187,188,191,196,198,199,200,202,203,204,205,208,211,221,222,223,224,227,228,229,230,231,237,238,239,240,],[8,8,8,8,8,8,8,8,-41,-42,-43,-44,-45,-116,-71,-72,-73,-93,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-89,-74,-75,-76,-60,-61,-68,-69,-70,-110,-112,-116,-111,-113,-90,-51,-46,-94,-95,-96,-109,-103,-104,-106,-107,-108,-129,-18,-77,-78,-79,-25,-19,-23,-80,-81,-82,-62,-63,-97,-98,-27,-26,-83,-84,-85,-28,-86,-87,-88,-64,-65,-20,-29,-30,-21,]),'PUBLIC':([3,7,14,15,16,17,18,19,24,25,26,27,28,60,61,62,63,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,85,86,91,92,93,105,106,107,108,109,128,129,130,131,132,135,144,149,153,154,155,156,157,158,159,160,161,162,169,185,186,187,188,191,196,198,199,200,202,203,204,205,208,211,221,222,223,224,227,228,229,230,231,237,238,239,240,],[9,22,22,22,22,22,22,22,-41,-42,-43,-44,-45,-116,-71,-72,-73,-93,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-89,-74,-75,-76,-60,-61,-68,-69,-70,-110,-112,-116,-111,-113,-90,-51,-46,-94,-95,-96,-109,-103,-104,-106,-107,-108,-129,-18,-77,-78,-79,-25,-19,-23,-80,-81,-82,-62,-63,-97,-98,-27,-26,-83,-84,-85,-28,-86,-87,-88,-64,-65,-20,-29,-30,-21,]),'PROTECTED':([3,7,14,15,16,17,18,19,24,25,26,27,28,60,61,62,63,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,85,86,91,92,93,105,106,107,108,109,128,129,130,131,132,135,144,149,153,154,155,156,157,158,159,160,161,162,169,185,186,187,188,191,196,198,199,200,202,203,204,205,208,211,221,222,223,224,227,228,229,230,231,237,238,239,240,],[10,10,10,10,10,10,10,10,-41,-42,-43,-44,-45,-116,-71,-72,-73,-93,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-89,-74,-75,-76,-60,-61,-68,-69,-70,-110,-112,-116,-111,-113,-90,-51,-46,-94,-95,-96,-109,-103,-104,-106,-107,-108,-129,-18,-77,-78,-79,-25,-19,-23,-80,-81,-82,-62,-63,-97,-98,-27,-26,-83,-84,-85,-28,-86,-87,-88,-64,-65,-20,-29,-30,-21,]),'CLASS':([6,8,9,10,],[12,-38,-39,-40,]),'VAR':([7,14,15,16,17,18,19,24,25,26,27,28,60,61,62,63,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,85,86,91,92,93,105,106,107,108,109,128,129,130,131,132,135,144,149,153,154,155,156,157,158,159,160,161,162,169,170,185,186,187,188,191,194,195,196,198,199,200,202,203,204,205,208,209,211,221,222,223,224,227,228,229,230,231,237,238,239,240,],[20,20,20,20,20,20,20,-41,-42,-43,-44,-45,-116,-71,-72,-73,-93,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-89,-74,-75,-76,-60,-61,-68,-69,-70,-110,-112,-116,-111,-113,-90,-51,-46,-94,-95,-96,-109,-103,-104,-106,-107,-108,-129,-18,20,-77,-78,-79,-25,-19,20,20,-23,-80,-81,-82,-62,-63,-97,-98,-27,20,-26,-83,-84,-85,-28,-86,-87,-88,-64,-65,-20,-29,-30,-21,]),'IF':([7,14,15,16,17,18,19,24,25,26,27,28,60,61,62,63,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,85,86,91,92,93,105,106,107,108,109,128,129,130,131,132,135,144,149,153,154,155,156,157,158,159,160,161,162,169,185,186,187,188,191,196,198,199,200,202,203,204,205,208,211,221,222,223,224,227,228,229,230,231,237,238,239,240,],[29,29,29,29,29,29,29,-41,-42,-43,-44,-45,-116,-71,-72,-73,-93,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-89,-74,-75,-76,-60,-61,-68,-69,-70,-110,-112,-116,-111,-113,-90,-51,-46,-94,-95,-96,-109,-103,-104,-106,-107,-108,-129,-18,-77,-78,-79,-25,-19,-23,-80,-81,-82,-62,-63,-97,-98,-27,-26,-83,-84,-85,-28,-86,-87,-88,-64,-65,-20,-29,-30,-21,]),'PRINT':([7,14,15,16,17,18,19,24,25,26,27,28,60,61,62,63,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,85,86,91,92,93,105,106,107,108,109,128,129,130,131,132,135,144,149,153,154,155,156,157,158,159,160,161,162,169,170,185,186,187,188,191,194,195,196,198,199,200,202,203,204,205,208,209,211,221,222,223,224,227,228,229,230,231,237,238,239,240,],[32,32,32,32,32,32,32,-41,-42,-43,-44,-45,-116,-71,-72,-73,-93,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-89,-74,-75,-76,-60,-61,-68,-69,-70,-110,-112,-116,-111,-113,-90,-51,-46,-94,-95,-96,-109,-103,-104,-106,-107,-108,-129,-18,32,-77,-78,-79,-25,-19,32,32,-23,-80,-81,-82,-62,-63,-97,-98,-27,32,-26,-83,-84,-85,-28,-86,-87,-88,-64,-65,-20,-29,-30,-21,]),'READ':([7,14,15,16,17,18,19,24,25,26,27,28,60,61,62,63,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,85,86,91,92,93,105,106,107,108,109,128,129,130,131,132,135,144,149,153,154,155,156,157,158,159,160,161,162,169,170,185,186,187,188,191,194,195,196,198,199,200,202,203,204,205,208,209,211,221,222,223,224,227,228,229,230,231,237,238,239,240,],[33,33,33,33,33,33,33,-41,-42,-43,-44,-45,-116,-71,-72,-73,-93,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-89,-74,-75,-76,-60,-61,-68,-69,-70,-110,-112,-116,-111,-113,-90,-51,-46,-94,-95,-96,-109,-103,-104,-106,-107,-108,-129,-18,33,-77,-78,-79,-25,-19,33,33,-23,-80,-81,-82,-62,-63,-97,-98,-27,33,-26,-83,-84,-85,-28,-86,-87,-88,-64,-65,-20,-29,-30,-21,]),'WHILE':([7,14,15,16,17,18,19,24,25,26,27,28,30,60,61,62,63,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,85,86,91,92,93,105,106,107,108,109,128,129,130,131,132,135,144,149,153,154,155,156,157,158,159,160,161,162,169,185,186,187,188,191,196,198,199,200,202,203,204,205,208,211,221,222,223,224,227,228,229,230,231,237,238,239,240,],[-24,-24,-24,-24,-24,-24,-24,-41,-42,-43,-44,-45,51,-116,-71,-72,-73,-93,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-89,-74,-75,-76,-60,-61,-68,-69,-70,-110,-112,-116,-111,-113,-90,-51,-46,-94,-95,-96,-109,-103,-104,-106,-107,-108,-129,-18,-77,-78,-79,-25,-19,-23,-80,-81,-82,-62,-63,-97,-98,-27,-26,-83,-84,-85,-28,-86,-87,-88,-64,-65,-20,-29,-30,-21,]),'DEF':([8,10,22,23,],[-38,-40,-39,49,]),'RBRACE':([13,14,15,16,17,18,19,24,25,26,27,28,36,37,38,39,40,41,60,61,62,63,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,85,86,91,92,93,105,106,107,108,109,128,129,130,131,132,135,144,149,153,154,155,156,157,158,159,160,161,162,169,185,186,187,188,191,193,194,195,196,198,199,200,202,203,204,205,208,211,212,213,217,221,222,223,224,227,228,229,230,231,235,236,237,238,239,240,],[35,-6,-7,-8,-9,-10,-11,-41,-42,-43,-44,-45,-12,-13,-14,-15,-16,-17,-116,-71,-72,-73,-93,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-89,-74,-75,-76,-60,-61,-68,-69,-70,-110,-112,-116,-111,-113,-90,-51,-46,-94,-95,-96,-109,-103,-104,-106,-107,-108,-129,-18,-77,-78,-79,-25,-19,211,-31,-32,-23,-80,-81,-82,-62,-63,-97,-98,-27,-26,-33,-34,224,-83,-84,-85,-28,-86,-87,-88,-64,-65,238,239,-20,-29,-30,-21,]),'EQUALS':([21,31,85,134,143,206,214,],[44,52,-129,164,173,216,219,]),'LBRACKET':([21,31,43,53,85,134,152,],[45,53,58,94,-129,163,180,]),'LPAREN':([21,29,32,33,44,45,46,48,50,51,52,53,54,60,65,85,88,90,94,113,114,115,116,117,118,119,120,121,123,124,125,126,127,136,145,146,147,148,163,164,172,173,182,183,210,216,218,219,],[46,50,54,55,65,65,65,87,65,90,65,65,65,46,65,46,139,65,65,65,65,65,-123,-124,-125,-126,-127,-128,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,218,65,65,65,]),'PERIOD':([21,60,81,102,130,],[47,47,133,133,133,]),'RETURN':([24,25,26,27,28,60,61,62,63,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,85,86,91,92,93,105,106,107,108,109,128,129,130,131,132,135,144,149,153,154,155,156,157,158,159,160,161,162,185,186,187,194,195,198,199,200,202,203,204,205,212,213,217,221,222,223,227,228,229,230,231,],[-41,-42,-43,-44,-45,-116,-71,-72,-73,-93,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-89,-74,-75,-76,-60,-61,-68,-69,-70,-110,-112,-116,-111,-113,-90,-51,-46,-94,-95,-96,-109,-103,-104,-106,-107,-108,-129,-77,-78,-79,-31,-32,-80,-81,-82,-62,-63,-97,-98,-33,-34,225,-83,-84,-85,-86,-87,-88,-64,-65,]),'COLON':([34,42,43,111,112,152,215,],[56,57,-66,-66,-67,181,220,]),'COMMA':([43,60,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,84,85,86,97,98,99,100,102,103,111,128,129,130,131,132,135,153,154,155,156,157,158,159,160,161,162,167,204,205,],[59,-116,-93,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,136,-129,-89,145,146,147,148,150,151,59,-110,-112,-116,-111,-113,-90,-94,-95,-96,-109,-103,-104,-106,-107,-108,-129,189,-97,-98,]),'TRUE':([44,50,52,54,65,90,113,114,115,116,117,118,119,120,121,145,146,147,148,164,173,182,183,216,218,219,],[66,66,66,66,66,66,66,66,66,-123,-124,-125,-126,-127,-128,66,66,66,66,66,66,66,66,66,66,66,]),'FALSE':([44,50,52,54,65,90,113,114,115,116,117,118,119,120,121,145,146,147,148,164,173,182,183,216,218,219,],[67,67,67,67,67,67,67,67,67,-123,-124,-125,-126,-127,-128,67,67,67,67,67,67,67,67,67,67,67,]),'PLUS':([44,45,46,50,52,53,54,60,65,68,69,72,73,74,75,76,77,78,79,80,81,82,84,85,90,94,95,113,114,115,116,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,136,142,145,146,147,148,156,157,158,159,160,161,162,163,164,172,173,182,183,184,197,216,218,219,],[70,70,70,70,70,70,70,-116,70,123,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,123,123,-129,70,70,123,70,70,70,-123,-124,-125,-126,-127,-128,70,70,70,70,70,-110,-112,-116,-111,-113,70,123,70,70,70,70,-109,-103,-104,-106,-107,-108,-129,70,70,70,70,70,70,123,123,70,70,70,]),'MINUS':([44,45,46,50,52,53,54,60,65,68,69,72,73,74,75,76,77,78,79,80,81,82,84,85,90,94,95,113,114,115,116,117,118,119,120,121,123,124,125,126,127,128,129,130,131,132,136,142,145,146,147,148,156,157,158,159,160,161,162,163,164,172,173,182,183,184,197,216,218,219,],[71,71,71,71,71,71,71,-116,71,124,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,124,124,-129,71,71,124,71,71,71,-123,-124,-125,-126,-127,-128,71,71,71,71,71,-110,-112,-116,-111,-113,71,124,71,71,71,71,-109,-103,-104,-106,-107,-108,-129,71,71,71,71,71,71,124,124,71,71,71,]),'CINT':([44,45,46,50,52,53,54,58,65,70,71,90,94,113,114,115,116,117,118,119,120,121,123,124,125,126,127,136,145,146,147,148,163,164,172,173,180,182,183,216,218,219,],[78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,-123,-124,-125,-126,-127,-128,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,]),'NUMBER':([44,45,46,50,52,53,54,65,70,71,90,94,113,114,115,116,117,118,119,120,121,123,124,125,126,127,136,145,146,147,148,163,164,172,173,182,183,216,218,219,],[79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,-123,-124,-125,-126,-127,-128,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,]),'CCHAR':([44,45,46,50,52,53,54,65,70,71,90,94,113,114,115,116,117,118,119,120,121,123,124,125,126,127,136,145,146,147,148,163,164,172,173,182,183,216,218,219,],[80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,-123,-124,-125,-126,-127,-128,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,]),'CSTRING':([54,145,146,147,148,],[100,100,100,100,100,]),'INT':([57,87,139,181,189,220,225,],[107,107,107,107,107,107,232,]),'FLOAT':([57,87,139,181,189,220,225,],[108,108,108,108,108,108,233,]),'TIMES':([60,69,72,73,74,75,76,77,78,79,80,81,85,128,129,130,131,132,156,157,158,159,160,161,162,],[-116,125,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-110,-112,-116,-111,-113,-109,125,125,-106,-107,-108,-129,]),'DIVIDE':([60,69,72,73,74,75,76,77,78,79,80,81,85,128,129,130,131,132,156,157,158,159,160,161,162,],[-116,126,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-110,-112,-116,-111,-113,-109,126,126,-106,-107,-108,-129,]),'MODULO':([60,69,72,73,74,75,76,77,78,79,80,81,85,128,129,130,131,132,156,157,158,159,160,161,162,],[-116,127,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-110,-112,-116,-111,-113,-109,127,127,-106,-107,-108,-129,]),'AND':([60,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,85,128,129,130,131,132,153,156,157,158,159,160,161,162,],[-116,114,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-110,-112,-116,-111,-113,182,-109,-103,-104,-106,-107,-108,-129,]),'OR':([60,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,85,128,129,130,131,132,153,156,157,158,159,160,161,162,],[-116,115,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-110,-112,-116,-111,-113,183,-109,-103,-104,-106,-107,-108,-129,]),'LT':([60,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,85,128,129,130,131,132,156,157,158,159,160,161,162,],[-116,116,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-110,-112,-116,-111,-113,-109,-103,-104,-106,-107,-108,-129,]),'LE':([60,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,85,128,129,130,131,132,156,157,158,159,160,161,162,],[-116,117,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-110,-112,-116,-111,-113,-109,-103,-104,-106,-107,-108,-129,]),'GT':([60,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,85,128,129,130,131,132,156,157,158,159,160,161,162,],[-116,118,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-110,-112,-116,-111,-113,-109,-103,-104,-106,-107,-108,-129,]),'GE':([60,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,85,128,129,130,131,132,156,157,158,159,160,161,162,],[-116,119,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-110,-112,-116,-111,-113,-109,-103,-104,-106,-107,-108,-129,]),'EQ':([60,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,85,128,129,130,131,132,156,157,158,159,160,161,162,],[-116,120,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-110,-112,-116,-111,-113,-109,-103,-104,-106,-107,-108,-129,]),'NE':([60,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,85,128,129,130,131,132,156,157,158,159,160,161,162,],[-116,121,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,-129,-110,-112,-116,-111,-113,-109,-103,-104,-106,-107,-108,-129,]),'RPAREN':([60,64,66,67,68,69,72,73,74,75,76,77,78,79,80,81,83,84,85,86,87,89,96,97,98,99,100,101,102,103,122,128,129,130,131,132,135,137,139,141,153,154,155,156,157,158,159,160,161,162,165,167,168,174,175,176,177,178,179,189,204,205,207,226,],[-116,-93,-99,-100,-101,-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,135,-91,-129,-89,-35,140,144,-52,-53,-54,-55,149,-47,-48,156,-110,-112,-116,-111,-113,-90,166,-35,171,-94,-95,-96,-109,-103,-104,-106,-107,-108,-129,-92,-36,190,-56,-57,-58,-59,-49,-50,-35,-97,-98,-37,234,]),'RBRACKET':([69,72,73,74,75,76,77,78,79,80,81,82,95,110,128,129,130,131,132,142,156,157,158,159,160,161,162,184,197,201,],[-102,-105,-115,-114,-117,-118,-119,-120,-121,-122,-116,134,143,152,-110,-112,-116,-111,-113,172,-109,-103,-104,-106,-107,-108,-129,206,214,215,]),'ELIF':([169,192,211,237,],[-22,210,-26,-22,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'class':([3,],[4,]),'context':([3,4,],[5,11,]),'scope':([3,7,14,15,16,17,18,19,],[6,23,23,23,23,23,23,23,]),'aux6':([7,14,15,16,17,18,19,],[13,36,37,38,39,40,41,]),'vars':([7,14,15,16,17,18,19,170,194,195,209,],[14,14,14,14,14,14,14,194,194,194,194,]),'constructor':([7,14,15,16,17,18,19,],[15,15,15,15,15,15,15,]),'funcion':([7,14,15,16,17,18,19,],[16,16,16,16,16,16,16,]),'estatuto':([7,14,15,16,17,18,19,170,194,195,209,],[17,17,17,17,17,17,17,195,195,195,195,]),'condicion':([7,14,15,16,17,18,19,],[18,18,18,18,18,18,18,]),'ciclo':([7,14,15,16,17,18,19,],[19,19,19,19,19,19,19,]),'asignacion':([7,14,15,16,17,18,19,170,194,195,209,],[24,24,24,24,24,24,24,24,24,24,24,]),'escritura':([7,14,15,16,17,18,19,170,194,195,209,],[25,25,25,25,25,25,25,25,25,25,25,]),'llamada_func':([7,14,15,16,17,18,19,44,47,52,54,145,146,147,148,164,170,173,194,195,209,216,219,],[26,26,26,26,26,26,26,62,86,92,98,98,98,98,98,186,26,199,26,26,26,222,228,]),'objeto_metodo':([7,14,15,16,17,18,19,44,52,54,145,146,147,148,164,170,173,194,195,209,216,219,],[27,27,27,27,27,27,27,63,93,99,99,99,99,99,187,27,200,27,27,27,223,229,]),'lectura':([7,14,15,16,17,18,19,170,194,195,209,],[28,28,28,28,28,28,28,28,28,28,28,]),'aux_ciclo':([7,14,15,16,17,18,19,],[30,30,30,30,30,30,30,]),'objeto_aAcceso':([7,14,15,16,17,18,19,44,45,46,50,52,53,54,55,65,70,71,90,94,113,114,115,123,124,125,126,127,136,145,146,147,148,150,151,163,164,170,172,173,182,183,194,195,209,216,218,219,],[31,31,31,31,31,31,31,73,73,73,73,73,73,73,103,73,128,131,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,103,103,73,73,31,73,73,73,73,31,31,31,73,73,73,]),'aux2':([20,59,],[42,112,]),'expresion':([44,50,52,54,65,90,114,115,145,146,147,148,164,173,182,183,216,218,219,],[61,89,91,97,122,141,154,155,97,97,97,97,185,198,204,205,221,226,227,]),'exp_bool':([44,50,52,54,65,90,113,114,115,145,146,147,148,164,173,182,183,216,218,219,],[64,64,64,64,64,64,153,64,64,64,64,64,64,64,64,64,64,64,64,64,]),'exp':([44,45,46,50,52,53,54,65,90,94,113,114,115,136,145,146,147,148,163,164,172,173,182,183,216,218,219,],[68,82,84,68,68,95,68,68,68,142,68,68,68,84,68,68,68,68,184,68,197,68,68,68,68,68,68,]),'termino':([44,45,46,50,52,53,54,65,90,94,113,114,115,123,124,136,145,146,147,148,163,164,172,173,182,183,216,218,219,],[69,69,69,69,69,69,69,69,69,69,69,69,69,157,158,69,69,69,69,69,69,69,69,69,69,69,69,69,69,]),'factor':([44,45,46,50,52,53,54,65,90,94,113,114,115,123,124,125,126,127,136,145,146,147,148,163,164,172,173,182,183,216,218,219,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,159,160,161,72,72,72,72,72,72,72,72,72,72,72,72,72,72,]),'var':([44,45,46,50,52,53,54,65,70,71,90,94,113,114,115,123,124,125,126,127,136,145,146,147,148,163,164,172,173,182,183,216,218,219,],[74,74,74,74,74,74,74,74,129,132,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'cint':([44,45,46,50,52,53,54,58,65,70,71,90,94,113,114,115,123,124,125,126,127,136,145,146,147,148,163,164,172,173,180,182,183,216,218,219,],[75,75,75,75,75,75,75,110,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,201,75,75,75,75,75,]),'cfloat':([44,45,46,50,52,53,54,65,70,71,90,94,113,114,115,123,124,125,126,127,136,145,146,147,148,163,164,172,173,182,183,216,218,219,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'cchar':([44,45,46,50,52,53,54,65,70,71,90,94,113,114,115,123,124,125,126,127,136,145,146,147,148,163,164,172,173,182,183,216,218,219,],[77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,]),'aux':([46,136,],[83,165,]),'aux3':([54,145,146,147,148,],[96,174,175,176,177,]),'aux4':([55,150,151,],[101,178,179,]),'tipo_simple':([57,87,139,181,189,220,],[105,138,138,202,138,230,]),'tipo_compuesto':([57,181,220,],[106,203,231,]),'rel_op':([64,],[113,]),'param':([87,139,189,],[137,168,207,]),'bloque':([140,166,171,234,],[169,188,196,237,]),'elif':([169,237,],[191,240,]),'aux_elif':([169,237,],[192,192,]),'aux5':([170,194,195,209,],[193,212,213,217,]),'contexto_func':([190,],[208,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> PROGRAM ID class context','programa',4,'p_programa','obi_yacc.py',27),
  ('programa -> PROGRAM ID context','programa',3,'p_programa','obi_yacc.py',28),
  ('class -> scope CLASS ID','class',3,'p_class','obi_yacc.py',39),
  ('class -> scope CLASS ID COLON ID','class',5,'p_class','obi_yacc.py',40),
  ('context -> LBRACE aux6 RBRACE','context',3,'p_context','obi_yacc.py',44),
  ('aux6 -> vars','aux6',1,'p_aux6','obi_yacc.py',47),
  ('aux6 -> constructor','aux6',1,'p_aux6','obi_yacc.py',48),
  ('aux6 -> funcion','aux6',1,'p_aux6','obi_yacc.py',49),
  ('aux6 -> estatuto','aux6',1,'p_aux6','obi_yacc.py',50),
  ('aux6 -> condicion','aux6',1,'p_aux6','obi_yacc.py',51),
  ('aux6 -> ciclo','aux6',1,'p_aux6','obi_yacc.py',52),
  ('aux6 -> vars aux6','aux6',2,'p_aux6','obi_yacc.py',53),
  ('aux6 -> constructor aux6','aux6',2,'p_aux6','obi_yacc.py',54),
  ('aux6 -> funcion aux6','aux6',2,'p_aux6','obi_yacc.py',55),
  ('aux6 -> estatuto aux6','aux6',2,'p_aux6','obi_yacc.py',56),
  ('aux6 -> condicion aux6','aux6',2,'p_aux6','obi_yacc.py',57),
  ('aux6 -> ciclo aux6','aux6',2,'p_aux6','obi_yacc.py',58),
  ('condicion -> IF LPAREN expresion RPAREN bloque','condicion',5,'p_condicion','obi_yacc.py',61),
  ('condicion -> IF LPAREN expresion RPAREN bloque elif','condicion',6,'p_condicion','obi_yacc.py',62),
  ('elif -> aux_elif ELIF LPAREN expresion RPAREN bloque','elif',6,'p_elif','obi_yacc.py',70),
  ('elif -> aux_elif ELIF LPAREN expresion RPAREN bloque elif','elif',7,'p_elif','obi_yacc.py',71),
  ('aux_elif -> <empty>','aux_elif',0,'p_aux_elif','obi_yacc.py',74),
  ('ciclo -> aux_ciclo WHILE LPAREN expresion RPAREN bloque','ciclo',6,'p_ciclo','obi_yacc.py',83),
  ('aux_ciclo -> <empty>','aux_ciclo',0,'p_aux_ciclo','obi_yacc.py',91),
  ('constructor -> PUBLIC ID LPAREN param RPAREN bloque','constructor',6,'p_constructor','obi_yacc.py',95),
  ('bloque -> LBRACE aux5 RBRACE','bloque',3,'p_bloque','obi_yacc.py',98),
  ('funcion -> scope DEF ID LPAREN param RPAREN contexto_func','funcion',7,'p_funcion','obi_yacc.py',101),
  ('contexto_func -> LBRACE aux5 RBRACE','contexto_func',3,'p_contexto_func','obi_yacc.py',106),
  ('contexto_func -> LBRACE aux5 RETURN INT ID RBRACE','contexto_func',6,'p_contexto_func','obi_yacc.py',107),
  ('contexto_func -> LBRACE aux5 RETURN FLOAT ID RBRACE','contexto_func',6,'p_contexto_func','obi_yacc.py',108),
  ('aux5 -> vars','aux5',1,'p_aux5','obi_yacc.py',116),
  ('aux5 -> estatuto','aux5',1,'p_aux5','obi_yacc.py',117),
  ('aux5 -> vars aux5','aux5',2,'p_aux5','obi_yacc.py',118),
  ('aux5 -> estatuto aux5','aux5',2,'p_aux5','obi_yacc.py',119),
  ('param -> <empty>','param',0,'p_param','obi_yacc.py',122),
  ('param -> tipo_simple ID','param',2,'p_param','obi_yacc.py',123),
  ('param -> tipo_simple ID COMMA param','param',4,'p_param','obi_yacc.py',124),
  ('scope -> PRIVATE','scope',1,'p_scope','obi_yacc.py',127),
  ('scope -> PUBLIC','scope',1,'p_scope','obi_yacc.py',128),
  ('scope -> PROTECTED','scope',1,'p_scope','obi_yacc.py',129),
  ('estatuto -> asignacion','estatuto',1,'p_estatuto','obi_yacc.py',132),
  ('estatuto -> escritura','estatuto',1,'p_estatuto','obi_yacc.py',133),
  ('estatuto -> llamada_func','estatuto',1,'p_estatuto','obi_yacc.py',134),
  ('estatuto -> objeto_metodo','estatuto',1,'p_estatuto','obi_yacc.py',135),
  ('estatuto -> lectura','estatuto',1,'p_estatuto','obi_yacc.py',136),
  ('lectura -> READ LPAREN aux4 RPAREN','lectura',4,'p_lectura','obi_yacc.py',139),
  ('aux4 -> ID','aux4',1,'p_aux4','obi_yacc.py',145),
  ('aux4 -> objeto_aAcceso','aux4',1,'p_aux4','obi_yacc.py',146),
  ('aux4 -> ID COMMA aux4','aux4',3,'p_aux4','obi_yacc.py',147),
  ('aux4 -> objeto_aAcceso COMMA aux4','aux4',3,'p_aux4','obi_yacc.py',148),
  ('escritura -> PRINT LPAREN aux3 RPAREN','escritura',4,'p_escritura','obi_yacc.py',155),
  ('aux3 -> expresion','aux3',1,'p_aux3','obi_yacc.py',161),
  ('aux3 -> llamada_func','aux3',1,'p_aux3','obi_yacc.py',162),
  ('aux3 -> objeto_metodo','aux3',1,'p_aux3','obi_yacc.py',163),
  ('aux3 -> CSTRING','aux3',1,'p_aux3','obi_yacc.py',164),
  ('aux3 -> expresion COMMA aux3','aux3',3,'p_aux3','obi_yacc.py',165),
  ('aux3 -> llamada_func COMMA aux3','aux3',3,'p_aux3','obi_yacc.py',166),
  ('aux3 -> objeto_metodo COMMA aux3','aux3',3,'p_aux3','obi_yacc.py',167),
  ('aux3 -> CSTRING COMMA aux3','aux3',3,'p_aux3','obi_yacc.py',168),
  ('vars -> VAR aux2 COLON tipo_simple','vars',4,'p_vars','obi_yacc.py',176),
  ('vars -> VAR aux2 COLON tipo_compuesto','vars',4,'p_vars','obi_yacc.py',177),
  ('vars -> VAR ID LBRACKET cint RBRACKET COLON tipo_simple','vars',7,'p_vars','obi_yacc.py',178),
  ('vars -> VAR ID LBRACKET cint RBRACKET COLON tipo_compuesto','vars',7,'p_vars','obi_yacc.py',179),
  ('vars -> VAR ID LBRACKET cint RBRACKET LBRACKET cint RBRACKET COLON tipo_simple','vars',10,'p_vars','obi_yacc.py',180),
  ('vars -> VAR ID LBRACKET cint RBRACKET LBRACKET cint RBRACKET COLON tipo_compuesto','vars',10,'p_vars','obi_yacc.py',181),
  ('aux2 -> ID','aux2',1,'p_aux2','obi_yacc.py',200),
  ('aux2 -> ID COMMA aux2','aux2',3,'p_aux2','obi_yacc.py',201),
  ('tipo_simple -> INT','tipo_simple',1,'p_tipo_simple','obi_yacc.py',206),
  ('tipo_simple -> FLOAT','tipo_simple',1,'p_tipo_simple','obi_yacc.py',207),
  ('tipo_compuesto -> ID','tipo_compuesto',1,'p_tipo_compuesto','obi_yacc.py',211),
  ('asignacion -> ID EQUALS expresion','asignacion',3,'p_asignacion','obi_yacc.py',215),
  ('asignacion -> ID EQUALS llamada_func','asignacion',3,'p_asignacion','obi_yacc.py',216),
  ('asignacion -> ID EQUALS objeto_metodo','asignacion',3,'p_asignacion','obi_yacc.py',217),
  ('asignacion -> objeto_aAcceso EQUALS expresion','asignacion',3,'p_asignacion','obi_yacc.py',218),
  ('asignacion -> objeto_aAcceso EQUALS llamada_func','asignacion',3,'p_asignacion','obi_yacc.py',219),
  ('asignacion -> objeto_aAcceso EQUALS objeto_metodo','asignacion',3,'p_asignacion','obi_yacc.py',220),
  ('asignacion -> ID LBRACKET exp RBRACKET EQUALS expresion','asignacion',6,'p_asignacion','obi_yacc.py',221),
  ('asignacion -> ID LBRACKET exp RBRACKET EQUALS llamada_func','asignacion',6,'p_asignacion','obi_yacc.py',222),
  ('asignacion -> ID LBRACKET exp RBRACKET EQUALS objeto_metodo','asignacion',6,'p_asignacion','obi_yacc.py',223),
  ('asignacion -> objeto_aAcceso LBRACKET exp RBRACKET EQUALS expresion','asignacion',6,'p_asignacion','obi_yacc.py',224),
  ('asignacion -> objeto_aAcceso LBRACKET exp RBRACKET EQUALS llamada_func','asignacion',6,'p_asignacion','obi_yacc.py',225),
  ('asignacion -> objeto_aAcceso LBRACKET exp RBRACKET EQUALS objeto_metodo','asignacion',6,'p_asignacion','obi_yacc.py',226),
  ('asignacion -> ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS expresion','asignacion',9,'p_asignacion','obi_yacc.py',227),
  ('asignacion -> ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS llamada_func','asignacion',9,'p_asignacion','obi_yacc.py',228),
  ('asignacion -> ID LBRACKET exp RBRACKET LBRACKET exp RBRACKET EQUALS objeto_metodo','asignacion',9,'p_asignacion','obi_yacc.py',229),
  ('asignacion -> objeto_aAcceso LBRACKET LBRACKET exp RBRACKET exp RBRACKET EQUALS expresion','asignacion',9,'p_asignacion','obi_yacc.py',230),
  ('asignacion -> objeto_aAcceso LBRACKET LBRACKET exp RBRACKET exp RBRACKET EQUALS llamada_func','asignacion',9,'p_asignacion','obi_yacc.py',231),
  ('asignacion -> objeto_aAcceso LBRACKET LBRACKET exp RBRACKET exp RBRACKET EQUALS objeto_metodo','asignacion',9,'p_asignacion','obi_yacc.py',232),
  ('objeto_metodo -> ID PERIOD llamada_func','objeto_metodo',3,'p_objeto_metodo','obi_yacc.py',246),
  ('llamada_func -> ID LPAREN aux RPAREN','llamada_func',4,'p_llamada_func','obi_yacc.py',249),
  ('aux -> exp','aux',1,'p_aux','obi_yacc.py',253),
  ('aux -> exp COMMA aux','aux',3,'p_aux','obi_yacc.py',254),
  ('expresion -> exp_bool','expresion',1,'p_expresion','obi_yacc.py',259),
  ('expresion -> exp_bool rel_op exp_bool','expresion',3,'p_expresion','obi_yacc.py',260),
  ('expresion -> exp_bool AND expresion','expresion',3,'p_expresion','obi_yacc.py',261),
  ('expresion -> exp_bool OR expresion','expresion',3,'p_expresion','obi_yacc.py',262),
  ('expresion -> exp_bool rel_op exp_bool AND expresion','expresion',5,'p_expresion','obi_yacc.py',263),
  ('expresion -> exp_bool rel_op exp_bool OR expresion','expresion',5,'p_expresion','obi_yacc.py',264),
  ('exp_bool -> TRUE','exp_bool',1,'p_exp_bool','obi_yacc.py',285),
  ('exp_bool -> FALSE','exp_bool',1,'p_exp_bool','obi_yacc.py',286),
  ('exp_bool -> exp','exp_bool',1,'p_exp_bool','obi_yacc.py',287),
  ('exp -> termino','exp',1,'p_exp','obi_yacc.py',293),
  ('exp -> exp PLUS termino','exp',3,'p_exp','obi_yacc.py',294),
  ('exp -> exp MINUS termino','exp',3,'p_exp','obi_yacc.py',295),
  ('termino -> factor','termino',1,'p_termino','obi_yacc.py',314),
  ('termino -> termino TIMES factor','termino',3,'p_termino','obi_yacc.py',315),
  ('termino -> termino DIVIDE factor','termino',3,'p_termino','obi_yacc.py',316),
  ('termino -> termino MODULO factor','termino',3,'p_termino','obi_yacc.py',317),
  ('factor -> LPAREN expresion RPAREN','factor',3,'p_factor','obi_yacc.py',335),
  ('factor -> PLUS objeto_aAcceso','factor',2,'p_factor','obi_yacc.py',336),
  ('factor -> MINUS objeto_aAcceso','factor',2,'p_factor','obi_yacc.py',337),
  ('factor -> PLUS var','factor',2,'p_factor','obi_yacc.py',338),
  ('factor -> MINUS var','factor',2,'p_factor','obi_yacc.py',339),
  ('factor -> var','factor',1,'p_factor','obi_yacc.py',340),
  ('factor -> objeto_aAcceso','factor',1,'p_factor','obi_yacc.py',341),
  ('var -> ID','var',1,'p_var','obi_yacc.py',348),
  ('var -> cint','var',1,'p_var','obi_yacc.py',349),
  ('var -> cfloat','var',1,'p_var','obi_yacc.py',350),
  ('var -> cchar','var',1,'p_var','obi_yacc.py',351),
  ('cint -> CINT','cint',1,'p_cint','obi_yacc.py',358),
  ('cfloat -> NUMBER','cfloat',1,'p_cfloat','obi_yacc.py',365),
  ('cchar -> CCHAR','cchar',1,'p_cchar','obi_yacc.py',371),
  ('rel_op -> LT','rel_op',1,'p_rel_op','obi_yacc.py',377),
  ('rel_op -> LE','rel_op',1,'p_rel_op','obi_yacc.py',378),
  ('rel_op -> GT','rel_op',1,'p_rel_op','obi_yacc.py',379),
  ('rel_op -> GE','rel_op',1,'p_rel_op','obi_yacc.py',380),
  ('rel_op -> EQ','rel_op',1,'p_rel_op','obi_yacc.py',381),
  ('rel_op -> NE','rel_op',1,'p_rel_op','obi_yacc.py',382),
  ('objeto_aAcceso -> ID PERIOD ID','objeto_aAcceso',3,'p_objeto_aAcceso','obi_yacc.py',388),
]
