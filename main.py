def main():
    # Aquí pones el código principal que quieres que se ejecute
    print("¡Hola! Este es el punto de inicio de mi programa.")

# ---- BUCLES ----
# Bucle for - Bloque de código a repetir instrucciones
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(fruta)

# Bucle while - Bloque de código a repetir instrucciones
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Bucle while con break
contador = 0
while True:
    print(contador)
    contador += 1
    if contador == 5:
        break


# Ejemplos de función range
for i in range(5):
    print(i)
# Resultado: 0, 1, 2, 3, 4

for i in range(2, 6):
    print(i)
# Resultado: 2, 3, 4, 5

for i in range(1, 10, 2):
    print(i)
# Resultado: 1, 3, 5, 7, 9 (solo números impares)

for i in range(5, 0, -1):
    print(i)
# Resultado: 5, 4, 3, 2, 1

# Bucle for y continue
for i in range(10):

    if i % 2 == 0:
        continue
    print(i)

# Bucle for y pass (cuando se está desarrollando un programa y se desea reservar un bloque de código para implementarlo más adelante)
for i in range(5):
    pass

# ---- LISTAS ----
#Para acceder a los elementos de una lista, utiliza el índice del elemento entre corchetes. 
# Los índices comienzan desde 0.
frutas = ["manzana", "banana", "naranja"]
print(frutas[0])  # Imprime "manzana"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "naranja"

#También puedes acceder a los elementos desde el final de la lista utilizando índices negativos. 
# El índice -1 representa el último elemento, -2 representa el penúltimo, y así sucesivamente.

print(frutas[-1])  # Imprime "naranja"
print(frutas[-2])  # Imprime "banana"
print(frutas[-3])  # Imprime "manzana"


# ---- METODOS DE LISTAS ----
frutas = ["manzana", "banana", "naranja"]  

# Agregar elementos a una lista con append()    
frutas.append("pera")
print(frutas)  # Imprime ["manzana", "banana", "naranja", "pera"]

# Insertar elementos a una lista con insert()
frutas.insert(1, "uva")
print(frutas)  # Imprime ["manzana", "uva", "banana", "naranja", "pera"]

# Eliminar elementos de una lista con remove()
frutas.remove("banana")
print(frutas)  # Imprime ["manzana", "uva", "naranja", "pera"]

# Eliminar elementos de una lista con pop() y obtener el elemento eliminado
fruta_eliminada = frutas.pop(2)
print(frutas)  # Imprime ["manzana", "uva", "pera"]
print(fruta_eliminada)  # Imprime "naranja"

# Ordenar una lista con sort()
frutas.sort()
print(frutas)  # Imprime ["manzana", "pera", "uva"]

# Invertir el orden de una lista con reverse()
frutas.reverse()
print(frutas)  # Imprime ["uva", "pera", "manzana"]

# ---- LISTAS DE COMPRENSION ----
# Crear una lista de cuadrados utilizando una lista de comprensión              
numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]

# ---- TUPLAS ----
# Las tuplas son similares a las listas, pero son inmutables, lo que significa que no se pueden modificar después de su creación.
# Para crear una tupla, puedes usar paréntesis () o simplemente separar los elementos con comas.

punto = (3, 4)

print(punto[0])  # Imprime 3
print(punto[1])  # Imprime 4

# ---- MÉTODOS DE TUPLAS ----
#index() - El método index es como decirle a Python: "Oye, búscame este valor y dime en qué caja (índice) lo has encontrado primero".
mi_tupla = (1, 2, 3, 2, 4, 2)

# Busca el primer número 2 en toda la tupla
print ("El 2 está en el indice", mi_tupla.index(2))   # Salida: 1 (1 es el índice)

# Busca el primer número 2, pero empieza a buscar desde el índice 2 en adelante
print ("El 2 está en el indice", mi_tupla.index(2, 2))   #Salida: 3

# Busca el número 2, empezando en el índice 2 y terminando justo antes del índice 4
print ("El 2 está en el indice", mi_tupla.index(2, 2, 4))   #Salida: 3

#count() - El método count es como decirle a Python: "Oye, cuéntame cuántas veces aparece este valor en la tupla".
notas = (7, 8, 5, 9, 5, 6, 5, 10)
repes_del_cinco = notas.count(5)
print ("El 5 aparece", repes_del_cinco, "veces en la tupla")  # Salida: 3

