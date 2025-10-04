#Practica 2. Atributos públicos y privados

class Persona:
    def __init__ (self, nombre, edad): #Constructor de una clase
        self.nombre = nombre
        self.edad = edad
        self.__cuenta = None #Atributo privado 
    
    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años")

    def cumplir_anios(self):
        self.edad +=1 
        print(f"Esta persona cumplió: {self.edad}")

    def asignar_cuenta(self, cuenta):
        self.__cuenta = cuenta
        print(f"{self.nombre} ahora tiene una cuenta bancaria")

    def consultar_saldo(self):
        if self.__cuenta:
            print(f"El saldo de {self.nombre} es ${self.__cuenta.mostrar_saldo()}")
        else:
            print(f"{self.nombre} aún no tiene cuenta bancaria")

class cuenta_bancaria:
    def __init__(self, num_cuenta, saldo):
        self.num_cuenta = num_cuenta
        self.__saldo = saldo #Atributo privado

    def mostrar_saldo(self):
        return self.__saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Se depositó la cantidad de ${cantidad} a la cuenta, nuevo saldo ${self.__saldo}")
        else:
            print("Ingresa una cantidad valida")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Se retiró la cantidad de ${cantidad}, nuevo saldo: ${self.__saldo}")
        elif cantidad > self.__saldo:
            print("La cantidad no es válida, saldo insuficiente")
        else:
            print("Ingresa una cantidad valida")

#Crearun objeto o instancia de la clase
persona1 = Persona("Helena", 19)
cuenta1 = cuenta_bancaria("001", 500)

#Acceder a los valores de los atributos públicos
print(persona1.nombre)
print(f"{persona1.edad} años")
persona1.asignar_cuenta(cuenta1)
persona1.consultar_saldo()

cuenta1.depositar(300)
cuenta1.retirar(200)
