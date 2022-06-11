from lib2to3.pgen2.token import OP
from webbrowser import Opera
from execution.memory import Memory
from execution.operations import Operations
from execution.tables import ConstantTable, Function, ProcedureSymbol
from semantical.quadruples import Quadruple, Quadruples
from semantical.operations_codes import OperationCodes

quadruples = Quadruples()

def get_value(functions_table, constants_table, address, func_address):
    if address >= 1600000:
        value = constants_table.get(address)
        if type(value) is str:
            value = value.strip("\"")
        if address < 1700000:
            value = int(value)
        elif address < 1800000:
            value = float(value)
        elif address < int(OperationCodes.SUM): # 2100000
            if value == 'True':
                value = True
            elif value == 'False':
                value = False
        return value

    if func_address == None:
        return functions_table.get_value("global", address)
    else:
        is_global = functions_table.is_var_global(address)
        if is_global != None:
            return is_global
        else:
            name_func = functions_table.get_name_func(func_address)
            return functions_table.get_value(name_func, address)
    

def set_value(functions_table, address, value, func_address):
    #print("Func address:", func_address)
    if func_address == None:
        if address < 500000:
            functions_table.set_value("global", address, value)
        elif address < 1600000:
            functions_table.set_value("global", address, value)
    else:
        '''Busca si una variable es global cuando estamos dentro de una función y 
        le asigna un valor. Si no es global, busca en memoria local y le asigna un
        valor'''
        #print("Set value address:", address)
        is_global = functions_table.is_var_global(address)

        #print("Is global:", is_global)
        if is_global != None:
            functions_table.set_value("global", address, value)
        else:
            #functions_table.get_all_methods()
            #print("Set value:", address, value, func_address)
            name_func = functions_table.get_name_func(func_address)
            #print("Name func:", name_func)

            #print("Set value:", value)
            functions_table.set_value(name_func, address, value)

def debug(functions_table, constants_table):

    print(f"===Functions====")
    for key, value in functions_table.debug().items():
        print(f"\t{key}")

        print(f"\t\tdirBase: {value['initial_address']}")
        print(f"\t\tsize: {value['size']}")
        print(f"\t\tparams: {value['params']}")
        #print(f"\t\tLOCAL MEMORY")

        for memory_type, memory_list in value.items():
            if memory_type not in {'initial_address', 'size', 'params'}:
                print(f"\t\t{memory_type} ")
                for type, list_type in memory_list.items(): #value['local_memory'].items():
                    print(f"\t\t\t{type}")
                    for info_var in list_type:
                        print(f"\t\t\t\t{info_var['index']}(index): {info_var['value']}")

    print(f"===Constants====")
    for key, value in constants_table.debug().items():
        print(f"\tAddress: {value['address']}    Value: {value['value']}")
                
        
def cast_to_type(value, address):
    if address < 500000:        #   Variable global
        if address >= 0 and address < 100000:
            value = int(value)
        elif address >= 100000 and address < 200000:
            value = float(value)
        elif address >= 200000 and address < 300000:
            pass # char
        elif address >= 400000 and address < 500000:
            value = bool(value)
    elif address < 1000000:     #   Variable local
        if address >= 500000 and address < 600000:
            value = int(value)
        elif address >= 600000 and address < 700000:
            value = float(value)
        elif address >= 700000 and address < 800000:
            pass # char
        elif address >= 900000 and address < 1000000:
            value = bool(value)
    elif address < 1600000:     #   Variable temporal
        if address >= 1000000 and address < 1100000:
            value = int(value)
        elif address >= 1100000 and address < 1200000:
            value = float(value)
        elif address >= 1200000 and address < 1300000:
            pass # char
        elif address >= 1400000 and address < 1500000:
            value = bool(value)
    
    return value


