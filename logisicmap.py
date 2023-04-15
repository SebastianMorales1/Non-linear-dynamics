#Código de mapa logístico
#Link: https://blbadger.github.io/logistic-map.html

# import third-party libraries, libreria de código de terceros
# np es una forma de abreviar "numpy"
import numpy as np 
#Se invoca la libreria numpy para usar "arrays"
#
steps = 500
#supongo que crea vectores vacíos o algo así
y = np.zeros(steps + 1)
x = np.zeros(steps + 1)
# definir constante r
r = 3.4
# definir valores iniciales
y[0] = 0.2
x[0] = 0.200001

# loop over the steps and replace array values with calculations
# se realizan dos iteraciones diferentes, para ver como divergen en el tiempo
# se quiere buscar un comportamiento caótico.
for i in range(steps):
	y[i+1] = r * y[i] * (1 - y[i])
for i in range(steps):
  x[i+1] = r * x[i] * (1 - x[i])

# se imprime los resultados de las variables
print(y[i+1],x[i+1])
