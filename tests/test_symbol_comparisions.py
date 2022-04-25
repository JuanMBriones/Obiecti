import unittest
from semantical.symbol_tables import SymbolTable, ProcedureSymbol, Symbol
import logging

class TestSymbolComparisions(unittest.TestCase):
    symbol_table = SymbolTable()

    def test_compare_int_less_than(self):   
        self.symbol_table.add("num", "int", "variable", "global")
        self.symbol_table.add("num2", "int", "variable", "global")
        
        self.symbol_table.get("num").value = 1
        self.symbol_table.get("num2").value = 2

        num = self.symbol_table.get("num")
        num2 = self.symbol_table.get("num2")

        self.assertLess(num, num2)

    def test_compare_int_less_than_false(self):   
        self.symbol_table.add("num", "int", "variable", "global")
        self.symbol_table.add("num2", "int", "variable", "global")
        
        self.symbol_table.get("num").value = 1
        self.symbol_table.get("num2").value = 2

        num = self.symbol_table.get("num")
        num2 = self.symbol_table.get("num2")

        self.assertFalse(num>=num2)

    def test_compare_int_equal(self):   
        self.symbol_table.add("num", "int", "variable", "global")
        self.symbol_table.add("num2", "int", "variable", "global")
        
        self.symbol_table.get("num").value = 67
        self.symbol_table.get("num2").value = 67

        num = self.symbol_table.get("num")
        num2 = self.symbol_table.get("num2")

        self.assertEqual(num, num2)

    def test_compare_int_equal_false(self):   
        self.symbol_table.add("num", "int", "variable", "global")
        self.symbol_table.add("num2", "int", "variable", "global")
        
        self.symbol_table.get("num").value = 1
        self.symbol_table.get("num2").value = 2

        num = self.symbol_table.get("num")
        num2 = self.symbol_table.get("num2")

        self.assertNotEqual(num, num2)
    
    def test_compare_int_non_equal(self):   
        self.symbol_table.add("num", "int", "variable", "global")
        self.symbol_table.add("num2", "int", "variable", "global")
        
        self.symbol_table.get("num").value = 67
        self.symbol_table.get("num2").value = 69

        num = self.symbol_table.get("num")
        num2 = self.symbol_table.get("num2")

        self.assertTrue(num!=num2)

    def test_compare_int_non_equal_false(self):   
        self.symbol_table.add("num", "int", "variable", "global")
        self.symbol_table.add("num2", "int", "variable", "global")
        
        self.symbol_table.get("num").value = 1
        self.symbol_table.get("num2").value = 1

        num = self.symbol_table.get("num")
        num2 = self.symbol_table.get("num2")

        self.assertFalse(num!=num2)

    def test_compare_int_float_equal(self):
        self.symbol_table.add("num", "int", "variable", "global")
        self.symbol_table.add("num_float", "float", "variable", "global")
        
        self.symbol_table.get("num").value = 1
        self.symbol_table.get("num_float").value = 1.0

        num = self.symbol_table.get("num")
        num_float = self.symbol_table.get("num_float")

        self.assertEqual(num, num_float)
    


if __name__ == '__main__':
    unittest.main()