"""
El gran almirante del MCU Khan “El Conquistador” es el estratega del multiverso y normalmente se encuentra desbordado de pedidos de 
sugerencia de cómo actuar por las variantes de el mismo de las diferentes épocas y Multiversos. Para lo cual nos solicita desarrollar un 
algoritmo que le permita atender los pedidos de ayuda de acuerdo con la prioridad de los mismo en base a los siguientes requerimientos:
 
se deben contemplar tres niveles de prioridad para la cola;
 
cada pedido de sugerencia cuenta con la siguiente información: nombre del “Khan” solicitante, multiverso en el que se encuentra o el más 
próximo y descripción del pedido;
 
aquellos pedidos que provengan del “Gran Conquistador”, del universo de 616 o la descripción mencione a “El que permanece” tendrán la mayor 
prioridad;
 
si el pedido es del “Khan que todo lo sabe” o la descripción menciona “Carnicero de Dioses” o universo “838” tendrán prioridad media;
 
el resto de los pedidos serán de prioridad baja;
 
realizar la atención de la cola almacenando los pedidos de mayor prioridad en una pila llamada “bitácora” para revisión y seguimiento;
 
luego de cada atención se podrá agregar un pedido a la cola.
"""
from Herramientas import Cola
class Pedido(object):
    def __init__(self):
        self.solicitante = input("Nombre del solicitante: ")
        self.multiverso = input("Nombre del multiverso: ")
        self.descripcion = input("descripcion")
def bitacora():
    pedido = Pedido()
    pedidos = Cola()
    bitacora = Cola()
    mayor = 2
    media = 1
    baja = 0
    while(pedido.solicitante != ""):
        if (pedido.solicitante == "Gran Conquistador"):
            Cola.arribo_con_prioridad(pedidos, pedido, mayor)
        elif(pedido.multiverso == 616):
            Cola.arribo_con_prioridad(pedidos, pedido, mayor)
        elif(pedido.descripcion == "El que permanece"):
            Cola.arribo_con_prioridad(pedidos, pedido, mayor)
        elif(pedido.solicitante == "Khan que todo lo sabe"):
            Cola.arribo_con_prioridad(pedidos, pedido, media)
        elif(pedido.multiverso == 838):
            Cola.arribo_con_prioridad(pedidos, pedido, media)
        elif(pedido.descripcion == "Carnicero de Dioses"):
            Cola.arribo_con_prioridad(pedidos, pedido, media)
        else:
            Cola.arribo_con_prioridad(pedidos, pedido,baja)
        pedido = Pedido()
        

    

    
