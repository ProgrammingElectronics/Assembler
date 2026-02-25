import unittest
from main import *
from parser import *


class TestMainFunctionality(unittest.TestCase):

    def test_smoke(self):
        result = 2 + 2
        self.assertEqual(result, 4)


class TestParserFunctionality(unittest.TestCase):

    def test_constructor_stores_asm_lines(self):
        test_content = "// This file is part of www.nand2tetris.org\n"

        result = Parser("Add.asm")

        self.assertEqual(result.lines[0], test_content)


if __name__ == "__main__":
    unittest.main()
