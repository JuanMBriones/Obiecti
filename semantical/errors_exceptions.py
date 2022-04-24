
class TypeMismatchError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        var_a -- input salary which caused the error
        var_b -- explanation of the error
    """

    def __init__(self, var_a, var_b, message="Type mismatch on variables: "):
        

        self.var_a = var_a
        self.var_b = var_b
        self.message = message + f"{self.var_a.name}({self.var_a.data_type}) and {var_b}({self.var_b.data_type})"
        super().__init__(self.message)
