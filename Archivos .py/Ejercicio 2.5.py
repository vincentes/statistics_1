import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from numpy import random

muestra = list(random.choice([1,-1], p=[18/37,19/37], size=20000))
esperanzas = []
for i in range(1, len(muestra) + 1):
    primeros_i = muestra[:i]
    suma = sum(primeros_i)
    esperanzas.append(suma)
    
plt.plot(esperanzas)