class Parser:

    def __init__(self, file_name):

        with open(file_name, "r") as f:
            self.lines = f.readlines()

        self.current_line = None
        self.current_command = None

        if self.has_more_commands():

            self.current_line = 0
            self.current_command = self.lines[self.current_line]

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


    