import math

class Container:
    ''' This is a meta class that's supposed to NOT have an initializer.
        It's only to be extended upon.
    '''
    def __init__(self):
        pass

class Box(Container):
    ''' A cuboid box, having width, depth, and height.
        When initializing the dimensions should be in cm.
        The dimcost is the sum of all three sides.
    '''
    def __init__(self, width, depth, height):
        self.width = width
        self.depth = depth
        self.height = height
        self.dim_cost = width + depth + height
        self.volume = width * depth * height

class Cylinder(Container):
    ''' A cylindrical tube, having length and diameter.
        It is used for shipping long things like rolled posters.
        Both dimensions should be in cm.
    '''
    def __init__(self, length, diameter):
        self.length = length
        self.diameter = diameter
        self.dim_cost = pi * diameter
        self.volume = pi * (diameter / 2) ** 2


mybox = Box(10,10,10,)

print(mybox.width, mybox.depth, mybox.height, mybox.volume)