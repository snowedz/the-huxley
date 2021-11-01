raios = input()
Ri, Re = raios.split()
Ri = float(Ri)
Re = float(Re)
Pi = 3.14159
Area = ((Pi * Re**2) - (Pi * Ri**2))
print('{:.2f}'.format(Area))
