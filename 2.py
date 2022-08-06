print("type a value for vector x and y")
vx = int (input())
vy = int (input())
# ** means exponential
vr = vx**2 + vy**2
print("raiz de: ",vr)
square_root = vr**(1/2)
print(square_root)


print('Vetor: [',vx,']/', square_root)
print('       [',vy,']/', square_root)
print('vetor unitario/normalizado ->   x:', vx/square_root, '---' , 'y:', vy/square_root)