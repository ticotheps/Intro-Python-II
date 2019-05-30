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
    def __repr__(self):
        returnString = f"-----------\n{self.name}\n\n {self.description}\n\n"
        returnString += f"\n\n{self.getRoomExitString()}\n\n"
    def getRoomExitString(self):
        exits = []
        if self.n_to is not None:
            exits.append("n")
        if self.s_to is not None:
            exits.append("s")
        if self.e_to is not None:
            exits.append("e")
        if self.w_to is not None:
            exits.append("w")
        return ", ".join(exits)