import unittest
from semantical.symbol_tables import SymbolTable, ProcedureSymbol, Symbol
from semantical.semantic_cube import SemanticCube
import logging

class TestSymbolOperations(unittest.TestCase):
    symbol_table = SymbolTable()

    def test_compare_int_less_than(self):   
        self.symbol_table.add("num", "int", "variable", "global")
        self.symbol_table.add("num2", "int", "variable", "global")
        
        self.symbol_table.get("num").value = 1
        self.symbol_table.get("num2").value = 2

        num = self.symbol_table.get("num")
        num2 = self.symbol_table.get("num2")

        self.assertLess(num, num2)

    def test_sum_int_float(self):
        self.symbol_table.free_all_variables()
        self.symbol_table.add("num", "int", "variable", "global")
        self.symbol_table.add("num2", "float", "variable", "global")
        
        self.symbol_table.get("num").value = 1
        self.symbol_table.get("num2").value = 2.0

        num = self.symbol_table.get("num")
        num2 = self.symbol_table.get("num2")


        result = num + num2
        self.assertTrue(result == 3.0 and isinstance(result, float))
    
    def test_sum_int_int(self):
        self.symbol_table.free_all_variables()
        self.symbol_table.add("num", "int", "variable", "global")
        self.symbol_table.add("num2", "int", "variable", "global")
        
        self.symbol_table.get("num").value = 1
        self.symbol_table.get("num2").value = 2.0

        num = self.symbol_table.get("num")
        num2 = self.symbol_table.get("num2")


        result = num + num2
        self.assertTrue(result == 3 and isinstance(result, int))

if __name__ == '__main__':
    unittest.main()