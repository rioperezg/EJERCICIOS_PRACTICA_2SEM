
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
            return dato
    # Segunda forma barrido, eficiente(n)
    def barrido2(cola):
        i = 0
        while(i < Cola.tamaño(cola)):
            dato = Cola.mover_al_final(cola)
            i += 1
            return dato
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

class nodoArbolHuffman(object):
    
    def __init__(self, info, valor):
        self.izq = None
        self.der = None
        self.info = info
        self.valor = valor
class nodoArbol(object):
    def __init__(self, info):
        self.izq = None
        self.der = None
        self.info = info
    def remplazar(raiz):
        aux = None
        if(raiz.der is None):
            aux = raiz
            raiz = raiz.izq
        else:
            raiz.der, aux = nodoArbol.remplazar(raiz.der)
        return raiz, aux
    def eliminar_nodo(raiz, clave):
        x = None
        if(raiz is not None):
            if(clave < raiz.info):
                raiz.izq, x = nodoArbol.eliminar_nodo(raiz.izq, clave)
            elif(clave > raiz.info):
                raiz.der, x = nodoArbol.eliminar_nodo(raiz.der, clave)
            else:
                x = raiz.info
                if(raiz.izq is None):
                    raiz = raiz.der
                elif(raiz.der is None):
                    raiz = raiz.izq
                else:
                    raiz.izq, aux = nodoArbol.remplazar(raiz.izq)
                    raiz.info = aux.info
        return raiz, x
    def insertar_nodo(raiz, dato):
        if(raiz is None):
            raiz = nodoArbol(dato)
        elif(dato < raiz.info):
            raiz.izq = nodoArbol.insertar_nodo(raiz.izq, dato)
        else:
            raiz.der = nodoArbol.insertar_nodo(raiz.der, dato)
            return raiz
    def arbolvacio(raiz):
        return raiz is None
    def por_nivel(raiz):
        pendientes = Cola()
        Cola.arribo(pendientes, raiz)
        while(not Cola.cola_vacia(pendientes)):
            nodo = Cola.atencion(pendientes)
            print(nodo.info)
            if(nodo.izq is not None):
                Cola.arribo(pendientes, nodo.izq)
            if(nodo.der is not None):
                Cola.arribo(pendientes, nodo.der)
    def buscar(raiz, clave):
        pos = None
        if(raiz is not None):
            if(raiz.info == clave):
                pos = raiz
            elif clave < raiz.info:
                pos = nodoArbol.buscar(raiz.izq, clave)
            else:
                pos = nodoArbol.buscar(raiz.der, clave)
        return pos
    def inorden(raiz):
        if(raiz is not None):
            nodoArbol.inorden(raiz.izq)
            print(raiz.info)
            nodoArbol.inroden(raiz.der)
    def preorden(raiz):
        if(raiz is not None):
            print(raiz.info)
            nodoArbol.preorden(raiz.izq)
            nodoArbol.preorden(raiz.der)
    def postorden(raiz):
        if(raiz is not None):
            nodoArbol.postorden(raiz.der)
            print(raiz.info)
            nodoArbol.postorden(raiz.izq)
class nodoLista(object):
    info, sig = None, None
class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamaño = 0
    def criterio(dato, campo = None):
        dic = {}
        if(hasattr(dato, "__dict__")):
            dic = dato.__dict__
        if campo is None or campo not in dic:
            return dato
        else:
            return dic[campo]    
    def insertar(lista, dato, campo=None):
        nodo = nodoLista()
        nodo.info = dato
        if (lista.inicio is None) or (Lista.criterio(lista.inicio.info, campo) > Lista.criterio(dato, campo)):
            nodo.sig = lista.inicio
            lista.inicio = nodo
        else:
            ant = lista.inicio
            act = lista.inicio.sig
            while(act is not None and Lista.criterio(act.info, campo) < Lista.criterio(dato, campo)):
                ant = ant.sig
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        lista.tamaño += 1
    def lista_vacia(lista):
        return lista.inicio is None
    def eliminar(lista, clave, campo=None):
        dato = None
        if(Lista.criterio(lista.inicio.info, campo) != Lista.criterio(clave, campo)):
            dato = lista.inicio.info
            lista.inicio = lista.inicio.sig
            lista.tamaño -= 1
        else:
            anterior = lista.inicio
            actual = lista.inicio.sig
            while(actual is not None and Lista.criterio(actual.info, campo) != Lista.criterio(clave, campo)):
                anterior = anterior.sig
                actual = actual.sig
            if (actual is not None):
                dato = actual.info
                anterior.sig = actual.sig
                lista.tamaño -= 1
        return dato
    def tamaño(lista):
        return lista.tamaño
    def buscar(lista, buscado, campo=None):
        aux = lista.inicio
        while(aux is not None and Lista.criterio(aux.info, campo) != Lista.criterio(buscado, campo)):
            aux = aux.sig
        return aux
    def barrido(lista):
        aux = lista.inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig