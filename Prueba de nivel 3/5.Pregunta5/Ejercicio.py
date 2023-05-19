"""
Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera alea- toria– que resuelva las siguientes actividades:
 
realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
 determinar si un número está cargado en el árbol o no;
 eliminar tres valores del árbol;
 determinar la altura del subárbol izquierdo y del subárbol derecho;
 determinar la cantidad de ocurrencias de un elemento en el árbol;
 contar cuántos números pares e impares hay en el árbol.
"""
import random
from Herramientas import nodoArbol, NodoArbol
i = 0
num = int(random)
Arbol_de_nums = NodoArbol()
while(i != 1000):
    NodoArbol.insertar_nodo(Arbol_de_nums, num)
    i += 1
    num = int(random)
def barridos(Arbol):
    nodoArbol.inorden(Arbol)
    print("Barrido inorden realizado")
    nodoArbol.preorden(Arbol)
    print("Barrido preorden realizado")
    nodoArbol.postorden(Arbol)
    print("Barrido postorden realizado")
    nodoArbol.por_nivel(Arbol)
    print("Barrido por nivel realizado")
def Cargado(Arbol, num):
    pos = nodoArbol.buscar(Arbol, num)
    if pos != None:
        print("El elemento se encuentra en el arbol")
    else:
        print("El elemento no se encuentra en el arbol")

