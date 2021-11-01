n = int(input())


def vet(n):
    c = []
    for i in range(n):
        v = float(input())
        c = c + [v]
    c.sort()
    return c[0]


print(vet(n))
