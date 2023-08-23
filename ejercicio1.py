# 1- Escribir una función que calcule el máximo común divisor entre dos números.

def maximo_comun_divisor(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a


a = int(input("Escribe un número entero: "))
b = int(input("Escribe otro número entero: "))
mcd = maximo_comun_divisor(a, b)
print(f"El Máximo común divisor de {a} y {b} es {mcd}.")