#1.1 Creacion
#crea una clase llamada stormtrooper.py que tenga los atributos nombre y rango
#crea el constructor de la clase. Añadir en el contructor un print para informar de que el stormtrooper se ha creado con exito
#crear un metodo llamada "calificacion" que clasifique a los stormtroopers en funcion de su rango del imperio galactico de la siguiente manera
#tk-8654
#tk= codigo de legion 
#8= identificador de cohoerte
#6= identificador de siglo
#5= identificador de escuadra
#4= numero de Trooper
#1.2 Experimentacion
#crea una lista con un numero arbitrario de objetos tipo stormtrooper
#recorre los elementos de la lista y prueba a ejecutar el metodo calificacion de cada objeto que has sacado de la lista

class stormtrooper(object):
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
    def __str__(self):
        print("El stormtrooper {} se ha creado con exito".format(self.nombre))
    def Clasificacion(self):
        cod_leg = input("Introduzca el codigo de la legión de la Stormtrooper(2chrmáx): ")
        Id_Cohor = input("Introduzca el identificador de cohoerte(1intmáx): ")
        Id_siglo = input("Introduzca el identificador del siglo(1 int máx): ")
        Id_esc = input("Intoduzca el identificador de Escuadra: ")
        num_troop = input("Introduzca el numero de troopers: ")
        self.clasificacion = cod_leg + "-" + Id_Cohor + Id_siglo + Id_esc + num_troop
        return self.clasificacion
str1 = stormtrooper("ho", 6)
print(stormtrooper.Clasificacion(str1))

        

import unittest
class TestEjercicio(unittest.TestCase):
    def test_Clasificacion(self):
        stormt1 = stormtrooper("Imperio", 20)
        stormt2 = stormtrooper("Resistencia", 15)
        lista_stormtroo = []
        lista_stormtroo.append(stormt1)
        lista_stormtroo.append(stormt2)
        # 1er Stormtrooper
        stormtrooper_clasificado1 = stormtrooper.Clasificacion(stormt1)
        print("Identifique la clasificacion e introduzca los valores para comprobar si la funcion es correcta")
        print(stormtrooper_clasificado1)
        self.assertEqual(stormtrooper_clasificado1, stormtrooper.Clasificacion(stormt1))
        # 2ndo Stormtrooper
        stormtrooper_clasificado2 = stormtrooper.Clasificacion(stormt2)
        print("Identifique la clasificacion e introduzca los valores para comprobar si la funcion es correcta")
        print(stormtrooper_clasificado2)
        self.assertEqual(stormtrooper_clasificado2, stormtrooper.Clasificacion(stormt2))




