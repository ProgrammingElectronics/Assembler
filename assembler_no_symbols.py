from parser import Parser, Command_Type

def main():

    asm = Parser("asm_files/RectL.asm")
    
    while asm.has_more_commands():

        print(f"{asm.has_more_commands()} line # {asm.current_line}")
        asm.advance()

        # print(asm.current_line)
        # Core algorithm
        # Parse out the dest, comp, and jump mnemonics
        
        # check symbol
        # if line.command_type() == Command_Type.A_COMMAND:
        #     print(line)
            # with open("RectL.hack", "w") as f:
            #     f.write(line.current_command)       
        

        # concat each in order
        # paste line into hack file
        
  
        # If not line
            # End

if __name__ == "__main__":
    main()