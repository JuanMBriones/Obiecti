from ast import operator
from stat import FILE_ATTRIBUTE_REPARSE_POINT
from turtle import right
from execution.memory import Memory
from execution.tables import ConstantTable, Function, ProcedureSymbol
from semantical.quadruples import Quadruple, Quadruples

globalMemory = Memory()
quadruples = Quadruples()

def add(left_operand, right_operand):
    print(left_operand + right_operand)

def read_file(file):
    functions_text = []
    constants_text = []
    quadruples_text = []
    with open(file) as object_file:
        line = object_file.readlines()
        first_separator = line.index('%%\n')
        line.remove('%%\n')
        second_separator = line.index('%%\n')
        for i in range(first_separator):
            functions_text.append(line[i])

        for i in range(first_separator, second_separator):
            constants_text.append(line[i])

        for i in range(second_separator + 1, len(line)):
            quadruples_text.append(line[i])
            
    functions_text_strip = []
    for function in functions_text:
        functions_text_strip.append(function.strip('\n'))
    
    functions_good = []
    for function in functions_text_strip:
        functions_good.append(function.split(';'))

    functions_table = ProcedureSymbol(functions_good[0][3])
    functions_good.pop(0)

    for function in functions_good:
        functions_table.add_method(function[0], function[1], function[2], function[3], function[4])

    constants_table = ConstantTable()
    for constant in constants_text:
        constants_table.add(constant.strip())
    

    quadruples_text_strip = []
    for quadruple in quadruples_text:
        quadruples_text_strip.append(quadruple.strip('[]\n'))

    quadruples_good = []
    for quadruple in quadruples_text_strip:
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

    