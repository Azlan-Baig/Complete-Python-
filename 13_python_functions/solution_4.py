import math

def circle_radi(radius):
    area = math.pi * radius**2
    circum = 2 * math.pi * radius
    return area, circum

area,circ = circle_radi(5)
print("Area is",area, "Circumference is",circ)

    