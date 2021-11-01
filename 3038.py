ncasos = int(input())
for x in range(ncasos):
    raios = input()
    a, b = raios.split()
    a = int(a)
    b = int(b)
    print(int((2*a + 2*b)/2))
