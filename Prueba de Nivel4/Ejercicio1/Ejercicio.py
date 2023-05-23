"""
Dado un grafo no dirigido con personajes del MCU de la siguiente tabla:

 



 

 

Implementar los algoritmos necesarios para resolver las siguientes tareas:

 

cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos 
ambos personajes que se relacionan;
 

hallar el árbol de expansión máximo desde el vértice que contiene a Iron-Man, Thor y The Winter Soldier;
 

determinar cuál es el número máximo de episodio que comparten dos personajes, e indicar todos los pares de personajes que coinciden con 
dicho número
 

cargue todos los personajes de la tabla anterior
 

indicar qué personajes aparecieron en nueve episodios de la saga
"""
#  Primero cargaremos los personajes en un grafo
from Herramientas import Grafo, Cola, nodoArista, nodoVertice, Arista, prim, Kruskal
grafo_Superh = Grafo(False)
Superheroe = nodoVertice(info = input("Ingrese el nombre del superheroe a cargar: "))
while(Superheroe.info != ""):
    Arista.insertar_vertice(grafo_Superh, Superheroe)
    Superheroe = nodoVertice(info = input("Ingrese el nombre del superheroe a cargar(Pulse enter si ha terminado): "))
# Ahora determinaremos el numero de episodios que hay entre todos ellos
print("Ingrese dos personajes que hayan coincidido en un episodio o mas")
Superheroe1 = input("Superheroe 1: ")
Superheroe2 = input("Superheroe 2: ")
while(Superheroe1 != ""):
    episodios = nodoArista(info = int(input("Ingrese la cantidad de episodios en los que han coincidido: ")), destino=None)
    Arista.insertar_arista(grafo_Superh, episodios, Superheroe1, Superheroe2)
    print("Ingrese dos personajes que hayan coincidido en un episodio o mas(Presione enter si ha terminado)")
    Superheroe1 = input("Superheroe 1: ")
# Estrategia
"""
Volviendo un poco para atrás, mencionamos que a veces es útil hallar el árbol de expansión máxi- mo, pero ¿Cómo hacemos para hallarlo? 
Los algoritmos son los mismos que utilizamos anteriormente, pero para que en cada iteración tomen la arista de mayor peso, debemos utilizar 
un montículo máxi- mo para la cola de prioridad. Otra alternativa para encontrar el árbol de expansión máximo sin mo- dificar los algoritmos 
hechos para hallar el árbol de expansión mínimo, es transformar el peso de las aristas a mínimo. Para hacer esto primero buscamos la arista 
de mayor peso del grafo y luego a dicho valor le restamos el original de cada arista, como se puede observar en la siguiente tabla. Nótese 
que ahora las aristas que antes tenían mayor peso, ahora tienen el menor peso y las menores ahora son mayores, lo cual nos permite aplicar 
los algoritmos desarrollados para hallar el árbol mínimo.
"""
# Ahora hallaremos el arbol de expansion maximo
# Primero hallaremos el peso maximo
peso_max = 0
aux = grafo_Superh.inicio
while(aux is not None):
    aux2 = aux.adyacentes.inicio
    while(aux2 is not None):
        if(aux2.info > peso_max):
            peso_max = aux2.info
        aux2 = aux2.sig
    aux = aux.sig
# Ahora restaremos el peso maximo a cada arista
aux = grafo_Superh.inicio
while(aux is not None):
    aux2 = aux.adyacentes.inicio
    while(aux2 is not None):
        aux2.info = peso_max - aux2.info
        aux2 = aux2.sig
    aux = aux.sig
# Ahora hallaremos el arbol de expansion minimo con el algoritmo de prim
arbol_minimo = Kruskal(grafo_Superh)


