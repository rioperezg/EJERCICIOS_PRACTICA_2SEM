""""
Nick Fury, líder de la agencia S.H.I.E.L.D., tiene la difícil tarea de decidir qué vengador asignará a cada nueva misión 
(por ahora considere que solo se asignará un superhéroe por cada misión). Teniendo en cuenta el listado de superhéroes es el siguiente:
"""
from herramientas import nodoArbol, Cola
# Primero creamos el arbol con las misiones 
print("Ingrese todos los tipos de misiones que se realizaran")
mision = nodoArbol(info=input("Tipo de mision(Intergalactica, de recuperacion, etc...): "))
while(mision.info != ""):
    mision.info = mision.der
    
