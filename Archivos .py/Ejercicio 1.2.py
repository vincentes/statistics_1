#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Ejercicio 1.2

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from numpy import random

# Muestra de tamaño N de una X ~ Geo(p=0.5)

N=1000
p=0.5
muestra = list(random.geometric(p, size=N))

# Promedio en función de N

avg = []
for i in range(1,len(muestra)+1):
    primeros_i = muestra[:i]
    suma = sum(primeros_i)
    largo = len(primeros_i)
    promedio_i = suma/largo
    avg.append(promedio_i)


# In[4]:


# Gráfica promedio en función de N

line = [2 for _ in range(0,1000)]
plt.plot(line,linestyle='solid')
plt.plot(avg)
plt.show()


# Verifica la ley de los grandes números porque tiende a p=2 


# In[ ]:




