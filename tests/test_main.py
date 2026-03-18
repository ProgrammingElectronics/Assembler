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

        test = 'D=A'

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

    def test_symbol_returns_correct_decimal_for_A_COMMAND(self):

        test_decimal = "2"

        result = Parser("Add.asm")
        
        self.assertEqual(result.symbol(), test_decimal)
    
    def test_symbol_returns_correct_symbol_for_L_COMMAND(self):

        test_symbol = "LOOP"

        result = Parser("test_commands.asm")
        result.advance()
        result.advance()

        self.assertEqual(result.symbol(), test_symbol)

    def test_dest_returns_correct_mnemonic(self):

        test_dest_mnemonic = "D"

        result = Parser("test_commands.asm")
        result.advance()

        self.assertEqual(result.dest(), test_dest_mnemonic)

    def test_dest_returns_none_if_command_type_is_not_C(self):

        test_dest_mnemonic = None

        result = Parser("test_commands.asm")
        
        self.assertEqual(result.dest(), test_dest_mnemonic)


    def test_comp_returns_correct_comp_mnemonics(self):

        test_comp_mnemonic = "A" 
        
        # Switch to different test file just for comp
        result = Parser("Add.asm")
        result.advance()

        self.assertEqual(result.comp(), test_comp_mnemonic)
        result.advance()
        self.assertEqual(result.comp(), test_comp_mnemonic)

if __name__ == "__main__":
    unittest.main()
