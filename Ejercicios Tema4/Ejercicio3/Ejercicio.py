"""
Se requiere implementar una red de ferrocarriles compuesta de estaciones de trenes y cambios de agujas (o desvíos). Contemplar las 
siguientes consideraciones:
 
cada vértice del grafo no dirigido tendrá un tipo (estación o desvió) y su nombre, en el caso de los desvíos el nombre es un número –estos 
estarán numerados de manera consecutiva–;
 
cada desvío puede tener múltiples puntos de entrada y salida;
 
se deben cargar seis estaciones de trenes y doce cambios de agujas;

cada cambio de aguja debe tener al menos cuatro salida o vértices adyacentes;
 
y cada estación como máximo dos salidas o llegadas y no puede haber dos estaciones co- nectadas directamente;
 
encontrar el camino más corto desde:
 
la estación King's Cross hasta la estación Waterloo,
 
la estación Victoria Train Station hasta la estación Liverpool Street Station,
 
la estación St. Pancras hasta la estación King's Cross;
"""
from Herramientas import Cola, Arista, Grafo, nodoVertice, nodoArista
# Hemos de cargar 6 estaciones y 12 cambios de agujas
# Cada cambio de aguja debe tener al menos 4 salidas o vertices adyacentes
# Cada estacion como maximo 2 salidas o llegadas y no puede haber dos estaciones conectadas directamente
class Tipo_vert(object):
    def __init__(self):
        tipo = input("Ingrese el tipo de vertice(estacion/desvio): ")
        if tipo == "estacion":
            self.tipo = "estacion"
        elif tipo == "desvio":
            self.tipo = "desvio"
red_ferro = Grafo(False)
estacion = nodoVertice(info=input("Ingrese el nombre de la estacion a cargar: "))
i = 0
while (i < 6):
    Tipo_vert(estacion)
    Arista.insertar_vertice(red_ferro, estacion)
    i += 1
    estacion = nodoVertice(info=input("Ingrese el nombre de la estacion a cargar: "))
desvio = nodoVertice(info=input("Ingrese el nombre del desvio a cargar: "))
i = 0
while (i < 12):
    Tipo_vert(desvio)
    Arista.insertar_vertice(red_ferro, desvio)
    i += 1
    desvio = nodoVertice(info=input("Ingrese el nombre del desvio a cargar: "))

Tamaño = Arista.tamaño(red_ferro)
while(Tamaño > 0):


