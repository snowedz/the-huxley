n = int(input())
vet_a = []


def vet(n):
    global vet_a
    for i in range(n):
        elem = float(input())
        vet_a.append(elem)
    return vet_a


vet(n)
vet_x = vet_a
vet_a = []
vet(n)
vet_y = vet_a


def prod(n):
    global vet_x
    global vet_y
    y = 0
    for i in range(0, n):
        x = vet_x[i] * vet_y[i]
        y = y + x
    return(y)


prod(n)
print(prod(n))
