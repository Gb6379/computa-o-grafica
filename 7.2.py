import random

print("Escolha uma operação")
op = int (input())

vector = []
vr = []
vr = 0
for i in range(3):
    vector.append(random.randint(0,20))
    
print("valores x,y,z do vetor")
print(vector)


for j in range(3):
    vr = vr + vector[j]**2
    ##print('position', j, 'VR',vr)
    


print('final',vr)
size = vr**(1/2)
print('Magnitude do vetor:',size)
