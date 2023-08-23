from ejercicio1 import maximo_comun_divisor

# 2- Escribir una función que calcule el mínimo común múltiplo entre dos números

def minimo_comun_multiplo(a, b):
    return (a * b) / maximo_comun_divisor(a, b)


a = int(input("Escribe un número entero: "))
b = int(input("Escribe otro número entero: "))
mcm = minimo_comun_multiplo(a, b)
print(f"El mínimo común múltiplo de {a} y {b} es {mcm}")