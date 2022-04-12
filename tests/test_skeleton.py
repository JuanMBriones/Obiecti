import unittest
from compile import test_syntax

class TestSkeleton(unittest.TestCase):
    file_name = "ejemplo.txt"

    def test_skeleton(self):    
        self.assertEqual(test_syntax(self.file_name), "Apropiado")

    def test_skeleton_false(self):
        self.assertNotEqual(test_syntax(self.file_name), "Syntax error in input!")

if __name__ == '__main__':
    unittest.main()