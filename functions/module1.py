import random

def vectorMag():
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


def normalize():
    vector = []
    vrf = 0
    for i in range(3):
        vector.append(random.randint(0,20))
        
    print("valores x,y,z do vetor")
    print(vector)
    
    for j in range(3):
        vrf = vrf + vector[j]**2

    print("raiz de: ",vrf)
    square_root = vrf**(1/2)
    print(square_root)

    print('Vetor: [',vector[0],']/', square_root)
    print('       [',vector[1],']/', square_root)
    print('       [',vector[2],']/', square_root)
    print('vetor unitario/normalizado ->   x:', vector[0]/square_root, '---' , 'y:', vector[1]/square_root, '---' ,'z:', vector[2]/square_root)
        

def addVet(): 
    vectorA = []
    vectorB = []
    vrf = []
    for i in range(3):
        vectorA.append(random.randint(0,20))
        
    print("valores x,y,z do vetor A")
    print(vectorA)

    for k in range(3):
        vectorB.append(random.randint(0,20))
        
    print("valores x,y,z do vetor B")
    print(vectorB)
    
    for j in range(3):
        vrf.append(vectorB[j] + vectorA[j])

    print('Soma dos vetores:', vrf[0],vrf[1],vrf[2])


def subVet():
    vectorA = []
    vectorB = []
    vrf = []
    for i in range(3):
        vectorA.append(random.randint(0,20))
        
    print("valores x,y,z do vetor A")
    print(vectorA)

    for k in range(3):
        vectorB.append(random.randint(0,20))
        
    print("valores x,y,z do vetor B")
    print(vectorB)
    
    for j in range(3):
        vrf.append(vectorB[j] - vectorA[j])

    print('Subtração dos vetores:', vrf[0],vrf[1],vrf[2])



def multVet():
    vectorA = []
    x = random.randint(0,20)
    vrf = []
    for i in range(3):
        vectorA.append(random.randint(0,20))
        
    print("valores x,y,z do vetor A")
    print(vectorA)
    print("Escalar = ", x)
    for j in range(3):
        vrf.append(vectorA[j] * x)

    print('Resultado da operação dos vetores:', vrf[0],vrf[1],vrf[2])

def divVet():
    vectorA = []
    x = random.randint(0,20)
    vrf = []
    for i in range(3):
        vectorA.append(random.randint(0,20))
        
    print("valores x,y,z do vetor A")
    print(vectorA)
    print("Escalar = ", x)
    
    for j in range(3):
        vrf.append(vectorA[j] / x)

    print('Resultado da operação dos vetores:', vrf[0],vrf[1],vrf[2])



def productEsc():
    vectorA = []
    vectorB = []
    vrf = []
    result = 0
    for i in range(3):
        vectorA.append(random.randint(0,20))
        
    print("valores x,y,z do vetor A")
    print(vectorA)

    for k in range(3):
        vectorB.append(random.randint(0,20))
        
    print("valores x,y,z do vetor B")
    print(vectorB)
    
    for j in range(3):
        vrf.append(vectorB[j] * vectorA[j])
    result = vrf[0] + vrf[1] + vrf[2]
    print('Soma dos vetores multiplicados:', vrf[0], '+' ,vrf[1], '+' ,vrf[2], '=' , result)