#len() - El método len es como decirle a Python: "Oye, ¿cuántos elementos hay en esta tupla?".
mochila = ("poción", "espada", "poción", "escudo", "poción", "flecha")
objetos_totales = len(mochila)
print ("La mochila tiene", objetos_totales, "objetos")  # Salida: 6

# ---- DICCIONARIOS ----
# Un diccionario es una colección de pares clave-valor. Cada clave es única y se utiliza para acceder a su valor correspondiente. Los diccionarios se crean utilizando llaves {} y los pares clave-valor se separan por dos puntos :.
persona = {"nombre": "Alex", "edad": 30, "ciudad": "Santander"}
print(persona["nombre"])  # Imprime "Alex"
print(persona["edad"])    # Imprime 30
print(persona["ciudad"])  # Imprime "Santander"

# ---- Métodos de diccionarios ---- 

# keys(): devuelve una vista de todas las claves del diccionario.
print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])

# values(): devuelve una vista de todos los valores del diccionario.
print(persona.values())  # Imprime dict_values(["Alex", 30, "Santander"])

# items(): devuelve una vista de todos los pares clave-valor del diccionario.
print(persona.items())   # Imprime dict_items([("nombre", "Alex"), ("edad", 30), ("ciudad", "Santander")])

# update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario.
persona.update({"profesion": "Programadora"})
print(persona)  # Imprime {"nombre": "Alex", "edad": 30, "ciudad": "Santander", "profesion": "Programadora"}

#get(clave, valor_predeterminado): devuelve el valor asociado a la clave, o un valor predeterminado si la clave no existe.
print(persona.get("nombre", "Desconocido"))  # Imprime "Alex"
print(persona.get("hobby", "Desconocido"))   # Imprime "Desconocido"

# pop(clave): elimina la clave y devuelve su valor asociado.
profesion = persona.pop("profesion")    
print(profesion)  # Imprime "Programadora"
print(persona)    # Imprime {"nombre": "Alex", "edad": 30, "ciudad": "Santander"}

# clear(): elimina todos los pares clave-valor del diccionario.
persona.clear()         
print(persona)    # Imprime {}      


# ---- CONJUNTOS (SET) ----
# Un conjunto es una colección de elementos únicos y no ordenados. 
# Los conjuntos se crean utilizando llaves {} o la función set(). 

frutas = {"manzana", "banana", "naranja"}
numeros = set([1, 2, 3, 4, 5])

# ---- Operaciones básicas conjuntos ---- 
# Los conjuntos admiten operaciones matemáticas de conjuntos,
#  como la unión (|), la intersección (&), la diferencia (-) 
# y la diferencia simétrica (^).

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}


union = conjunto1 | conjunto2
print(union)  # Imprime {1, 2, 3, 4, 5}


interseccion = conjunto1 & conjunto2
print(interseccion)  # Imprime {3}


diferencia = conjunto1 - conjunto2
print(diferencia)  # Imprime {1, 2}


diferencia_simetrica = conjunto1 ^ conjunto2
print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}

# ---- Métodos de conjuntos ----
frutas = {"manzana", "banana", "naranja"}

# add(elemento): agrega un elemento al conjunto.
frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}

# remove(elemento): elimina un elemento del conjunto. Si el elemento no existe, genera un error.
frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

#discard(elemento): elimina un elemento del conjunto si está presente. Si el elemento no existe, no hace nada.
frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}

#clear(): elimina todos los elementos del conjunto.
frutas.clear()
print(frutas)  # Imprime set()

# ---- FUNCIONES ----
# Una función es un bloque de código reutilizable que realiza una tarea específica.
# Opcionalmente, podemos especificar parámetros dentro de los paréntesis. 
# El bloque de código de la función se indenta después de los dos puntos.
def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("Alex"))  # Imprime "Hola, Alex!"


# Para llamar a una función, simplemente escribimos el nombre de la función seguido de paréntesis:
def saludo():
    print("¡Hola, mundo!")

saludo()  # Imprime "¡Hola, mundo!"

# También podemos definir funciones con parámetros para hacerlas más flexibles:
def saludo(nombre):
    print(f"¡Hola, {nombre}!")

