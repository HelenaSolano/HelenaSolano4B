#Practica3. Introducción al Polimorfismo
# Simular un sistema de cobro con multiples opciones de pago.

class pago_tarjeta:
    def procesar_pago(self, cantidad):
        return f"Procesando pago de ${cantidad} con tarjeta bancaria"
    
class transferencia:
    def procesar_pago(self, cantidad):
        return f"Procesando pago con transferencia por la cantidad de ${cantidad}"
    
class deposito:
    def procesar_pago(self, cantidad):
        return f"Procesando pago por medio deposito en ventanilla por la cantidad de ${cantidad}"
    
class paypal:
    def procesar_pago(self, cantidad):
        return f"Procesando pago de ${cantidad} por medio de paypal"
    
#Instancia
#metodos_pago = [pago_tarjeta(), transferencia(), deposito(), paypal()]

#for m in metodos_pago:
    #print(m.procesar_pago(500))

#ACTIVIDAD: PROCESAR PAGO CON DIFERENTES CANTIDADES EN CADA UNO DE LAS FORMAS DE PAGO
# EJEMPLO: 100 CON TARJETA, 500 CON TRANSFERENCIA, 2000 CON PAYPAL, 400 CON DEPOSITO

metodo_tarjeta = pago_tarjeta()
metodo_transferencia = transferencia()
metodo_paypal = deposito()
metodo_deposito = deposito()

print(metodo_tarjeta.procesar_pago(100))
print(metodo_paypal.procesar_pago(2000))
print(metodo_transferencia.procesar_pago(500))
print(metodo_deposito.procesar_pago(400))

class correo:
    def notificar(self, nombre):
        return f"{nombre} tienes un nuevo correo"
    
class tiktok:
    def notificar(self, nombre):
        return f"{nombre} tienes una nueva notificación de TikTok"
    
class whatsapp:
    def notificar(self, nombre):
        return f"{nombre} tienes un nuevo mensaje de WhatsApp"
    
class facebook:
    def notificar(self,nombre):
        return f"{nombre} tienes una nueva notificación de Facebook"
    
notificacion = [correo(), tiktok(), whatsapp(), facebook()]

for i in notificacion:
    print(i.notificar("Helena"))