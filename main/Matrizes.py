import numpy as np
import random
import sys

sys.path.insert(0, '/home/amaru/Documents/UFN/computacaoGrafica/functions')

from module2 import addSubMatrix, esc, MatPerVet, MatPerMat, MatTrans
#inicialização de uma matriz "no braço"
'''matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])'''

#inicialização de uma matriz com valors de 0 a 10 de tamanho 3x3 aleatória
m1 = np.random.randint(10, size=(3,3))
m2 = np.random.randint(10, size=(3,3))
print("Matriz inicial:")

while True:
    print("1. Adicionar e subtrair outra matriz")
    print("2. Multiplicar e dividir por escalar")
    print("3. Multiplicar a matriz por um vetor")
    print("4. Multiplicar a matriz por outra matriz")
    print("5. Transposta da matriz")
    op = int (input())
    if op == 1: 
        addSubMatrix(m1,m2)
    elif op == 2:
        esc(m1)
    elif op == 3:
        MatPerVet(m1)
    elif op == 4:
        MatPerMat(m1,m2)
    elif op == 5:
        MatTrans(m1)
    else:
        print("Invalid")