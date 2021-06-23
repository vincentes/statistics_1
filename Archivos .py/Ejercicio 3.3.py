import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import binom
from numpy import random

n = 100 # Cantidad de veces que se lanza una moneda equilibrada.
p = 0.5 # Probabilidad de que salga cara al lanzar una moneda (éxito)

# P(40 <= z <= 50)
p = binom.cdf(50, n, p) - binom.cdf(40, n, p)
print (f"La probabilidad de que la cantidad de caras esté entre 40 y 50 de forma exacta es : {p}" )

# P(40 <= z <= 50) utilizando la aproximación a una Distribución Normal.
pn = norm.cdf(0) - norm.cdf(-2)
print (f"La probabilidad de que la cantidad de caras esté entre 40 y 50 utilizando la aproximación a una Normal es: {pn}")

print (f"La diferencia fue de: {abs(p - pn)}")