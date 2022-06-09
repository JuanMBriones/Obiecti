from semantical.operations_codes import OperationCodes


class Operations:

    def __init__(self, functions_table, constants_table):
        self.functions_table = functions_table
        self.constants_table = constants_table

    def __set_value(self, address, value, name_func):
        '''Asigna un valor a una variable dentro de una función
        
        Parámetros
        ---------------
        address : int
            Dirección de la variable a la que se le va asignar el valor
        
        value : int
            Valor a asignar
            
        name_func : str
            Nombre de la función en la que se realizará la asignación'''
        
        if name_func == "global":
            #self.functions_table.print_func_size(name_func)
            self.functions_table.set_value(name_func, address, value)

    def __get_value(self, address, name_func):
        '''Regresa el valor de una variable dentro de una función
        
        Parámetros
        ---------------
        address : int
            Dirección de la variable de la que se va a regresar el valor
            
        name_func : str
            Nombre de la función en la que se realizará la asignación'''

        #   Si es mayor a 1600000, es una dirección en la tabla de constantes
        if address >= 1600000:
            value = self. constants_table.get(address)
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
        
        #   Checa si se busca la dirección en la tabla de variables global
        if name_func == "global":
            return self.functions_table.get_value(name_func, address)

    def assign_op(self, left_operand, result, name_func):
        '''Realiza la operación de asignación
        
        Parámetros
        ---------------
        left_operand : int
            Dirección del operador izquierdo
            
        result : int
            Dirección del resultado de la operación
            
        name_func : str
            Nombre de la función en la que se realizará la operación'''
        left_operand_value = self.__get_value(left_operand, name_func)
        self.__set_value(result, left_operand_value, name_func)

    def print_op(self, result, name_func):
        '''Realiza la operación de print
        
        Parámetros
        ---------------            
        result : int
            Dirección del resultado de la operación
            
        name_func : str
            Nombre de la función en la que se realizará la operación'''
        result_value = self.__get_value(result, name_func)
        print(result_value)
                
    def sum_op(self, left_operand, right_operand, result, name_func):
        '''Realiza la operación de suma
        
        Parámetros
        ---------------
        left_operand : int
            Dirección del operador izquierdo

        right_operand : int
            Dirección del operador derecho
            
        result : int
            Dirección del resultado de la operación
            
        name_func : str
            Nombre de la función en la que se realizará la operación'''
        left_operand_value = self.__get_value(left_operand, name_func)
        right_operand_value = self.__get_value(right_operand, name_func)
        result_value = left_operand_value + right_operand_value
        self.__set_value(result, result_value, name_func)

    def sub_op(self, left_operand, right_operand, result, name_func):
        '''Realiza la operación de resta
        
        Parámetros
        ---------------
        left_operand : int
            Dirección del operador izquierdo

        right_operand : int
            Dirección del operador derecho
            
        result : int
            Dirección del resultado de la operación
            
        name_func : str
            Nombre de la función en la que se realizará la operación'''
        left_operand_value = self.__get_value(left_operand, name_func)
        right_operand_value = self.__get_value(right_operand, name_func)
        result_value = left_operand_value - right_operand_value
        self.__set_value(result, result_value, name_func)

    def times_op(self, left_operand, right_operand, result, name_func):
        '''Realiza la operación de multiplicación
        
        Parámetros
        ---------------
        left_operand : int
            Dirección del operador izquierdo

        right_operand : int
            Dirección del operador derecho
            
        result : int
            Dirección del resultado de la operación
            
        name_func : str
            Nombre de la función en la que se realizará la operación'''
        left_operand_value = self.__get_value(left_operand, name_func)
        right_operand_value = self.__get_value(right_operand, name_func)
        result_value = left_operand_value * right_operand_value
        self.__set_value(result, result_value, name_func)

    def divide_op(self, left_operand, right_operand, result, name_func):
        '''Realiza la operación de división
        
        Parámetros
        ---------------
        left_operand : int
            Dirección del operador izquierdo

        right_operand : int
            Dirección del operador derecho
            
        result : int
            Dirección del resultado de la operación
            
        name_func : str
            Nombre de la función en la que se realizará la operación'''
        left_operand_value = self.__get_value(left_operand, name_func)
        right_operand_value = self.__get_value(right_operand, name_func)
        result_value = left_operand_value / right_operand_value
        self.__set_value(result, result_value, name_func)

    def modulo_op(self, left_operand, right_operand, result, name_func):
        '''Realiza la operación de modulo
        
        Parámetros
        ---------------
        left_operand : int
            Dirección del operador izquierdo

        right_operand : int
            Dirección del operador derecho
            
        result : int
            Dirección del resultado de la operación
            
        name_func : str
            Nombre de la función en la que se realizará la operación'''
        left_operand_value = self.__get_value(left_operand, name_func)
        right_operand_value = self.__get_value(right_operand, name_func)
        result_value = left_operand_value % right_operand_value
        self.__set_value(result, result_value, name_func)

    def lt_op(self, left_operand, right_operand, result, name_func):
        '''Realiza la operación de menor que
        
        Parámetros
        ---------------
        left_operand : int
            Dirección del operador izquierdo

        right_operand : int
            Dirección del operador derecho
            
        result : int
            Dirección del resultado de la operación
            
        name_func : str
            Nombre de la función en la que se realizará la operación'''
        left_operand_value = self.__get_value(left_operand, name_func)
        right_operand_value = self.__get_value(right_operand, name_func)
        result_value = left_operand_value < right_operand_value
        self.__set_value(result, result_value, name_func)

    def gt_op(self, left_operand, right_operand, result, name_func):
        '''Realiza la operación de mayor que
        
        Parámetros
        ---------------
        left_operand : int
            Dirección del operador izquierdo

        right_operand : int
            Dirección del operador derecho
            
        result : int
            Dirección del resultado de la operación
            
        name_func : str
            Nombre de la función en la que se realizará la operación'''
        left_operand_value = self.__get_value(left_operand, name_func)
        right_operand_value = self.__get_value(right_operand, name_func)
        result_value = left_operand_value > right_operand_value
        self.__set_value(result, result_value, name_func)

    def le_op(self, left_operand, right_operand, result, name_func):
        '''Realiza la operación de menor o igual que
        
        Parámetros
        ---------------
        left_operand : int
            Dirección del operador izquierdo

        right_operand : int
            Dirección del operador derecho
            
        result : int
            Dirección del resultado de la operación
            
        name_func : str
            Nombre de la función en la que se realizará la operación'''
        left_operand_value = self.__get_value(left_operand, name_func)
        right_operand_value = self.__get_value(right_operand, name_func)
        result_value = left_operand_value <= right_operand_value
        self.__set_value(result, result_value, name_func)

    def ge_op(self, left_operand, right_operand, result, name_func):
        '''Realiza la operación de mayor o igual que
        
        Parámetros
        ---------------
        left_operand : int
            Dirección del operador izquierdo

        right_operand : int
            Dirección del operador derecho
            
        result : int
            Dirección del resultado de la operación
            
        name_func : str
            Nombre de la función en la que se realizará la operación'''
        left_operand_value = self.__get_value(left_operand, name_func)
        right_operand_value = self.__get_value(right_operand, name_func)
        result_value = left_operand_value >= right_operand_value
        self.__set_value(result, result_value, name_func)

    def eq_op(self, left_operand, right_operand, result, name_func):
        '''Realiza la operación de igual que
        
        Parámetros
        ---------------
        left_operand : int
            Dirección del operador izquierdo

        right_operand : int
            Dirección del operador derecho
            
        result : int
            Dirección del resultado de la operación
            
        name_func : str
            Nombre de la función en la que se realizará la operación'''
        left_operand_value = self.__get_value(left_operand, name_func)
        right_operand_value = self.__get_value(right_operand, name_func)
        result_value = left_operand_value == right_operand_value
        self.__set_value(result, result_value, name_func)

    def ne_op(self, left_operand, right_operand, result, name_func):
        '''Realiza la operación de no igual que
        
        Parámetros
        ---------------
        left_operand : int
            Dirección del operador izquierdo

        right_operand : int
            Dirección del operador derecho
            
        result : int
            Dirección del resultado de la operación
            
        name_func : str
            Nombre de la función en la que se realizará la operación'''
        left_operand_value = self.__get_value(left_operand, name_func)
        right_operand_value = self.__get_value(right_operand, name_func)
        result_value = left_operand_value != right_operand_value
        self.__set_value(result, result_value, name_func)

    def and_op(self, left_operand, right_operand, result, name_func):
        '''Realiza la operación and
        
        Parámetros
        ---------------
        left_operand : int
            Dirección del operador izquierdo

        right_operand : int
            Dirección del operador derecho
            
        result : int
            Dirección del resultado de la operación
            
        name_func : str
            Nombre de la función en la que se realizará la operación'''
        left_operand_value = self.__get_value(left_operand, name_func)
        right_operand_value = self.__get_value(right_operand, name_func)
        result_value = None
        if left_operand_value and right_operand_value:
            result_value = True
        else:
            result_value = False
        self.__set_value(result, result_value, name_func)

    def or_op(self, left_operand, right_operand, result, name_func):
        '''Realiza la operación or
        
        Parámetros
        ---------------
        left_operand : int
            Dirección del operador izquierdo

        right_operand : int
            Dirección del operador derecho
            
        result : int
            Dirección del resultado de la operación
            
        name_func : str
            Nombre de la función en la que se realizará la operación'''
        left_operand_value = self.__get_value(left_operand, name_func)
        right_operand_value = self.__get_value(right_operand, name_func)
        result_value = None
        if left_operand_value or right_operand_value:
            result_value = True
        else:
            result_value = False
        self.__set_value(result, result_value, name_func)
