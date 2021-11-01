numeros = input()
R, H = numeros.split()
R = float(R)
H = float(H)
Pi = 3.1415
Volume = Pi * R**R * H
print('{:.2f}'.format(Volume))
