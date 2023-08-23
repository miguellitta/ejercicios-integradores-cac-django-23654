from ejercicio6 import Persona

#Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Crear los siguientes métodos para la clase: Un constructor, donde los datos pueden estar vacíos. Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero. mostrar(): Muestra los datos de la cuenta. ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada. retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.


class Cuenta(Persona):
    def __init__(self, titular, edad, dni, cantidad = 0) -> None:
        super().__init__(titular, edad, dni)
        self._titular = titular
        self._cantidad = cantidad

    @property
    def titular(self):
        return self._titular
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @titular.setter
    def titular(self,titular):
        self._titular = titular


    def mostrar(self):
        return print(f'Cuenta \nTitular: {self._titular} - Cantidad: {str(self._cantidad)}')

    def ingresar(self,cantidad):
        if cantidad > 0:
            self._cantidad += cantidad
            print(f'Se ha ingresado dinero. El saldo actual es {self._cantidad}')

    def retirar(self,cantidad):
        if cantidad > 0:
            self._cantidad -= cantidad
            print(f'Se ha retirado dinero. El saldo actual es {self._cantidad}')



cuenta1 = Cuenta("miguel", 25, 40000200, 4000)
cuenta1.mostrar()