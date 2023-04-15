#forward euler con iteración y funciones diferenciales definidas.

import numpy as np

# se define numero de iteraciones
steps = 5
# Se ponen los arreglos en estado inicial "cero" SUPONGO
v = np.zeros(steps + 1)
x = np.zeros(steps + 1)
# se definen las variables iniciales de estado
x[0] = -1
v[0] = -2
#definir dt como diferencia de tiempo
dt = 0.1

# definir funcion diferencial de x
# x' = f(v) = v
def difx(a):
  x1 = a
  return x1
#x1 = difx(v)

#definir funcion diferencial de v 
# v' = f(x,v)= g - (b/m)*v - (k/m)*x
g, b, m, k = 0, 0, 0.5, 2
def difv(c, d):
  v1 = g - (b/m)*d - (k/m)*c
  return v1
#v1 = difv(x,v)

#Se empieza la iteración forward
for i in range(steps):
  x[i+1] = x[i] + dt*difx(v[i])
  v[i+1] = v[i] + dt*difv(x[i],v[i])

print(x[i+1], v[i+1], f"con {steps} iteraciones")

#-1.2 -1.6|1 iteracion
#-1.3599999999999999 -1.12|para 2 iteraciones
#-1.5283200000000001 0.6246399999999999 con 5 iteraciones
