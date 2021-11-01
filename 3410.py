xa = float(1)
ya = float(1)
xb = float(2)
yb = float(1)
ponto = input()
x, y = ponto.split()
x = float(x)
y = float(y)
distA = ((x - xa)**2 + (y-ya)**2)**0.5
distB = ((x - xb)**2 + (y - yb)**2)**0.5
if distA > 1 and distB > 1:
    print("Exterior")
elif distA <= 1 and distB <= 1:
    print("Interior A,B")
elif distA <= 1 and distB > 1:
    print("Interior A")
elif distA > 1 and distB <= 1:
    print("Interior B")
