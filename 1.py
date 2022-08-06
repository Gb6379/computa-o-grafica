print("type a value for vector x and y")
vx = int (input())
vy = int (input())
vz = int (input())
# ** means exponential
vr = vx**2 + vy**2 + vz**2
print('tamanho do vetor: ')
print('[',vx,']')
print('[',vy,']')
print('[',vz,']')
print('é raiz de', vr)
size = vr**(1/2)
print(size)