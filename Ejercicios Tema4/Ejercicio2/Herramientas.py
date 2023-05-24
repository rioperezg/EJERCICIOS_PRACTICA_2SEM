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
            cola.final = nodo
        cola.final = nodo
        cola.tamaño += 1
    def atencion(cola):
        aux = cola.datos[cola.frente]
        cola.frente += 1
        if(cola.frente==len(cola.datos)):
            cola.frente = 0
        cola.tamanio -= 1
        return aux
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