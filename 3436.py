from math import pi
r = float(input())


def area(r):
    area_circulo = pi * (r**2)
    return area_circulo


def perim(r):
    perim_circulo = 2 * pi * r
    return perim_circulo


print('{:.5f}'.format(area(r)))
print('{:.5f}'.format(perim(r)))
