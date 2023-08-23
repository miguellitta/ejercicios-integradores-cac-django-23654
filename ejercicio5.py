# 5- Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto. Intente resolver el ejercicio tanto de manera iterativa como recursiva.

def get_int():
    try:
        num_entero = int(input('Ingrese un número entero: '))
        return print(f'El número entero ingresado es {num_entero}')
    except ValueError:
        print('Debe ingresar un número entero, Ingrese un número de nuevo')
        return get_int()


get_int()
    