def read_file(file="object.txt"):
    functions_text = []
    constants_text = []
    quadruples_text = []
    jump_stack = []

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
    functions_stack = ["global"]
    for function in functions_good:
        #print(function[0])
        if function[0] == "main":
            functions_table.add_method(function[0], function[1], function[2], function[3], function[4])
            functions_stack.append(function[0])
            break
        #functions_table.add_method(function[0], function[1], function[2], function[3], function[4])


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
        try:
            result = int(quadruple[3])
        except:
            result = quadruple[3]
        q = Quadruple(operator, left_operand, right_operand, result)
        quadruples.add_quadruple(q)

    operations = Operations(functions_table, constants_table)

    ip = 0
    try:
        while ip < len(quadruples.quadruples):
            name_func = functions_table.get_name_func(ip)
            #print(name_func, ip)
            #print(ip)
            #print(functions_stack)
            """if name_func != "global":
                #print(name_func)
                if functions_stack.count(ip) < 1:
                    print('ENTRO')
                    functions_stack.append(ip)""" # DE MIENTRAS ESTA COMENTADO BY THE MOMENT
            #print(functions_stack)
            cod_op = quadruples.quadruples[ip].get_operation()

            left = quadruples.quadruples[ip].get_left_operand()
            right = quadruples.quadruples[ip].get_right_operand()
            result = quadruples.quadruples[ip].get_result()
            print('👴🏻')
            if type(left) == str and '*' in left:
                left = left[3:len(left)-1]
                #real_address = get_value(functions_table, constants_table, int(left), functions_stack[-1])
                quadruples.quadruples[ip].left_operand = operations.change_reference(int(left), functions_stack[-1])
            if type(right) == str and '*' in right:
                right = right[3:len(right)-1]
                #real_address = get_value(functions_table, constants_table, int(right), functions_stack[-1])
                quadruples.quadruples[ip].right_operand = operations.change_reference(int(right), functions_stack[-1])
            if type(result) == str and '*' in result:
                result = result[3:len(result)-1]
                #real_address = get_value(functions_table, constants_table, int(result), functions_stack[-1])
                quadruples.quadruples[ip].result = operations.change_reference(int(result), functions_stack[-1])
            print('🎉')
            if cod_op == int(OperationCodes.SUM):
                left_operand = quadruples.quadruples[ip].get_left_operand()
                right_operand = quadruples.quadruples[ip].get_right_operand()
                result = quadruples.quadruples[ip].get_result()
                operations.sum_op(left_operand, right_operand, result, functions_stack[-1])
                ip += 1
            elif cod_op == int(OperationCodes.MINUS):
                left_operand = quadruples.quadruples[ip].get_left_operand()
                right_operand = quadruples.quadruples[ip].get_right_operand()
                result = quadruples.quadruples[ip].get_result()
                operations.sub_op(left_operand, right_operand, result, functions_stack[-1])
                ip += 1
            elif cod_op == int(OperationCodes.MULT):
                left_operand = quadruples.quadruples[ip].get_left_operand()
                right_operand = quadruples.quadruples[ip].get_right_operand()
                result = quadruples.quadruples[ip].get_result()
                operations.times_op(left_operand, right_operand, result, functions_stack[-1])
                ip += 1
            elif cod_op == int(OperationCodes.DIV):
                left_operand = quadruples.quadruples[ip].get_left_operand()
                right_operand = quadruples.quadruples[ip].get_right_operand()
                result = quadruples.quadruples[ip].get_result()
                operations.divide_op(left_operand, right_operand, result, functions_stack[-1])
                ip += 1
            elif cod_op == int(OperationCodes.MOD):
                left_operand = quadruples.quadruples[ip].get_left_operand()
                right_operand = quadruples.quadruples[ip].get_right_operand()
                result = quadruples.quadruples[ip].get_result()
                operations.modulo_op(left_operand, right_operand, result, functions_stack[-1])
                ip += 1
            elif cod_op == int(OperationCodes.ASSIGN):
                left_operand = quadruples.quadruples[ip].get_left_operand()
                result = quadruples.quadruples[ip].get_result()
                operations.assign_op(left_operand, result, functions_stack[-1])
                ip += 1
            elif cod_op == int(OperationCodes.LT):
                left_operand = quadruples.quadruples[ip].get_left_operand()
                right_operand = quadruples.quadruples[ip].get_right_operand()
                result = quadruples.quadruples[ip].get_result()
                operations.lt_op(left_operand, right_operand, result, functions_stack[-1])
                ip += 1
            elif cod_op == int(OperationCodes.GT):
                left_operand = quadruples.quadruples[ip].get_left_operand()
                right_operand = quadruples.quadruples[ip].get_right_operand()
                result = quadruples.quadruples[ip].get_result()
                operations.gt_op(left_operand, right_operand, result, functions_stack[-1])
                ip += 1
            elif cod_op == int(OperationCodes.LE):
                left_operand = quadruples.quadruples[ip].get_left_operand()
                right_operand = quadruples.quadruples[ip].get_right_operand()
                result = quadruples.quadruples[ip].get_result()
                operations.le_op(left_operand, right_operand, result, functions_stack[-1])
                ip += 1
            elif cod_op == int(OperationCodes.GE):
                left_operand = quadruples.quadruples[ip].get_left_operand()
                right_operand = quadruples.quadruples[ip].get_right_operand()
                result = quadruples.quadruples[ip].get_result()
                operations.ge_op(left_operand, right_operand, result, functions_stack[-1])
                ip += 1
            elif cod_op == int(OperationCodes.EQ):
                left_operand = quadruples.quadruples[ip].get_left_operand()
                right_operand = quadruples.quadruples[ip].get_right_operand()
                result = quadruples.quadruples[ip].get_result()
                operations.eq_op(left_operand, right_operand, result, functions_stack[-1])
                ip += 1
            elif cod_op == int(OperationCodes.NE):
                left_operand = quadruples.quadruples[ip].get_left_operand()
                right_operand = quadruples.quadruples[ip].get_right_operand()
                result = quadruples.quadruples[ip].get_result()
                operations.ne_op(left_operand, right_operand, result, functions_stack[-1])
                ip += 1
            elif cod_op == int(OperationCodes.AND):
                left_operand = quadruples.quadruples[ip].get_left_operand()
                right_operand = quadruples.quadruples[ip].get_right_operand()
                result = quadruples.quadruples[ip].get_result()
                operations.and_op(left_operand, right_operand, result, functions_stack[-1])
                ip += 1
            elif cod_op == int(OperationCodes.OR):
                left_operand = quadruples.quadruples[ip].get_left_operand()
                right_operand = quadruples.quadruples[ip].get_right_operand()
                result = quadruples.quadruples[ip].get_result()
                operations.or_op(left_operand, right_operand, result, functions_stack[-1])
                ip += 1
            elif cod_op == int(OperationCodes.GOTO):
                ip = quadruples.quadruples[ip].get_result()
            elif cod_op == int(OperationCodes.GOTOF):
                left_operand = quadruples.quadruples[ip].get_left_operand()
                left_operand_value = operations.goto_op(left_operand, functions_stack[-1])
                if left_operand_value == False:
                    ip = quadruples.quadruples[ip].get_result()
                else:
                    ip += 1
            elif cod_op == int(OperationCodes.ENDFUNC):             # ENDFUNC
                #functions_stack.pop()
                #main_address = functions_table.get_method('main').initial_address
                if functions_stack[-1] != "main": # main
                    ip = jump_stack.pop()
                else:
                    ip += 1
                functions_stack.pop()
                #else: 
                #functions_stack.pop()
            elif cod_op == int(OperationCodes.PRINT):             # PRINT
                result = quadruples.quadruples[ip].get_result()

                #if type(result) == 'str':
                print('☠️☠️☠️☠️☠️☠️☠️', type(result))
                operations.print_op(result, functions_stack[-1])
                ip += 1
            elif cod_op == int(OperationCodes.ERA):            # ERA
                name_func_address = quadruples.quadruples[ip].get_result()                
                for function in functions_good:
                    if int(function[2]) == int(name_func_address):
                        operations.add_method(function[0], function[1], function[2], function[3], function[4])
                        functions_stack.append(function[0])  
                        break

                #print(functions_stack)

                #print(functions_table.get_all_func_directions())

                ip += 1
            elif cod_op == int(OperationCodes.RETURN):            # RETURN
                left_operand = quadruples.quadruples[ip].get_left_operand()    
                result = quadruples.quadruples[ip].get_result()
                name_function = functions_stack[-1]
                operations.return_op(left_operand, result, name_function)
                ip += 1
            elif cod_op == int(OperationCodes.GOSUB):
                jump_stack.append(ip + 1)
                ip = operations.gosub_op(functions_stack[-1])
            elif cod_op == int(OperationCodes.PARAM):
                actual_function = functions_stack.pop()
                left_operand = quadruples.quadruples[ip].get_left_operand()
                result = quadruples.quadruples[ip].get_result()
                operations.param_op(left_operand, result, functions_stack[-1], actual_function)
                functions_stack.append(actual_function)
                ip += 1
            elif cod_op == int(OperationCodes.VER):
                left_operand_address = quadruples.quadruples[ip].get_left_operand()
                right_operand = quadruples.quadruples[ip].get_right_operand()
                result = quadruples.quadruples[ip].get_result()
                
                operations.ver_value(left_operand_address, right_operand, result, functions_stack[-1])
                #right_operand_address = quadruples.quadruples[ip].get_right_operand()

                
                #right_operand_value = get_value(functions_table, constants_table, right_operand_address, functions_stack[-1])

                #result = 
                #result_value = get_value(functions_table, constants_table, result, functions_stack[-1])
                #set_value(functions_table, left_operand, result_value, None)
                ip += 1
            elif cod_op == int(OperationCodes.MULTDIR):
                # name_func, left_operand_address, right_operand, result_address):
                left_operand_address = quadruples.quadruples[ip].get_left_operand()
                right_operand = int(quadruples.quadruples[ip].get_right_operand())
                operations.mult_dir(functions_stack[-1], left_operand_address, right_operand, quadruples.quadruples[ip].result)
                ip += 1
            elif cod_op == int(OperationCodes.SUMDIR):
                left_operand_address = quadruples.quadruples[ip].get_left_operand()
                right_operand = quadruples.quadruples[ip].get_right_operand()
                """result_address = quadruples.quadruples[ip].get_result()

                left_operand_value = get_value(functions_table, constants_table, left_operand_address, functions_stack[-1])
                address_index = left_operand_value + int(right_operand)

                set_value(functions_table, quadruples.quadruples[ip].result, address_index, functions_stack[-1])"""
                # left_operand_address, right_operand, name_func, result):
                operations.sum_dir(left_operand_address, right_operand, functions_stack[-1], quadruples.quadruples[ip].result)
                ip += 1
            elif cod_op == int(OperationCodes.ASSIGNDIR):
                left_operand_value = quadruples.quadruples[ip].get_left_operand()
                result_address = quadruples.quadruples[ip].get_result()
                """try: 
                    left_operand_value = get_value(functions_table, constants_table, quadruples.quadruples[ip].get_left_operand(), functions_stack[-1])
                except:
                    left_operand_value = quadruples.quadruples[ip].get_left_operand()
                # the result_part of quadruple is a pointr to the address of the variable
                
                real_address = get_value(functions_table, constants_table, result_address, functions_stack[-1])
                
                set_value(functions_table, real_address, left_operand_value, functions_stack[-1])"""

                operations.assign_dir(left_operand_value, result_address, functions_stack[-1])
                ip += 1
            elif cod_op == int(OperationCodes.READ):
                result_address = quadruples.quadruples[ip].get_result()

                input_value = input()
                input_value = cast_to_type(input_value, result_address)

                operations.read_op(result_address, functions_stack[-1], input_value)

                #set_value(functions_table, result_address, input_value, functions_stack[-1])

                ip += 1
            elif cod_op == int(OperationCodes.FIND):
                left_operand_address = quadruples.quadruples[ip].get_left_operand()
                right_operand_address = quadruples.quadruples[ip].get_right_operand()
                result_address = quadruples.quadruples[ip].get_result()
                #print('🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧🚧')
                to_find = get_value(functions_table, constants_table, result_address, functions_stack[-1])
                current_address = left_operand_address
                res = -1
                index = 0
                while(current_address <= right_operand_address):
                    current_value = get_value(functions_table, constants_table, current_address, functions_stack[-1])
                    if int(current_value) == int(to_find):
                        res = index
                        break

                    current_address += 1
                    index += 1
                
                print(res)
                ip += 1
            elif cod_op == int(OperationCodes.SORT):
                #[2100030, 500001, 500010, 500000]

                left_operand_address = quadruples.quadruples[ip].get_left_operand()
                right_operand_address = quadruples.quadruples[ip].get_right_operand()
                result_address = quadruples.quadruples[ip].get_result()

                current_address = left_operand_address
                lst = []
                while(current_address <= right_operand_address):
                    current_value = get_value(functions_table, constants_table, current_address, functions_stack[-1])
                    lst.append(current_value)
                    current_address += 1
                
                lst.sort()
                #print(f'❄️❄️❄️❄️❄️❄️❄️❄️', len(lst))
                current_address = left_operand_address
                index = 0
                while(current_address <= right_operand_address):
                    set_value(functions_table, current_address, lst[index], functions_stack[-1])

                    index += 1
                    current_address += 1
                ip += 1

            else:
                #print(cod_op)
                ip += 1
            
    except Exception as e:
        print(f"FAILED on Instruction Pointer {ip}")
        print(quadruples.quadruples[ip])
        debug(functions_table, constants_table)
        print(f"Stack trace")
        print(f"\t\t{e}")
        
    """for key, value in quadruples.get_quadruples().items():
        print(f"{key}: {value}")
    print('Uff✨')"""
    print('End🚀')
    debug(functions_table, constants_table)