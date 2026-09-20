
#Largo de una cadena de palabras sin map

text = "Ejercicio para conocer el largo de una cadena"
palabras = text.split()

def len_cadena(cadena):
    return len(cadena)

longitud = [len_cadena(p) for p in palabras]
print('La longitud del texto sin map es: ',longitud)


#Se agrega funcion para calculo de raiz cuadrada con lambda
#Raíz cuadrada de un número con función lambda.
#Raíz cuadrada de un número sin lambda

num=36
def raiz_cuadrada(a):
    return a ** 0.5

print('La raíz cuadrada de un número sin lambda es: ', raiz_cuadrada(num)) 
raiz_cuad = lambda x: x ** 0.5
print('La raíz cuadrada con lambda es: ', raiz_cuad(num))


#Calcular el producto de una lista sin reduce
numeros = [1, 2, 3, 4, 5]

producto = 1

for n in numeros:
    producto = producto * n

print("Producto de una lista de números sin reduce:", producto)

#Se agrega función reduce para producto de una lista
#Función reduce, que sirva para calcular el producto de una lista 
from functools import reduce

numeros = [1, 2, 3, 4, 5]

producto = reduce(lambda x, y: x * y, numeros)

print("Producto de una lista de números con reduce:", producto)


   
#Encontrar palabras que contengan mayúsculas o números en un listado sin filter
palabras = ["python", "50Mesa", "sillA", "ABCD", "", "1234"]

resultado = []

for palabra in palabras:
    for x in palabra:
        if x.isupper() or x.isdigit():
            resultado.append(palabra)
            break

print("Palabras con mayúsculas o números sin filter:", resultado)

