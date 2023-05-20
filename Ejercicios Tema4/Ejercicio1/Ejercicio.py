"""
Desarrollar los algoritmos necesarios para generar un árbol de Huffman a partir de la siguiente tabla –para lo cual deberá calcular 
primero las frecuencias de cada carácter a partir de la can- tidad de apariciones del mismo–, para resolver las siguientes actividades:
 
la generación del árbol debe hacerse desde los caracteres de menor frecuencia hasta los de mayor, en el caso de que dos caracteres tengan 
la misma frecuencia, primero se toma el que este primero en el alfabeto, el carácter “espacio” y “coma” se consideraran anteúltimo y último 
respectivamente en el orden alfabético;
 
descomprimir los siguientes mensajes –cuyo árbol ha sido construido de la misma manera que el ejemplo visto anteriormente:
"""
from Herramientas import nodoArbol, nodoArbolHuffman
# Primero hemos de calcular las frecuencias, hagamoslo generico por supuesto, Haremos una clase con objeto carater, y atributos cantidad 
# y Frecuencia, Podemos hacerlo con input
class Caracter(object):
    def __init__(self):
        size = input("Cuantas letras tiene la tabla en total?: ")
        self.string = input("Caracter: ")
        self.cantidad = input("Cantidad: ")
        self.frecuencia = self.cantidad / size
raiz = None
lista = []
letra = Caracter()
while(letra.string != ""):
    Letra = nodoArbolHuffman(info=letra.string, valor=letra.frecuencia)
    # Hay q almacenar primeramente los caracteres en una lista segun peso y orden alfabetico
    lista.append(Letra)





