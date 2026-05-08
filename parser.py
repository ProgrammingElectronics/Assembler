from enum import Enum

class Command_Type(Enum):
    A_COMMAND = 0
    C_COMMAND = 1
    L_COMMAND = 2

class Parser:

    def __init__(self, file_name):

        with open(file_name, "r") as f:
            self.lines = f.read().splitlines()
             # print(f"with open {self.lines}")

        self.current_line = 0
        self.current_command = None

        if self.has_more_commands():
    
            self.remove_comments_and_spaces()
            self.current_line = 0
            self.current_command = self.lines[self.current_line]
            self.command_type()

    def __str__(self):
        return f"{self.lines}"

    def has_more_commands(self):

        if len(self.lines) >= self.current_line:
        # if len(self.lines) > 0 and len(self.lines) > self.current_line:
            return True
        else:
            return False

    def advance(self):
        
        if self.has_more_commands():
            
            #############################################
            # YOU ARE GOING OUT OF INDEX HERE
            #############################################
            self.current_line += 1 
            self.current_command = self.lines[self.current_line]
        else:

            return 0
    """
    If I wanted to make a more robust parser, I would deal with 
    end of line comments and such, but I am not. Making the toy assumption for 
    a specific format...
    """
    def remove_comments_and_spaces(self):
        
        clean_lines = []
        for line in self.lines:

            if not line.startswith("//") and line:
            
                clean_lines.append(line)

        self.lines = clean_lines
        # print(f"clean lines -> {self.lines}")

    def command_type(self):

        current_type = None
        first_char = self.current_command[0] 

        if first_char == "@":
            current_type = Command_Type.A_COMMAND
        elif first_char == "(":
            current_type = Command_Type.L_COMMAND
        else:
            current_type = Command_Type.C_COMMAND

        return current_type
        
    def symbol(self):

        current_symbol = None
        if self.command_type() == Command_Type.A_COMMAND: # E.g. @xxx
            current_symbol = self.current_command[1:]
        
        elif self.command_type() == Command_Type.L_COMMAND: # E.g. (LOOP)
            current_symbol = self.current_command[1:-1] # Remove starting and ending parenthesis
        
        return current_symbol
    
    def dest(self):
        
        dest = None
        idx = self.current_command.find("=")
    
        if idx > 0:
            dest = self.current_command[:idx] 
        
        return dest
    
    def comp(self):

        comp = None

        # Get index of "=", if not dest field, then set start_idx 0
        # Get index of ";", if not jump field, then set stop_idx -1
        # Return slic of currents command

        start_idx = self.current_command.find("=")
        if start_idx == -1:
            start_idx = 0
        else:
            start_idx +=1
        
        end_idx = self.current_command.find(";")
        if end_idx == -1:
            comp = self.current_command[start_idx:]
        else:
            comp = self.current_command[start_idx:end_idx]

        return comp
    

    def jump(self):

        jump = None

        idx = self.current_command.find(";")

        if idx > 0:
            idx += 1 # Do not include ;
            jump = self.current_command[idx:]

        return jump