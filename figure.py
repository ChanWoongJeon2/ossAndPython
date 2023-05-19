import math

class line:

    __length = 0

    def __init__(self, length):
        self.__length = length

    def set_length(self, length):
        self.__length = length

    def get_length(self):
        return self.__length

def area_square(length):
    return length**2
    
def area_regular_triangle(length):
    return length**2*math.sqrt(3)/4

def area_circle(length):
    return length**2*math.pi