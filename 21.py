inicio = int(input())
fim = int(input())
for a in range(inicio, fim+1, 1):
    if a % 2 != 0:
        print(a)
