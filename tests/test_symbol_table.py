import unittest
from semantical.symbol_tables import SymbolTable, ProcedureSymbol, Symbol
import logging

class TestSymbolTable(unittest.TestCase):
    symbol_table = SymbolTable()

    def test_symbol_table_empty(self):   
        self.assertEqual(self.symbol_table.get('a_random_num'), None)

    def test_symbol_table_one_var(self):
        self.symbol_table.add("a", "int", "variable", "global")
        self.assertEqual(self.symbol_table.get('a'), Symbol("a", "int", "global"))

    def test_symbol_table_one_var_false(self):
        self.assertEqual(self.symbol_table.add("a", "int", "variable", "global"), None)

    def test_symbol_table_two_vars(self):
        self.symbol_table.add('foo', 'int', 'procedure', 'local', ['param1'])
        self.assertEqual(self.symbol_table.get('foo'), ProcedureSymbol('foo', 'int', 'local', ['param1']))
    
    def test_symbol_table_two_vars_false(self):
        self.assertEqual(self.symbol_table.add('foo', 'int', 'procedure', 'local'), None)
    
    def test_total_vars(self):
        self.symbol_table.add("a", "int", "variable", "global")
        self.symbol_table.add("foo", "int", "procedure", "global")
        self.assertNotEqual(self.symbol_table.get_all_variables_names(), ['a', 'foo'])

    def test_singleton_instance(self):
        new_symbol_table = SymbolTable()
        self.assertEqual(new_symbol_table, self.symbol_table)
    
    def test_singleton_instance_total_vars(self):
        new_symbol_table = SymbolTable()
        self.assertEqual(new_symbol_table.get_all_variables_names(), self.symbol_table.get_all_variables_names())

    def test_singleton_instance_total_vars_after_assigment(self):
        new_symbol_table = SymbolTable()
        self.symbol_table.add("a", "int", "variable", "global")
        self.assertEqual(new_symbol_table.get_all_variables_names(), self.symbol_table.get_all_variables_names())
    
    def test_symboltable_free_var(self):
        if not self.symbol_table.get('a'):
            self.symbol_table.add("a", "int", "variable", "global")
        
        self.symbol_table.free_variable("a")
        self.assertEqual(self.symbol_table.get('a'), None)

    def test_symboltable_free_all(self):
        self.symbol_table.free_all_variables()

        self.assertEqual(len(self.symbol_table.get_all_variables_names()), 0)


if __name__ == '__main__':
    unittest.main()