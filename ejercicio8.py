from ejercicio7 import Cuenta
from ejercicio6 import Persona

#Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar una bonificación que estará expresada en tanto por ciento. Crear los siguientes métodos para la clase: Un constructor. Los setters y getters para el nuevo atributo. En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lotanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es mayor de edad pero menor de 25 años y falso en caso contrario. Además, la retirada de dinero sólo se podrá hacer si el titular es válido. El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.


class CuentaJoven(Cuenta):

    def __init__(self, titular, edad, dni, cantidad = 0, bonificacion = 0) -> None:
        super().__init__(titular, edad, dni, cantidad)
        self.bonificacion = bonificacion

    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self,bonificacion):
        self._bonificacion=bonificacion

    def mostrar(self):
        return print(f'Cuenta Joven \n - Titular: {self._titular} - Cantidad: {str(self._cantidad)} + Bonificación: {str(self._bonificacion)}%')
    
    def esTitularValido(self):
        if super().edad < 25 and super().esMayorDeEdad():
            return True

    
    def retirar(self,cantidad):
        if self.esTitularValido():
            super().retirar(cantidad)
        else:
            print(f'No es un titular valido para retirar ${cantidad} de esta cuenta')





cuentajoven1 = CuentaJoven("miguel", 20, 40000200, 5000, 20)
cuentajoven1.mostrar()
cuentajoven1.retirar(200)