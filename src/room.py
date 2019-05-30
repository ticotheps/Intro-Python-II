# Implement a class to hold room information. This should have name and
# description attributes.

# Define room class before player class.
# This should only take about 20 lines of code to define your room class.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None 
        self.e_to = None 
        self.w_to = None  
    def __str__(self):
        return f"-----------\n{self.name}\n\n {self.description}\n\n"