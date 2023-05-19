""""
Nick Fury, líder de la agencia S.H.I.E.L.D., tiene la difícil tarea de decidir qué vengador asignará a cada nueva misión 
(por ahora considere que solo se asignará un superhéroe por cada misión). Teniendo en cuenta el listado de superhéroes es el siguiente:
"""
from herramientas import nodoArbol, Cola

# Haremos un input para hacer de todos los agentes una cola
def Crear_cola(elemento):
    Cola_s = Cola()
    print("Introduzca un@ ", elemento)
    Superheroe = input("> ")
    while(Superheroe != ""):
       Cola.arribo(Cola_s, Superheroe)
       print("Introduzca un@ ", elemento)
       Superheroe = input("> ")
    return Cola_s

def Arbol_Superh(cola_Super, cola_misio):
    # Arbol Vacio
    raiz = None
    while(not Cola.cola_vacia(cola_misio)):
        Superheroe = Cola.atencion(cola_Super)
        print("Nombre del Superheroe: ",Superheroe)
        Mision = Cola.atencion(cola_misio)
        Cometido = print("¿Esta el superheroe destinado a ",Mision,"?")
        nodoArbol.insertar_nodo(raiz, Cometido)
        respuesta = input("(si/no)> ")
    # Comenzamos a cargar el arbol: Si resulta que el superheroe esta destinado a la mision sera almacenado en la rama izq mientras que 
    # la pregunta sera siempre almacenada en la dcha
    # Cmbio de planes: El arbol principal seran las preguntas
        if(respuesta == "si"):
            Superheroe < raiz.info
            nodoArbol.insertar_nodo(raiz, Superheroe)
        elif(respuesta == "no"):
            Superheroe > raiz.info
            nodoArbol.insertar_nodo(raiz, Superheroe)
        
           










