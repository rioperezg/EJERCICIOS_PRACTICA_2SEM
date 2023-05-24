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
# Probemos a darle una estructura personalizada
class nodoArista(object):
    def __init__(self, info , destino):
        self.info = info
        self.destino = destino
        self.sig = None
class nodoVertice_ferro(object):
    def __init__(self, info, tipo):
        self.info = info
        self.tipo = tipo
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()
class Grafo(object):
    def __init__(self, dirigido = True):
        self.inicio = None
        self.dirigido = dirigido
        self.tamaño = 0
class Arista(object):
    def __init__(self):
        self.inicio = None
        self.tamaño = 0
    def insertar_vertice(grafo, dato, tipo):
        nodo = nodoVertice_ferro(dato, tipo)
        if (grafo.inicio is None or grafo.inicio.info > dato):
            nodo.sig = grafo.inicio
            grafo.inicio = nodo
        else:
            ant = grafo.inicio
            act = grafo.inicio.sig
            while(act is not None and act.info < dato):
                ant = act
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        grafo.tamaño += 1



red_ferro = Grafo(False)
tipo = input("Desvio/Estación: ")
if tipo == "Estacion":
    i = 0
    while (i < 6):
        estacion = input("(debe ingresar 6 estaciones)Ingrese el nombre de la estacion a cargar: ")
        Arista.insertar_vertice(red_ferro, estacion, tipo)
        i += 1
    tipo = input("Desvio/Estación: ")
    if tipo == "Desvio":
        j = 0
        while (j < 12):
            desvio = info=input("Ingrese el nombre del desvio a cargar: ")
            Arista.insertar_vertice(red_ferro, desvio, tipo)
            j += 1
    else:
        print("Debio de introducir Desvio")
    
elif tipo == "Desvio":       
    j = 0
    while (j < 12):
        desvio = info=input("Ingrese el nombre del desvio a cargar: ")
        Arista.insertar_vertice(red_ferro, desvio, tipo)
        j += 1
    tipo = input("Desvio/Estación: ")
    if tipo == "Estación":
        i = 0
        while (i < 6):
            estacion = input("(debe ingresar 6 estaciones)Ingrese el nombre de la estacion a cargar: ")
            Arista.insertar_vertice(red_ferro, estacion, tipo)
            i += 1
    else:
        print("Debio introducir Estacion")

# Tamaño = Arista.tamaño(red_ferro)
# while(Tamaño > 0):


