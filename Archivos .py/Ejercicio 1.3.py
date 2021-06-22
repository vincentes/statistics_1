#!/usr/bin/env python
# coding: utf-8

# In[28]:


#Ejercicio 1.3

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from numpy import random
import math 

muestra = [6,19,1,4,3,6,9,9,3,9,34,7,28,2,5,1,15,11,9,3,11,41,14,10,4,2,4,8,3,1,12,4,3,
           2,15,1,3,1,16,19,12,29,8,9,1,7,9,7,2,8,2,11,2,7,5,8,13,13,6,6,2,5,2,11,3,2,
           6,17,3,23,7,12,11,7,23,36,18,21,5,3,14,15,2,3,5,2,15,9,4,3,4,1,8,5,1,2,1,11,
           5,8]

# Probabilidad de obtener un 6

    # x = "cantidad de tiradas hasta obtener un 6"
    # p = "probabilidad de obtener un 6"
    # n = "tamaño de la muestra"

for i in range(0,len(muestra)):
    primeros_i = muestra[:i]
    suma = sum(primeros_i)
    
p = 100/suma #Explicación en imagen adjunta

#Verificamos
   
    # Promedio en función de N

avg = []
for i in range(1,len(muestra)+1):
    primeros_i = muestra[:i]
    suma = sum(primeros_i)
    largo = len(primeros_i)
    promedio_i = suma/largo
    avg.append(promedio_i)

    # Gráfica promedio en función de N

line = [(1/p) for _ in range(0,100)]
plt.plot(line,linestyle='solid')
plt.plot(avg)
plt.show()


# In[ ]:





# In[ ]:




