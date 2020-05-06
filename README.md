# gravedad
Estudio del peso en los distintos astros

Con este ejemplo usaremos los diccionarios de Python, para analizar el Peso de un cuerpo en los distintos astros del sistema solar.

![github-small](https://fisicapython.files.wordpress.com/2017/09/solar-system-1789557_1920-e1506665131188.jpg)

Al estudiar la ley de Gravitación Universal de Isaac Newton, publicada en 1687, encontramos que la fuerza gravitatoria, entre dos cuerpos cualquiera, es directamente proporcional al producto de sus masas, e inversamente proporcional al cuadrado de la distancia que los separa.

Matemáticamente, lo podemos expresar así:

![github-small](https://fisicapython.files.wordpress.com/2017/09/captura-de-pantalla-2017-09-29-a-las-20-27-39.png)

Siendo F la fuerza gravitatoria, m1 y m2 las masas de los cuerpos que interactúan, r la distancia entre los cuerpos y G una constante de proporcionalidad (denominada constante de gravitación universal).

En el sistema internacional de unidades (SI) G tiene un valor de:

![github-small](https://fisicapython.files.wordpress.com/2017/09/captura-de-pantalla-2017-09-29-a-las-20-27-51.png)

Con esta ley podemos fácilmente calcular la fuerza gravitatoria entre dos cuerpos cualquiera. Por ejemplo, podríamos determinar la fuerza de atracción gravitatoria entre dos personas, que podemos aproximar a dos cuerpos de 100Kg separados una distancia de 1m.

Correr el programa lgu_1.py (ver archivos) y se obtiene una salida así:

> La fuerza gravitatoria entre las personas es de 6.67384e-07 Newtons

---

Se puede observar que esta es una fuerza muy pequeña y es por eso que no la notamos comúnmente. Sin embargo, basta con tropezar con una piedra para ir a parar al piso y experimentar la enorme atracción gravitatoria que la Tierra nos ejerce.

![github-small](https://fisicapython.files.wordpress.com/2017/09/skydiving-678168_1920-e1506730558918.jpg)

En efecto, si consideramos ahora como m la masa de una persona, M la masa de la Tierra y R su radio, la fuerza gravitatoria entre una persona y nuestro planeta, se puede determinar así:

![github-small](https://fisicapython.files.wordpress.com/2017/09/captura-de-pantalla-2017-09-29-a-las-21-06-40.png)

esta última expresión se puede reescribir de una forma muy interesante reordenando un poco:

![github-small](https://fisicapython.files.wordpress.com/2017/09/captura-de-pantalla-2017-09-29-a-las-21-09-39.png)

o también:

![github-small](https://fisicapython.files.wordpress.com/2017/09/captura-de-pantalla-2017-09-29-a-las-21-09-52.png)

siendo g:

![github-small](https://fisicapython.files.wordpress.com/2017/09/captura-de-pantalla-2017-09-29-a-las-21-10-01.png)

Si observamos la segunda ecuación, es precisamente la manera usual de calcular el Peso de un cuerpo…

![github-small](https://fisicapython.files.wordpress.com/2017/09/captura-de-pantalla-2017-09-29-a-las-21-22-03.png)

Así que conociendo la masa de un astro, y su radio, es posible determinar la aceleración gravitatoria en su superficie y por consiguiente el peso de un objeto allí. Eso es precisamente lo que nos proponemos determinar en el siguiente programa, que es un poco más elaborado que el anterior.

Correr el programa lgu_2.py

Al correr el programa y seleccionar la primera opción nos aparece el siguiente diálogo:

![github-small](https://fisicapython.files.wordpress.com/2017/09/captura-de-pantalla-2017-09-29-a-las-23-52-23.png)

Si ingresamos por ejemplo una masa de 10Kg, obtendremos su peso en los distintos astros pre-cargados en nuestro programa:

![github-small](https://fisicapython.files.wordpress.com/2017/09/captura-de-pantalla-2017-09-29-a-las-23-52-55.png)

Calculando la aceleración gravitatoria en la Tierra y en la “Súper Tierra”

Si seleccionamos la segunda opción e ingresamos los datos de la masa y radio terrestre proporcionados por el buscador Google, obtenemos el siguiente resultado:

![github-small](https://fisicapython.files.wordpress.com/2017/09/captura-de-pantalla-2017-09-30-a-las-00-21-02.png)

Como vemos, no está nada mal para ser la aceleración gravitatoria media en todo el planeta.

En el año 2007, se descubrió un exoplaneta que tendría condiciones similares a la Tierra para albergar vida y que se denominó “Gliese 581c“, aunque fue rápidamente bautizado como la “Súper Tierra”.

![github-small](https://fisicapython.files.wordpress.com/2017/09/planet-571901_1920-e1506743477658.jpg)

Este planeta posee una masa 5 veces mayor a la de nuestro planeta y un radio ecuatorial 1,5 veces más grande, de allí su denominación “Súper-Tierra”.

Si utilizamos nuestro programa para determinar la aceleración gravitatoria, obtenemos lo siguiente:

![github-small](https://fisicapython.files.wordpress.com/2017/09/captura-de-pantalla-2017-09-30-a-las-00-44-58.png)

Es decir unas 2,22 veces la aceleración gravitatoria en nuestro planeta. Por supuesto que todos estos datos son aproximados, pero si tuviéramos que catalogar o investigar cientos de cuerpos celestes, este tipo de código podría darnos al menos los mejores candidatos para buscar planetas con condiciones propicias para buscar vida o un nuevo hogar.

¿Qué sugerencias se te ocurren para mejorar el código y agregar más opciones?

