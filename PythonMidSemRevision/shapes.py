import math

def square_metrics(side):
    area = side ** 2
    perimeter = 4 * side
    return area, perimeter

def circle_metrics(radius):
    area = math.pi * (radius ** 2)
    perimeter = 2 * math.pi * radius
    return area, perimeter

def cube_metrics(side):
    surface_area = 6 * (side ** 2)
    volume = side ** 3
    return surface_area, volume

def cylinder_metrics(radius, height):
    surface_area = (2 * math.pi * radius * height) + (2 * math.pi * (radius ** 2))
    volume = math.pi * (radius ** 2) * height
    return surface_area, volume
