
class nodoCola(object):
    info, sig = None, None
class Cola(object):
    def __init__(self):
        self.frente, self.final = None, None
        self.tamaño = 0
    def arribo(cola, dato):
        nodo = nodoCola()
        nodo.info = dato
        if cola.frente is None:
            cola.frente = nodo
        else:
            cola.final.sig = nodo
        cola.final = nodo
        cola.tamaño += 1
    def atencion(cola, dato):
        dato = cola.frente.info
        cola.frente = cola.frente.sig
        if cola.frente is None:
            cola.final = None
            cola.tamaño -= 1
            return dato
    def cola_vacia(cola):
        return cola.frente is None
    def en_frente(cola):
        return cola.frente.info
    def tamaño(cola):
        return cola.tamaño
    def mover_al_final(cola):
        dato = Cola.atencion(cola)
        Cola.arribo(cola,dato)
        return dato
    # Primera forma barrido, ineficiente(n^2)
    def barrido(cola):
        caux = Cola()
        while(not Cola.cola_vacia(cola)):
            dato = Cola.atencion(cola)
            print(dato)
            Cola.arribo(caux, dato)
        while(not Cola.cola_vacia(caux)):
            dato = Cola.atencion(caux)
            Cola.arribo(cola,dato)
    # Segunda forma barrido, eficiente(n)
    def barrido2(cola):
        i = 0
        while(i < Cola.tamaño(cola)):
            dato = Cola.mover_al_final(cola)
            print(dato)
            i += 1
    def arribo_con_prioridad(cola, elemento, prioridad):
        nodo = nodoCola()
        nodo.info = elemento
        nodo.prioridad = prioridad
        if cola.frente is None or prioridad < cola.frente.prioridad:
            nodo.sig = cola.frente
            cola.frente = nodo
        else:
            ant = cola.frente
            act = cola.frente.sig
            while(act is not None and act.prioridad <= prioridad):
                ant = act
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        cola.tamaño += 1
class nodoArista(object):
    def __init__(self, info , destino):
        self.info = info
        self.destino = destino
        self.sig = None
class nodoVertice(object):
    def __init__(self, info):
        self.info = info
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
    def insertar_vertice(grafo, dato):
        nodo = nodoVertice(dato)
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
        
    def insertar_arista(grafo, dato, origen, destino):
        Arista.agregar_arista(origen.adyacentes, dato, destino.info)
        if(not grafo.dirigido):
            Arista.agregar_arista(destino.adyacentes, dato, origen.info)
    
    def agregar_arista(origen, dato, destino):
        nodo = nodoArista(dato, destino)
        if(origen.inicio is None or origen.inicio.destino > destino):
            nodo.sig = origen.inicio
            origen.inicio = nodo
        else:
            ant = origen.inicio
            act = origen.inicio.sig
            while(act is not None and act.destino < nodo.destino):
                ant = act
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
            origen.tamaño += 1
    def eliminar_vertice(grafo, clave):
        x = None 
        if(grafo.inicio.info == clave):
            x = grafo.inicio.info
            grafo.inicio = grafo.inicio.sig
            grafo.tamaño -= 1
        else:
            ant = grafo.inicio
            act = grafo.inicio.sig
            while(act is not None and act.info != clave):
                ant = act
                act = act.sig
            if(act is not None):
                x = act.info
                ant.sig = act.sig
                grafo.tamaño -= 1
        if(x is not None):
            aux = grafo.inicio
            while(aux is not None):
                if(aux.adyacentes.inicio is not None):
                    Arista.eliminar_arista(aux.adyacentes, clave)
                aux = aux.sig
        return x
    def buscar_vertice(grafo, buscado):
        aux = grafo.inicio
        while(aux is not None and aux.info != buscado):
            aux = aux.sig
        return aux
    def buscar_arista(vertice, buscado):
        aux = vertice.adyacentes.inicio
        while(aux is not None and aux.destino != buscado):
            aux = aux.sig
        return aux
    
    def tamaño(grafo):
        return grafo.tamaño
    def grafo_vacio(grafo):
        return grafo.inicio is None
    
    def eliminar_arista(vertice, destino):
        x = None
        if(vertice.inicio.destino == destino):
            x = vertice.inicio.info
            vertice.inicio = vertice.inicio.sig
            vertice.tamaño -= 1
        else:
            ant = vertice.inicio
            act = vertice.inicio.sig
            while(act is not None and act.destino != destino):
                ant = act
                act = act.sig
            if(act is not None):
                x = act.info
                ant.sig = act.sig
                vertice.tamaño -= 1
        return x
    def existe_paso(grafo, origen, destino):
        resultado = False
        if(not origen.visitado):
            origen.visitado = True
            vadyacentes = origen.adyacentes.inicio
            while(vadyacentes is not None and not resultado):
                adyacente = Grafo.buscar_vertice(grafo, vadyacentes.destino)
                if(adyacente.info == destino.info):
                    resultado = True
                elif(not adyacente.visitado):
                    resultado = Grafo.existe_paso(grafo, adyacente, destino)
                vadyacentes = vadyacentes.sig
        return resultado
    def adyacentes(vertice):
        aux = vertice.adyacentes.inicio
        while(aux is not None):
            print(aux.destino, aux.info)
            aux = aux.sig
    def es_adyacente(vertice, destino):
        resultado = False
        aux = vertice.adyacentes.inicio
        while(aux is not None and not resultado):
            if(aux.destino == destino):
                resultado = True
            aux = aux.sig
        return resultado
    def marcar_no_visitado(grafo):
        aux = grafo.inicio
        while(aux is not None):
            aux.visitado = False
            aux = aux.sig
    def barrido_vertices(grafo):
        aux = grafo.inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig
    def barrido_profundo(grafo, vertice):
        while(vertice is not None):
            if(not vertice.visitado):
                vertice.visitado = True
                print(vertice.info)
                adyacentes = vertice.adyacentes.inicio
                while(adyacentes is not None):
                    adyacente = Arista.buscar_vertice(grafo, adyacentes.destino)
                    if(not adyacente.visitado):
                        Arista.barrido_profundo(grafo, adyacente)
                    adyacentes = adyacentes.sig
            vertice = vertice.sig
    def barrido_amplitud(grafo, vertice):
        cola = Cola()
        while(vertice is not None):
            if(not vertice.visitado):
                vertice.visitado = True
                Cola.arribo(cola, vertice)
                while(not Cola.cola_vacia(cola)):
                    nodo = Cola.atencion(cola)
                    print(nodo.info)
                    adyacentes = nodo.adyacentes.inicio
                    while(adyacentes is not None):
                        adyacente = Arista.buscar_vertice(grafo, adyacentes.destino)
                        if(not adyacente.visitado):
                            adyacente.visitado = True
                            Cola.arribo(cola, adyacente)
                        adyacentes = adyacentes.sig
            vertice = vertice.sig