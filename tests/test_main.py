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

    def test_has_more_commands_returns_false_with_empty_asm_file(self):

        result = Parser("test_empty.asm")

        self.assertFalse(result.has_more_commands())

    def test_has_more_commands_returns_true_with_full_asm_file(self):

        result = Parser("Add.asm")

        self.assertTrue(result.has_more_commands())

    def test_advance_has_next_command(self):

        test = '// and the book "The Elements of Computing Systems"\n'

        result = Parser("Add.asm")
        result.advance()

        self.assertEqual(result.current_command, test)


if __name__ == "__main__":
    unittest.main()