saludo("Juan")  # Imprime "¡Hola, Juan!"
saludo("María")  # Imprime "¡Hola, María!"

# ---- Valores de retorno ----
# Las funciones pueden devolver un valor utilizando la palabra clave return.
def suma(a, b):
    return a + b

resultado = suma(3, 4)
print(resultado)  # Imprime 7

# ---- Funciones anónimas (lambda) ----
# Las funciones lambda son funciones pequeñas y anónimas que se definen utilizando la palabra clave lambda.
# Se utilizan principalmente para operaciones simples y se pueden asignar a variables o pasar como argumentos a otras funciones.
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Imprime 25


# ---- Alcance de las variables (local vs. global) ----


def funcion():
    variable_local = 10
    print(variable_local)  # Accesible dentro de la función


variable_global = 20


def funcion2():
    print(variable_global)  # Accesible desde cualquier lugar


funcion()  # Imprime 10
funcion2()  # Imprime 20
print(variable_global)  # Imprime 20
#print(variable_local)  # Genera un error, la variable no está definida en este alcance.


# ---- Documentación de funciones (docstrings) ---- 

def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.


    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.


    Returns:
        float: El área del rectángulo.
    """
    return base * altura

# ---- Funciones con número variable de argumentos ----
# Esto se logra utilizando el operador * antes del nombre del parámetro.
def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

# Ahora llamamos a la función con cualquier cantidad de argumentos:
print(suma_variable(1, 2, 3))  # Imprime 6
print(suma_variable(4, 5, 6, 7))  # Imprime 22


# Manejo de excepciones

# El bloque try contiene el código que puede generar una excepción. 
# Si ocurre una excepción dentro del try, el flujo de ejecución pasa al bloque except correspondiente.

try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")

# El bloque except especifica el tipo de excepción que se desea capturar y manejar. 
# Puedes tener múltiples bloques except para manejar diferentes tipos de excepciones.
try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")

# El bloque finally se ejecuta siempre, independientemente de si se ha producido una excepción o no.
"""try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción"""

# Excepciones personalizadas
# Para crear una excepción personalizada, 
# debes crear una clase que herede de la clase base Exception o de una de sus subclases.
"""def funcion():
    # Código que puede generar una excepción personalizada
    if condicion:
        raise Exception("Descripción del error")

try:
    funcion()
except Exception as e:
    print(f"Error: {str(e)}")"""

"""En este ejemplo, se define una función llamada funcion(). 
Dentro de la función, se verifica una condición y, si se cumple, 
se genera una excepción utilizando la declaración raise. 
En lugar de crear una clase personalizada, se utiliza directamente
la clase base Exception para generar la excepción."""


def retirar_dinero(cantidad_a_sacar, saldo_disponible):
    # CONDICIÓN: Si me piden más dinero del que hay...
    if cantidad_a_sacar > saldo_disponible:
        # Lanzamos la excepción con un mensaje personalizado
        raise Exception("Saldo insuficiente. No puedes sacar tanto dinero.")
    
    # Si la condición NO se cumple, el programa sigue de forma segura
    saldo_restante = saldo_disponible - cantidad_a_sacar
    return saldo_restante

# --- SIMULACIÓN DEL CAJERO ---
mi_saldo = 50  # Solo tengo 50€ en la cuenta
intento_sacar = 120  # Intento sacar 120€ (Esto va a activar la alarma)

try:
    # Intentamos ejecutar la función
    mi_saldo = retirar_dinero(intento_sacar, mi_saldo)
    print(f"¡Éxito! Operación realizada. Tu nuevo saldo es: {mi_saldo}€")

except Exception as e:
    # Si la función "retirar_dinero" lanza el error, saltamos directamente aquí
    print(f"Error del Cajero: {str(e)}")

# ---- Entradas/salidas ----
# --- Entrada de datos ----
"""Para obtener entrada del usuario, puedes utilizar la función input().
La función input() siempre devuelve una cadena de texto."""

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")

print("Hola, " + nombre + "!")
print("Tienes " + edad + " años.")


"""Si deseas trabajar con otros tipos de datos, como números enteros o float, 
debes realizar una conversión explícita utilizando funciones como int() o float()."""
   
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# --- Salida de datos ----
# Para mostrar información al usuario, puedes utilizar la función print().

nombre = "Alex"
edad = 30

print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")

# ---- Lectura y escritura de archivos ----

# LECTURA DE ARCHIVOS
"""Para leer el contenido de un archivo, primero debemos abrirlo utilizando la función open() en modo de lectura ("r"). 
Luego, podemos leer el contenido del archivo utilizando métodos como read() o readlines().
archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()"""

# ESCRITURA DE ARCHIVOS
""" Para escribir datos en un archivo, lo abrimos en modo de escritura ("w") utilizando la función open(). 
Si el archivo no existe, se creará automáticamente. 
Si el archivo ya existe, su contenido se sobrescribirá. """
archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

"""También puedes utilizar la declaración with para manejar la apertura y 
cierre de archivos de manera automática.

