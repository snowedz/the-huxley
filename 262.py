qnt = int(input())
b = []
cima = 0
baixo = 0
for a in range(qnt):
    nota = float(input())
    b.append(nota)
f = sum(b)
media = f / qnt
for c in range(qnt):
    if b[c] >= (media*1.10):
        cima += 1
    if b[c] <= (media*0.9):
        baixo += 1
print('{:.2f}'.format(media))
print(cima)
print(baixo)
