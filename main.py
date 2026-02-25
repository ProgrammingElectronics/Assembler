# Main Assembler program
# Will handle File I/O

import sys
from parser import *


def process_file(filename):
    with open(filename, "r") as f:
        return f.readlines()


if __name__ == "__main__":

    # Open asm file as list of lines
    lines = Parser(sys.argv[1])
    print(lines)

    # Create Symbol Table
    symbol_table = {}

    # First pass: update symbol table with labels

    # Second pass: translate commands
