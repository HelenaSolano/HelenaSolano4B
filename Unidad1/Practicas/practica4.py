#Practica 4 Herencia

class Ticket:
    def __init__ (self, id, prioridad, tipo):
        self.id = id
        self.prioridad = prioridad
        self.tipo = tipo
        self.estado = "Pendiente" #valor por defecto
    
    def identificar(self):
        print("...::TICKET::...")
        print(f"ID: {self.id}")
        print(f"Prioridad: {self.prioridad}")
        print(f"Tipo: {self.tipo}")
        print(f"Estado: {self.estado}")
        print("--------------------")


class Empleado:
    def __init__ (self, nombre ):
        self.nombre = nombre

    def trabajar_ticket(self, ticket):
        print(f"El empleado {self.nombre} esta trabajando en ticket {ticket.id}")


class Desarrollador(Empleado):
    def resolver_ticket(self, ticket):
        if ticket.tipo =="Software":
            ticket.estado =="Resuelto"
            print(f"El ticket {ticket.id} fue resuelto por {self.nombre}")
        else:
            print(f"El desarrollador {self.nombre} no puede resolver este tipo de ticket{ticket.tipo}")



class Tester(Empleado):
        def resolver_ticket(self, ticket):
            if ticket.tipo =="Prueba":
                ticket.estado =="Resuelto"
                print(f"El ticket {ticket.id} fue resuelto por {self.nombre}")
            else:
                print(f"El desarrollador {self.nombre} no puede resolver este tipo de ticket{ticket.tipo}")

class Proyect_Manager(Empleado):
    def asignar_ticket(self, ticket, empleado):
        print (f"{self.nombre} asigno el ticket {ticket.id}, a el empleado {empleado.nombre}")
        empleado.trabajar_ticket(ticket)

#Crea tickets y empleados (Instancias de objetos)
ticket1 = Ticket (1, "alta", "software")
ticket2 = Ticket (2, "media", "prueba")


developer1 = Desarrollador ("Gustavo")
tester1 = Desarrollador ("Pablo")
pm1 = Proyect_Manager ("Susana")

pm1.asignar_ticket(ticket1, developer1)
developer1.resolver_ticket(ticket1)

pm1.asignar_ticket(ticket2, tester1)
tester1.resolver_ticket(ticket2)

ticket1.identificar()
ticket2.identificar()

# Parte adicional
# Agregar un menú con while y con if que permita:
#1. Crear un ticket
#2. Ver tickets
#3. Asignar tickets
#4. Salir del programa

tickets = [ticket1, ticket2]

n="si"
while n == "si":
    print("\n--- MENU ---")
    print("1. Crear ticket")
    print("2. Ver tickets")
    print("3. Asignar ticket")
    print("4. Salir")
    opcion = input("Elige una opción:")

    if opcion == "1":
        id_ticket = len(tickets) + 1
        tipo = input("Ingrese el tipo de ticket (software/prueba): ").lower()
        prioridad = input("Ingrese la prioridad (alta/media/baja): ").lower()
        nuevo_ticket = Ticket(id_ticket, tipo, prioridad)
        tickets.append(nuevo_ticket)
        print(f"Ticket {id_ticket} creado exitosamente.")

    elif opcion == "2":
        if tickets == 0:
            print("No hay tickets creados.")
        else:
            for t in tickets:
                t.identificar()

    elif opcion == "3":
        if tickets == 0:
            print("No hay tickets para asignar.")
        else:
            for t in tickets:
                print(f"ID: {t.id} - Tipo: {t.tipo} - Estado: {t.estado}")

            try:
                id_asignar = int(input("Ingrese el ID del ticket a asignar: "))
                ticket = next((t for t in tickets if t.id == id_asignar), None)
                if ticket:
                    if ticket.tipo == "software":
                        pm1.asignar_ticket(ticket, developer1)
                        developer1.resolver_ticket(ticket)
                    elif ticket.tipo == "prueba":
                        pm1.asignar_ticket(ticket, tester1)
                        tester1.resolver_ticket(ticket)
                    else:
                        print("Este tipo de ticket no puede ser asignado.")
                else:
                    print("No existe un ticket con ese ID.")
            except ValueError:
                print("Debe ingresar un numero valido.")

    elif opcion == "4":
        print("Saliendo del programa...")
        n="no"

    else:
        print("Opcion no valida. Intente de nuevo.")


