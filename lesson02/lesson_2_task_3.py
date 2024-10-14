import math


def square(side):
    area = side * side
    return math.ceil(area)


side = 3.5
area = square(side)
print(f'Площадь квадрата со стороной {side} равна {area}')