from math import pi
n = int(input())
i = 0
c = []
b = []


def vet(n):
    for i in range(n):
        v = float(input())
        c.append(v)
    return c


def vet1(n):
    vet(n)
    for i in range(n):
        x = c[i] * pi/180
        print('{:.5f}'.format(x))


vet1(n)
