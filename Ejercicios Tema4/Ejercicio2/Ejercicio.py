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
from Herramientas import Cola

class Mision(object):
    def __init__(self):
        self.tipo = input("(Presione enter si quiere salir) Tipo de misión: ")
        self.Planeta = input("(Presione enter si quiere salir) Planeta de destino: ")
        self.general = input("(Presione enter si quiere salir) General que solicita la msiion: ")
prioridad_alta = 1
prioridad_baja = 0
mision = Mision()
misiones = Cola()
while(mision.tipo != "" or mision.Planeta != "" or mision.general != ""):
    if (mision.general == "Palpatine" or "Darth Vader"):
        Cola.arribo_con_prioridad(misiones, mision, )