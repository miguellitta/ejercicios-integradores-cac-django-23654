# 6- Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase: Un constructor, donde los datos pueden estar vacíos.  Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos. mostrar(): Muestra los datos de la persona.  Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona():

# CONSTRUCTOR
    def __init__(self, nombre = '', edad = 0, dni = 0) -> None:
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

# GETTERS Y SETTERS 

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def edad(self):
        return self._edad
    
    @property
    def dni(self):
        return self._dni
    
    @nombre.setter
    def nombre(self, nombre):
        if nombre != '':
            self._nombre = nombre
        else:
            print('El nombre esta vacio. Ingresa un nombre')
    
    @edad.setter
    def edad(self, edad):
        if edad != 0:
            self._edad = edad
        else:
            print('La edad esta vacia. Ingresa una edad')

    @dni.setter
    def dni(self, dni):
        if len(self._dni)!=9:
            print("DNI incorrecto. Ingresa un dni")
            self._dni = 0
        else:
            self._dni = dni

    
    def mostrar(self):
        return print(f'Nombre: {self._nombre} \n Edad: {self._edad} \n DNI: {self._dni}')

    def esMayorDeEdad(self):
        if self._edad >= 18:
            return True
        


persona1 = Persona("miguel", 25, 40000020)
persona1.mostrar()