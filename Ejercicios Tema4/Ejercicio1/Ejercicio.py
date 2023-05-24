"""
Desarrollar los algoritmos necesarios para generar un árbol de Huffman a partir de la siguiente tabla –para lo cual deberá calcular 
primero las frecuencias de cada carácter a partir de la can- tidad de apariciones del mismo–, para resolver las siguientes actividades:
 
la generación del árbol debe hacerse desde los caracteres de menor frecuencia hasta los de mayor, en el caso de que dos caracteres tengan 
la misma frecuencia, primero se toma el que este primero en el alfabeto, el carácter “espacio” y “coma” se consideraran anteúltimo y último 
respectivamente en el orden alfabético;
 
descomprimir los siguientes mensajes –cuyo árbol ha sido construido de la misma manera que el ejemplo visto anteriormente:
"""
from Herramientas import nodoArbol, nodoArbolHuffman, Lista, nodoLista, Cola
# Primero hemos de calcular las frecuencias, hagamoslo generico por supuesto, Haremos una clase con objeto carater, y atributos cantidad 
# y Frecuencia, Podemos hacerlo con input
class Caracter(object):
    def __init__(self):
        size = int(input("Cuantas letras tiene la tabla en total?: "))
        self.string = input("Caracter: ")
        self.cantidad = int(input("Cantidad: "))
        self.frecuencia = self.cantidad / size
raiz = None
lista_de_nums = Lista()
letra = Caracter()
while(letra.string != ""):
    Letra = nodoArbolHuffman(info=letra.string, valor=letra.frecuencia)
    # Hay q almacenar primeramente los caracteres en una lista segun peso y orden alfabetico
    Lista.insertar(lista_de_nums, Letra.info, campo = Letra.valor)
    letra = Caracter()



# Estas dos funciones las necesitaremos seguro
def generar_tabla(nodo, tabla, codigo=""):
    if nodo is not None:
        if nodo.izquierdo is None and nodo.derecho is None:
            tabla[nodo.caracter] = codigo
        else:
            generar_tabla(nodo.izquierdo, tabla, codigo + "0")
            generar_tabla(nodo.derecho, tabla, codigo + "1")
 
def decodificar(cadena, arbol_huff):
    cadena_deco = ''
    raiz_aux = arbol_huff
    pos = 0
    while(pos < len(cadena)):
        if(cadena[pos] == '0'):
            raiz_aux = raiz_aux.izquierdo
        else:
            raiz_aux = raiz_aux.derecho
        pos += 1
        if(raiz_aux.izquierdo is None):
            cadena_deco += raiz_aux.caracter
            raiz_aux = arbol_huff
    return cadena_deco

Lista.barrido(lista_de_nums)






