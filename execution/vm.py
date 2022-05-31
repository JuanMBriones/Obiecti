from execution.memory import Memory
from semantical.quadruples import Quadruple, Quadruples

globalMemory = Memory()
quadruples = Quadruples()

def add(left_operand, right_operand):
    print(left_operand + right_operand)

def read_file(file):
    with open(file) as object_file:
        line = object_file.read()

    text_quadruples = line.split('\n')
    text_quadruples_stripped = []
    for quadruple in text_quadruples:
        text_quadruples_stripped.append(quadruple.strip())

    text_quadruples_wb = []
    for quadruple in text_quadruples_stripped:
        text_quadruples_wb.append(quadruple.strip('[]'))

    text_quadruples_wc = []
    for quadruple in text_quadruples_wb:
        text_quadruples_wc.append(quadruple.split(','))
    
    for text_quadruple in text_quadruples_wc:
        operator = text_quadruple[0]
        left_operand = text_quadruple[1]
        right_operand = text_quadruple[2]
        result = text_quadruple[3]
        quadruple = Quadruple(operation=operator, left_operand=left_operand, right_operand=right_operand, result=result)
        quadruples.add_quadruple(quadruple)
        quadruples.increment_current()



    ip = 0
    if quadruples.get_quadruple(ip)[0] == '*':
        print("JALA")