#backward euler iterado y con funciones definidas

import numpy as np
import os

steps = 5
v = np.zeros(steps + 1)
x = np.zeros(steps + 1)
x[0] = -1
v[0] = -2
dt = 0.1

# definir funcion diferencial de x
# x' = f(v) = v
def difx(v):
  x1 = v
  return x1

#definir funcion diferencial de v 
# v' = f(x,v)= g - (b/m)*v - (k/m)*x
g, b, m, k = 0, 0, 0.5, 2
def difv(c, d):
  v1 = g - (b/m)*d - (k/m)*c
  return v1
#v1 = difv(x,v)

# un ciclo grande del backward euler, y uno pequeño de forward euler, porque es una función compleja
for i in range(steps):
  # Se realiza el forward euler
  fx = x[i] + dt*difx(v[i])
  fv = v[i] + dt*difv(x[i], v[i])
  # Se realiza el backward euler
  x[i+1] = x[i] + dt*difx(fv)
  v[i+1] = v[i] + dt*difv(fx, fv)

print(x[i+1], v[i+1], f"con {steps} iteraciones")
#-1.2450968576 0.6135605248000002 con 5 iteraciones
