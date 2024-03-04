
#class
Class Pet():
name = None
fullness = 0

def __init__(self, name):
    self.name = name
    
def eat(self, food):
    print(self.name + " is eating " + food + "...")
    self.fullness = 10