import random
import numpy as np



    
def addSubMatrix(matriz,matriz2):
    #matriz2 = np.random.randint(10, size=(3,3))
    print("Matriz a ser somada/subtraida:")
    print(matriz2)
    matrizSoma = matriz+matriz2
    matrizSub = matriz-matriz2
    print("Matriz soma:")
    print(matrizSoma)
    print("Matriz subtração:")
    print(matrizSub)

def esc(matriz):
    escalar = random.randint(0, 10)
    print("Escalar: ",escalar)
    matrizRes = matriz*escalar
    print("Matriz multiplicada por escalar:")
    print(matrizRes)

def MatPerVet(matriz):
    vetor = np.random.randint(10, size=(3))
    print("Vetor a ser multiplicado:")
    print(vetor)
    vetorRes = matriz.dot(vetor) #multiplicação da matriz pelo vetor
    print("Matriz multiplicada pelo vetor:")
    print(vetorRes)

def MatPerMat(matriz,matriz2):
        print("Calculo")
        print(matriz)
        print('X')
        print(matriz2)
        matrizRes = matriz.dot(matriz2)
        print("Matriz multiplicada por outra matriz:")
        print(matrizRes)
    
def MatTrans(matriz):
      matrizTransposta = np.transpose(matriz)
      print("Matriz transposta:")
      print(matrizTransposta)
