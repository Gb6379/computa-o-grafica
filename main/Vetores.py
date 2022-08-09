

import sys
import os
 
# adding Folder_2 to the system path #in case it gets pulled to another computer, pls map the path where the project is
sys.path.insert(0, '/home/amaru/Documents/UFN/computacaoGrafica/functions') #ubuntu path
##sys.path.insert(0,'d:/ComputacaoGrafica/functions') ##windows path
 
# importing the add and odd_even
# function
from module1 import vectorMag, normalize , addVet, subVet, multVet, divVet, productEsc

while 1 > 0:  
    print("Escolha uma operação")
    print("(1)Magnitude - (2)Normalizar - (3)Adição - (4)Subtração - (5)Multiplicação - (6)Divisão - (7) Produto Escalar")  
    print("Escolha uma operação")
    op = int (input())
    # calling  function
    if(op == 1):
        vectorMag()
    elif op == 2:
        normalize()
    elif op == 3:
        addVet()
    elif op == 4:
        subVet()
    elif op == 5:
        multVet()
    elif op == 6:
        divVet()
    else:
        productEsc()

    



