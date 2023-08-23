from ejercicio3 import obtenerCadena

# 4- Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def contador_dic(dic):
    palabra_repetida = ''
    cantidad = 0
    for keys, values in dic.items():
        if values > cantidad:
            cantidad = values
            palabra_repetida = keys
    return palabra_repetida, cantidad

cadena = input('Ingrese una cadena de caracteres: ')

print(obtenerCadena(cadena))
print(contador_dic(obtenerCadena(cadena)))