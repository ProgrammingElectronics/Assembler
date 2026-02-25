class Parser:

    def __init__(self, file_name):

        with open(file_name, "r") as f:
            self.lines = f.readlines()

    def __str__(self):
        return f"{self.lines}"
