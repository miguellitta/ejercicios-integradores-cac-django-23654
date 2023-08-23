# 3- Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).

def obtenerCadena(cadena):
    listaCadena = cadena.split()
    dic_cadena = {}
    for i in listaCadena:
        if i in dic_cadena:
            dic_cadena[i] += 1
        else:
            dic_cadena[i] = 1
    return dic_cadena
