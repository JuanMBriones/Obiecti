import unittest
from semantical.symbol_tables import SymbolTable, ProcedureSymbol, Symbol

class TestSymbolTable(unittest.TestCase):
    symbol_table = SymbolTable()

    def test_symbol_table_empty(self):   
        self.assertEqual(self.symbol_table.get('num'), None)

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
        self.assertNotEqual(self.symbol_table.get_all_variables_names(), ['a', 'foo'])

if __name__ == '__main__':
    unittest.main()