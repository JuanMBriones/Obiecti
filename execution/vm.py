from ast import operator
from turtle import right
from execution.memory import Memory
from semantical.quadruples import Quadruple, Quadruples

globalMemory = Memory()
quadruples = Quadruples()

def add(left_operand, right_operand):
    print(left_operand + right_operand)

def read_file(file):
    with open(file) as object_file:
        line = object_file.readlines()

    print(line)

    """ quadruples_text = []
    for quadruple in line:
        quadruples_text.append(quadruple.strip('[]\n'))

    quadruples_good = []
    for quadruple in quadruples_text:
        quadruples_good.append(quadruple.split(','))

    for quadruple in quadruples_good:
        operator = int(quadruple[0])
        left_operand = int(quadruple[1])
        right_operand = int(quadruple[2])
        result = int(quadruple[3])
        q = Quadruple(operator, left_operand, right_operand, result)
        quadruples.add_quadruple(q)
        
    for key, value in quadruples.get_quadruples().items():
        print(f"{key}: {value}")
    print('Uff✨')
    
    for ip in quadruples.get_quadruples():
        operator = quadruples.quadruples[ip].get_operation()
        if operator == 2100005:
            print("Hola")
        elif operator == 2100014:
            print("Hola otra vez") """
    

    