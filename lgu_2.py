# -*- coding: utf-8 -*-
'''
En este programa veremos algunas operaciones básicas de Python
y funciones, así como el uso de diccionarios,
calculando el peso de un cuerpo en los distintos astros de
nuestro Sistema Solar
'''

# En primer lugar vamos a definir un Título y un Menú:

print('''
Nuestro peso en los distintos astros del Sistema Solar:
Elija la opción:
1. Calcula tu peso en los distintos astros conocidos
2. Crea tu propio astro
'''
)

opcion = int(input('Opción = '))

# Como vemos, nuestro programa tiene dos finalidades; por un lado 
# calcular, a partir de datos preestablecidos (aceleración gravi-
# tatoria), el peso de un cuerpo en distintos astros.
# En segundo lugar, a partir de la Ley de Gravitación Universal,
# podremos definir ingresando nuestros propios argumentos con
# las características de un astro y determinar el peso del cuerpo allí.
# La Elección queda guardada en la variable "opcion" como un entero.

# Definamos la función Peso (que servirá par cualquiera de las
# opciones):

def Peso(masa,g_astro,astro):
    peso = masa*g_astro
    peso = "{0:.2f}".format(peso) #para redondear a 2 decimales
    print('El peso en', astro, ' es ', peso, 'Newtons')

# La función peso nos imprime el peso en cierto astro,
# a partir de tres parámetros: la masa, la aceleración gravitatoria y el 
# nombre del astro.

# Si elegimos la opción 1...

if opcion == 1:

#primero ingresamos la masa como una variable entera:
    masa = int(input('Ingrese la masa del cuerpo en kg: '))
# Construímos una diccionario con los astros del sistema solar y sus
# respectivas aceleraciones gravitatorias en m/s^2
    astros = {
        'Sol': 274,
        'Mercurio': 3.7,
        'Venus': 8.87,
        'Luna': 1.62,
        'Tierra': 9.81,
        'Marte': 3.7,
        'Júpiter': 24.88,
        'Saturno': 10.44,
        'Urano': 8.69,
        'Neptuno': 11.15,
        'Pluton': 0.62,
        'Ceres': 0.27,
        'Sedna':0.27,
        'Titan': 1.352,
        'Europa': 1.315,
        'Ganimedes': 1.236,
        'Calisto': 1.236,
        'Io': 1.796
    } 
    for astro, g_astro in astros.items():
        Peso(masa,float(g_astro),str(astro))

# Segunda opción: calcular la aceleración gravitatoria
# en un astro a partir de su masa y su radio

if opcion == 2:
    #Comenzamos decretando la constante de gravitación
    #universal que llamaremos G:
    G = 6.67384*10**(-11)
    #Definimos la función aceleración gravitatoria a
    #partir de las variables masa (M) y radio (R):
    
    def g_astro(M,R):
        g_astro = G*M/(R*1000)**2
        #Multiplicamos R por 1000 para pasar a metros
        g_astro = "{0:.2f}".format(g_astro) 
        # lo anterior para expresarlo con 2 cifras decimales
        return g_astro
    
    #Ingresamos la masa y el radio del astro:
    M = float(input('Ingrese la masa del astro (en kg): '))
    R = float(input('Ingrese ahora el radio (en km): '))

    #Hallamos la aceleración gravitatoria en dicho astro:
    print('')
    print ('La aceleración gravitatoria en el astro es', g_astro(M,R), 'm/s^2')
