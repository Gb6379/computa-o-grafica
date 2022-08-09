
import sys
import os
import random


sys.path.insert(0,'d:/ComputacaoGrafica/functions') ##windows path

rsize = 3
csize = 3
x = []
y = []


for j in range(csize):
    y.append(0)#populate matrix
for i in range(rsize):
    x.append(y)

m = 0   
#printar matrix
for k in range(len(x)):
    x.append(random.randint(0,20))
    m = m + x[j] +3
print(m)