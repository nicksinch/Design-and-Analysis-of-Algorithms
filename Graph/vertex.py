""" 
    A Class that represents a vertex in a Graph . 
    This allows us the vertex to have as many attributes as we need 
    which makes it more convenient.
"""

class Vertex:
    def __init__(self,value, color="white", arrival_time = 0, departure_time = 0,parent = None):
        self.__value = value # Could be a letter, string, char, whatever
        self.color = color
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.parent = parent
    
    @property
    def value(self):
        return self.__value

    def __lt__(self, other):
        return self.value < other.value
