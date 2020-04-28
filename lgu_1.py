# -*- coding: utf-8 -*-
'''
Determinaremos la fuerza gravitatoria entre dos personas
de 100Kg separadas una distancia de 1,0m.
'''

# Definimos la constante de gravitación universal G:

G = 6.67384*10**(-11)

#ahora las variables con sus respectivos valores:

m1=100
m2=100
r=1.0

# Calculamos la fuerza gravitatoria y almacenamos su valor en una
# variable llamada F:

F = G*m1*m2/r**2


# Finalmente imprimimos el valor de la fuerza gravitatoria

print(
    'La fuerza gravitatoria entre las personas es de ', F, 'Newtons'
)
