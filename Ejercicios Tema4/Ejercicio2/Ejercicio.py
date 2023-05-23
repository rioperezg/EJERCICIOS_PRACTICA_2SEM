"""
El comandante de la estrella de la muerte el gran Moff Tarkin debe administrar las asigna- ciones de vehículos y Stromtroopers a las 
distintas misiones que parten desde la estrella de la muerte, para facilitar esta tarea nos encomienda desarrollar las funciones necesarias 
para gestionar esto mediante prioridades de la siguiente manera:
 
de cada misión se conoce su tipo (exploración, contención o ataque), planeta destino y general que la solicitó;
 
si la misión fue pedida por Palpatine o Darth Vader estas tendrán alta prioridad, sino su prioridad será baja;
 
si la misión es de prioridad alta los recursos se asignarán manualmente independiente- mente de su tipo;
 
si la misión es de baja prioridad se asignarán los recursos de la siguiente manera depen- diendo de su tipo:
 
exploración: 15 Scout Troopers y 2 speeder bike,
 
contención: 30 Stormtroopers y tres vehículos aleatorios (AT-AT, AT-RT, AT-TE, AT-DP, AT-ST) pueden ser repetidos,
 
ataque: 50 Stormtroopers y siete vehículos aleatorios (a los anteriores se le suman AT-M6, AT-MP, AT-DT),

realizar la atención de todas las misiones y mostrar los recursos asignados a cada una, per- mitiendo agregar nuevos pedidos de misiones 
durante la atención;
 
indicar la cantidad total de recursos asignados a las misiones.
"""
from Herramientas import Cola, Lista, nodoLista  
# Necesitaremos una funcion que nos devuelva un vehiciulo aleatorio de una lista de vehiculos predefinida
import random

lista_vehiculos = Lista()

def Lista_vehiculos(vehiculos):
    if vehiculos == []:
        print("Ya se han cargado los vehiculos")
        return lista_vehiculos
    else:
        vehiculo = vehiculos[0]
        vehiculos.pop(vehiculo)
        Lista.insertar(lista_vehiculos, vehiculo)
        return Lista_vehiculos(vehiculos)
list_vehic = Lista_vehiculos(["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST"])
list_vehic2 = Lista_vehiculos(["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST", "AT-M6", "AT-MP", "AT-DT"])
class Mision(object):
    def __init__(self):
        self.tipo = input("(Presione enter si quiere salir) Tipo de misión: ")
        self.Planeta = input("(Presione enter si quiere salir) Planeta de destino: ")
        self.general = input("(Presione enter si quiere salir) General que solicita la msiion: ")
    def recursos(self, mision):
        if (mision.prioridad == prioridad_alta):
            print("los recursos se introduciran manualmente")
            self.stormtroopers = int(input("stormtroopers > "))
            self.vehiculos = input("vehiculos > ")
        else: 
            print("los recursos se asignara de forma automatica")
            if (mision.tipo == "exploracion"):
                self.stormtroopers = 15
                self.vehiculos = "2 speeder bikes"
            elif(mision.tipo == "contencion"):
                self.stormtroopers = 30
                # Ahora de forma aleatoria de la lista de vehiculos se eligen 3
                self.vehiculos = random.sample(list_vehic, 3)
            elif(mision.tipo == "ataque"):
                self.stormtroopers = 50
                self.vehiculos = random.sample(list_vehic2, 7)
i = 0
prioridad_alta = 1
prioridad_baja = 0
mision = Mision()
misiones = Cola()
while(mision.tipo != "" or mision.Planeta != "" or mision.general != ""):
    if (mision.general == "Palpatine" or "Darth Vader"):
        Cola.arribo_con_prioridad(misiones, mision, prioridad=prioridad_alta)
        i += 1
    else: 
        Cola.arribo_con_prioridad(misiones, mision, prioridad_baja)
        i += 1
    mision = Mision()
while(i != 0): 
    dato = Cola.barrido(misiones)
    if dato.prioridad == prioridad_alta:
        print("los recursos se introduciran manualmente")
        stormtroopers = input("stormtroopers > ")
        vehiculos = input("vehiculos > ")
        i -= 1
    else:
        Mision.recursos(dato)
        i -= 1

