
class Quadruple:
    def __init__(self, operation, left_operand, right_operand, result):
        self.operation = operation
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.result = result
    
    def __str__(self):
        return f"[{self.operation}, {self.left_operand}, {self.right_operand}, {self.result}]"
    
    def __repr__(self):
        return f"[{self.operation}, {self.left_operand}, {self.right_operand}, {self.result}]"

    def get_quadruples(self):
        return [self.operation, self.left_operand, self.right_operand, self.result]

class Quadruples:
    def __init__(self):
        self.quadruples = []
        self.current_quadruple = 1
        self.operands_stack = []
        self.operators_stack = []

    def add_quadruple(self, quadruple):
        self.quadruples.append(quadruple)
    
    def get_quadruple(self, index):
        return self.quadruples[index].get_quadruples()

    def get_quadruple_element(self, index):
        return self.quadruples[index]

    def increment_current(self):
        self.current_quadruple += 1

    def get_current(self):
        return f"t{self.current_quadruple}"

    def get_quadruples(self):
        return {i: self.get_quadruple(i) for i in range(len(self.quadruples))}
