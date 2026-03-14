import unittest
from main import *
from parser import *


class TestMainFunctionality(unittest.TestCase):

    def test_smoke(self):
        result = 2 + 2
        self.assertEqual(result, 4)


class TestParserFunctionality(unittest.TestCase):

    def test_constructor_stores_only_asm_lines(self):
        test_content = "@2"

        result = Parser("Add.asm")

        self.assertEqual(result.lines[0], test_content)

    def test_has_more_commands_returns_false_with_empty_asm_file(self):

        result = Parser("test_empty.asm")

        self.assertFalse(result.has_more_commands())

    def test_has_more_commands_returns_true_with_full_asm_file(self):

        result = Parser("Add.asm")

        self.assertTrue(result.has_more_commands())

    def test_advance_has_next_command(self):

        test = 'D=A\n'

        result = Parser("Add.asm")
        result.advance()

        self.assertEqual(result.current_command, test)

    def test_command_type_returns_correct_command(self):

        test_A_COMMAND = Command_Type.A_COMMAND
        test_C_COMMAND = Command_Type.C_COMMAND
        test_L_COMMAND = Command_Type.L_COMMAND
        
        result = Parser("test_commands.asm")
        self.assertEqual(result.command_type(), test_A_COMMAND)
        result.advance()     
        self.assertEqual(result.command_type(), test_C_COMMAND)
        result.advance()     
        self.assertEqual(result.command_type(), test_L_COMMAND)

    def test_symbol_returns_correct_decimal(self):

        test_decimal = "0000111100001111"

        result = Parser("test_commands.asm")
        
        self.assertEqual(result.symbol(), test_decimal)


if __name__ == "__main__":
    unittest.main()
