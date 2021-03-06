from re import A
from TS.Tipo import TIPO
from Abstract.NodoAST import NodoAST
from TS.Excepcion import Excepcion
from Abstract.Instruccion import Instruccion
from TS.Simbolo import Simbolo
import copy


class ReferenciaArreglo(Instruccion):
    def __init__(self, tipo, dimensiones_arreglo1, identificador1, identificador2, fila, columna):
        self.identificador1 = identificador1
        self.identificador2 = identificador2
        self.tipo = tipo
        self.dimensiones_arreglo1 = dimensiones_arreglo1
        self.fila = fila
        self.columna = columna
        self.arreglo = True
        self.dimensiones_arreglo2 = 1


    def interpretar(self, tree, table):
        try:
            arreglo2 = table.getTabla(self.identificador2.lower())

            if arreglo2 == None:
                return Excepcion("Semantico", "Variable " + self.identificador2 + " no encontrada.", self.fila, self.columna)

            if not arreglo2.getArreglo(): 
                return Excepcion("Semantico", "Variable " + self.identificador2 + " no es un arreglo.", self.fila, self.columna)

            if self.tipo != arreglo2.getTipo():
                return Excepcion("Semantico", "Tipo de dato diferente en " + self.identificador2, self.fila, self.columna)

            expresiones_arreglo2 = arreglo2.getValor()
            self.obtenerDimension(expresiones_arreglo2)
            if self.dimensiones_arreglo1 != self.dimensiones_arreglo2:   #VERIFICACION DE DIMENSIONES
                return Excepcion("Semantico", "Dimensiones diferentes en Arreglo.", self.fila, self.columna)

            arreglo1 = Simbolo(str(self.identificador1), self.tipo, self.arreglo, self.fila, self.columna, arreglo2.getValor())
            result = table.setTabla(arreglo1)
            if isinstance(result, Excepcion): return result
            return None
        except:
            return Excepcion("Semantico", "El indice del arreglo sobrepasa el rango.", self.fila, self.columna)

    def getNodo(self):
        nodo = NodoAST("REFERENCIA ARREGLO")
        nodo.agregarHijo(str(self.tipo))
        nodo.agregarHijo(str(self.dimensiones_arreglo1))
        nodo.agregarHijo(str(self.identificador1))
        nodo.agregarHijo(str(self.identificador2))
        return nodo

    def obtenerDimension(self, expresiones):
        for expresion in expresiones:
            if(isinstance(expresion,list)):
                self.dimensiones_arreglo2 += 1 
                self.obtenerDimension(expresion)
            return None



