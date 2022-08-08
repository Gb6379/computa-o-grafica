

import sys
 
# adding Folder_2 to the system path
sys.path.insert(0, '/home/amaru/Documents/UFN/computacaoGrafica/functions')
 
# importing the add and odd_even
# function
from module1 import odd_even, vectorMag
 
print("Escolha uma operação")
op = int (input())
# calling  function
vectorMag()



