from ast import operator
from asyncio import constants
from stat import FILE_ATTRIBUTE_REPARSE_POINT
from turtle import right
from execution.memory import Memory
from execution.tables import ConstantTable, Function, ProcedureSymbol
from semantical.quadruples import Quadruple, Quadruples
from semantical.operations_codes import OperationCodes

quadruples = Quadruples()

def get_value(functions_table, constants_table, address):
    if address >= 1600000:
        value = constants_table.get(address)
        if type(value) is str:
            value = value.strip("\"")

        if address < 1700000:
            value = int(value)
        elif address < 1800000:
            value = float(value)
        elif address < OperationCodes.SUM: # 2100000
            if value == 'True':
                value = True
            elif value == 'False':
                value = False
        return value

    elif address < 1600000:
        return functions_table.get_value("global", address)
    

def set_value(functions_table, address, value):
    if address < 500000:
        functions_table.set_value("global", address, value)
    elif address < 1600000:
        functions_table.set_value("global", address, value)


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

    constants_good = []
    for constant in constants_text:
        constants_good.append(constant.strip().split(','))
    
    constants_table = ConstantTable()
    for constant in constants_good:
        constants_table.add(constant[0], constant[1])

    #constants_table = ConstantTable()
    #for constant in constants_text:
     #   constants_table.add(constant.strip())

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

    ip = 1
    while ip < len(quadruples.quadruples):
        cod_op = quadruples.quadruples[ip].get_operation()
        if cod_op == OperationCodes.SUM:
            left_operand = quadruples.quadruples[ip].get_left_operand()
            right_operand = quadruples.quadruples[ip].get_right_operand()
            result = quadruples.quadruples[ip].get_result()
            left_operand_value = get_value(functions_table, constants_table, left_operand)
            right_operand_value = get_value(functions_table, constants_table, right_operand)
            result_value = left_operand_value + right_operand_value
            set_value(functions_table, result, result_value)
            ip += 1
        elif cod_op == OperationCodes.MINUS:
            left_operand = quadruples.quadruples[ip].get_left_operand()
            right_operand = quadruples.quadruples[ip].get_right_operand()
            result = quadruples.quadruples[ip].get_result()
            left_operand_value = get_value(functions_table, constants_table, left_operand)
            right_operand_value = get_value(functions_table, constants_table, right_operand)
            result_value = left_operand_value - right_operand_value
            set_value(functions_table, result, result_value)
            ip += 1
        elif cod_op == OperationCodes.MULT:
            left_operand = quadruples.quadruples[ip].get_left_operand()
            right_operand = quadruples.quadruples[ip].get_right_operand()
            result = quadruples.quadruples[ip].get_result()
            left_operand_value = get_value(functions_table, constants_table, left_operand)
            right_operand_value = get_value(functions_table, constants_table, right_operand)
            result_value = left_operand_value * right_operand_value
            set_value(functions_table, result, result_value)
            ip += 1
        elif cod_op == OperationCodes.DIV:
            left_operand = quadruples.quadruples[ip].get_left_operand()
            right_operand = quadruples.quadruples[ip].get_right_operand()
            result = quadruples.quadruples[ip].get_result()
            left_operand_value = get_value(functions_table, constants_table, left_operand)
            right_operand_value = get_value(functions_table, constants_table, right_operand)
            result_value = left_operand_value / right_operand_value
            set_value(functions_table, result, result_value)
            ip += 1
        elif cod_op == OperationCodes.MOD:
            left_operand = quadruples.quadruples[ip].get_left_operand()
            right_operand = quadruples.quadruples[ip].get_right_operand()
            result = quadruples.quadruples[ip].get_result()
            left_operand_value = get_value(functions_table, constants_table, left_operand)
            right_operand_value = get_value(functions_table, constants_table, right_operand)
            result_value = left_operand_value % right_operand_value
            set_value(functions_table, result, result_value)
            ip += 1
        elif cod_op == 2100005:
            left_operand = quadruples.quadruples[ip].get_left_operand()
            left_operand_value = get_value(functions_table, constants_table, left_operand)
            result = quadruples.quadruples[ip].get_result()
            set_value(functions_table, result, left_operand_value)
            ip += 1
        elif cod_op == 2100006:
            left_operand = quadruples.quadruples[ip].get_left_operand()
            right_operand = quadruples.quadruples[ip].get_right_operand()
            result = quadruples.quadruples[ip].get_result()
            left_operand_value = get_value(functions_table, constants_table, left_operand)
            right_operand_value = get_value(functions_table, constants_table, right_operand)
            result_value = left_operand_value < right_operand_value
            set_value(functions_table, result, result_value)
            ip += 1
        elif cod_op == 2100007:
            left_operand = quadruples.quadruples[ip].get_left_operand()
            right_operand = quadruples.quadruples[ip].get_right_operand()
            result = quadruples.quadruples[ip].get_result()
            left_operand_value = get_value(functions_table, constants_table, left_operand)
            right_operand_value = get_value(functions_table, constants_table, right_operand)
            result_value = left_operand_value > right_operand_value
            set_value(functions_table, result, result_value)
            ip += 1
        elif cod_op == 2100008:
            left_operand = quadruples.quadruples[ip].get_left_operand()
            right_operand = quadruples.quadruples[ip].get_right_operand()
            result = quadruples.quadruples[ip].get_result()
            left_operand_value = get_value(functions_table, constants_table, left_operand)
            right_operand_value = get_value(functions_table, constants_table, right_operand)
            result_value = left_operand_value <= right_operand_value
            set_value(functions_table, result, result_value)
            ip += 1
        elif cod_op == 2100009:
            left_operand = quadruples.quadruples[ip].get_left_operand()
            right_operand = quadruples.quadruples[ip].get_right_operand()
            result = quadruples.quadruples[ip].get_result()
            left_operand_value = get_value(functions_table, constants_table, left_operand)
            right_operand_value = get_value(functions_table, constants_table, right_operand)
            result_value = left_operand_value >= right_operand_value
            set_value(functions_table, result, result_value)
            ip += 1
        elif cod_op == 2100010:
            left_operand = quadruples.quadruples[ip].get_left_operand()
            right_operand = quadruples.quadruples[ip].get_right_operand()
            result = quadruples.quadruples[ip].get_result()
            left_operand_value = get_value(functions_table, constants_table, left_operand)
            right_operand_value = get_value(functions_table, constants_table, right_operand)
            result_value = left_operand_value == right_operand_value
            set_value(functions_table, result, result_value)
            ip += 1
        elif cod_op == 2100011:
            left_operand = quadruples.quadruples[ip].get_left_operand()
            right_operand = quadruples.quadruples[ip].get_right_operand()
            result = quadruples.quadruples[ip].get_result()
            left_operand_value = get_value(functions_table, constants_table, left_operand)
            right_operand_value = get_value(functions_table, constants_table, right_operand)
            result_value = left_operand_value != right_operand_value
            set_value(functions_table, result, result_value)
            ip += 1
        elif cod_op == 2100012:
            left_operand = quadruples.quadruples[ip].get_left_operand()
            right_operand = quadruples.quadruples[ip].get_right_operand()
            result = quadruples.quadruples[ip].get_result()
            left_operand_value = get_value(functions_table, constants_table, left_operand)
            right_operand_value = get_value(functions_table, constants_table, right_operand)
            if left_operand_value and right_operand_value:
                result_value = True
            else:
                result_value = False
            set_value(functions_table, result, result_value)
            ip += 1
        elif cod_op == 2100013:
            left_operand = quadruples.quadruples[ip].get_left_operand()
            right_operand = quadruples.quadruples[ip].get_right_operand()
            result = quadruples.quadruples[ip].get_result()
            left_operand_value = get_value(functions_table, constants_table, left_operand)
            right_operand_value = get_value(functions_table, constants_table, right_operand)
            if left_operand_value or right_operand_value:
                result_value = True
            else:
                result_value = False
            set_value(functions_table, result, result_value)
            ip += 1
        elif cod_op == 2100014:
            ip = quadruples.quadruples[ip].get_result()
        elif cod_op == 2100015:
            left_operand = quadruples.quadruples[ip].get_left_operand()
            left_operand_value = get_value(functions_table, constants_table, left_operand)
            if left_operand_value == False:
                ip = quadruples.quadruples[ip].get_result()
            else:
                ip += 1
        elif cod_op == 2100020:
            result = quadruples.quadruples[ip].get_result()
            result_value = get_value(functions_table, constants_table, result)
            print(result_value)
            ip += 1

        
    """for key, value in quadruples.get_quadruples().items():
        print(f"{key}: {value}")
    print('Uff✨')"""