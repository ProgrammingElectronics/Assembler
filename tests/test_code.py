import unittest
from code import *
from parser import *

class TestCodeModuleFunctionality(unittest.TestCase):

    def test_dest_returns_correct_binary(self):
        
        test_binary = "010"
        
        mnemonic = Parser("test_commands.asm")
        mnemonic.advance()
        mnemonic.advance()

        dest_mnemonic = mnemonic.dest()
        Coder = Code()
        result = Coder.dest(dest_mnemonic)
        self.assertEqual(result, test_binary)
    
    def test_comp_returns_correct_binary(self):
        
        test_binary = "0000010"
        
        mnemonic = Parser("test_commands.asm")
        mnemonic.advance()
        mnemonic.advance()

        comp_mnemonic = mnemonic.comp()
        Coder = Code()
        result = Coder.comp(comp_mnemonic)
        self.assertEqual(result, test_binary)

    def test_jump_returns_correct_binary(self):
        
        test_binary = "010"
        
        mnemonic = Parser("test_commands.asm")
        mnemonic.advance()
        mnemonic.advance()
        mnemonic.advance()

        jump_mnemonic = mnemonic.jump()
        Coder = Code()
        result = Coder.jump(jump_mnemonic)
        self.assertEqual(result, test_binary)

if __name__ == "__main__":
    unittest.main()