with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

En este caso, el archivo se abre utilizando la declaración with y se cierra automáticamente 
una vez que se sale del bloque with, incluso si ocurre una excepción."""


# Importación y creación de módulos
# Para utilizar un módulo en nuestro programa, 
# debemos importarlo utilizando la declaración import. 
# Podemos importar un módulo completo o funciones específicas de un módulo.

import math

resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

""" En este ejemplo, se importa el módulo math utilizando la declaración import. 
Luego, se utiliza la función sqrt() del módulo math para calcular la raíz cuadrada de 25. """
"""También podemos importar funciones específicas de un módulo utilizando la sintaxis from módulo import función."""

from math import sqrt

resultado = sqrt(25)
print(resultado)  # Imprime 5.0

""" En este caso, se importa solo la función sqrt() del módulo math, 
lo que nos permite utilizarla directamente sin tener que precederla con el nombre del módulo."""

# ---- Funciones y clases de módulos estándar de Python---- 

import random
import datetime


numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10


fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual

# ---- Creación de módulos propios ----
""" Para crear un módulo personalizado, simplemente creamos un nuevo archivo Python 
con el nombre deseado y definimos las funciones, clases y variables que queremos incluir en el módulo. 
Por ejemplo, creamos un archivo (en el mismo directorio donde estamos ejecutando Python) llamado mi_modulo.py con el siguiente contenido:

#mi_modulo.py
def saludar(nombre):
    print(f"Hola, {nombre}!")

def calcular_suma(a, b):
    return a + b
    
Luego, podemos importar y utilizar las funciones definidas en mi_modulo.py en otro archivo Python."""
import mi_modulo

mi_modulo.saludar("Alex")  # Imprime "Hola, Alex!"
resultado = mi_modulo.calcular_suma(5, 3)
print(resultado)  # Imprime 8

""" En este ejemplo, se importa el módulo mi_modulo y se utilizan las funciones saludar() y calcular_suma() definidas en él."""

# ---- Organización del código en módulos ----

"""Es una buena práctica organizar nuestro código en módulos separados según su funcionalidad. 
Esto nos permite conservar un código más legible, agrupado en módulos y fácil de mantener.

Por ejemplo, podemos tener un módulo operaciones.py que contenga funciones relacionadas con operaciones matemáticas, 
y otro módulo utilidades.py que contenga funciones de uso general.

# operaciones.py
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

# utilidades.py
def imprimir_mensaje(mensaje):
    print(mensaje)

def obtener_nombre_usuario():
    return input("Ingresa tu nombre: ")"""

# Luego, podemos importar y utilizar estas funciones en nuestro programa principal:

import operaciones
import utilidades

resultado = operaciones.sumar(5, 3)
utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")


nombre = utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(f"Hola, {nombre}!")

# ---- Paquetes ----
"""Un paquete es una forma de organizar módulos relacionados en un directorio. 
Para crear un paquete, creamos un directorio con el nombre deseado y agregamos un archivo especial llamado __init__.py dentro del directorio. 
Este archivo puede estar vacío o contener código de inicialización del paquete.

Por ejemplo, creamos un directorio llamado mi_paquete con la siguiente estructura:

mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py
Luego, podemos importar y utilizar los módulos del paquete en nuestro programa.

from mi_paquete import modulo1, modulo2


modulo1.funcion1()
modulo2.funcion2()
En este ejemplo, se importan los módulos modulo1 y modulo2 del paquete mi_paquete y se utilizan las funciones definidas en ellos.
"""
