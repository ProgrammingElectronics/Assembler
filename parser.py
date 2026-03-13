from enum import Enum

class Command_Type(Enum):
    A_COMMAND = 0
    B_COMMAND = 1
    C_COMMAND = 2

class Parser:

    def __init__(self, file_name):

        with open(file_name, "r") as f:
            self.lines = f.readlines()

        self.current_line = None
        self.current_command = None
        # self.type = None

        if self.has_more_commands():
    
            self.remove_comments_and_spaces()
            self.current_line = 0
            self.current_command = self.lines[self.current_line]
            self.command_type()

    def __str__(self):
        return f"{self.lines}"

    def has_more_commands(self):

        if self.lines:
            return True
        else:
            return False

    def advance(self):
        
        if self.has_more_commands():

            self.current_line += 1 
            self.current_command = self.lines[self.current_line]
        else:

            return 0
        
    def remove_comments_and_spaces(self):
        
        clean_lines = []
        for line in self.lines:

            line.strip()
            # print(f"line strip -> {line}")

            if not line.startswith("//") and not line.startswith("\n"):
                clean_lines.append(line)
                # print(clean_lines)

        self.lines = clean_lines
        # print(f"clean lines -> {self.lines}")

    def command_type(self):

        current_type = None

        first_char = self.current_command[0] 
        if first_char == "@":

            current_type = Command_Type.A_COMMAND

        return current_type
        
