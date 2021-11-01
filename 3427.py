o = int(input())
a = []
dia = 1
d = []
for i in range(o):
    linha = []
    for i in range(o):
        elemento = int(input())
        linha.append(elemento)
    a.extend(linha)
for c in range(0, len(a), o+1):
    d = a[c]
    dia *= d
    dia = float(dia)
print(dia)
