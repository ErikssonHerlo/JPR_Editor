from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos
from Instrucciones.Break import Break


class Llamada(Instruccion):
    def __init__(self, nombre, fila, columna):
        self.nombre = nombre
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        result = tree.getFuncion(self.nombre.lower()) ## OBTENER LA FUNCION
        if result == None: # NO SE ENCONTRO LA FUNCION
            return Excepcion("Semantico", "No se encontro la Funcion: " + self.nombre, self.fila, self.columna)

        # OBTENER PARAMETROS

        value = result.interpretar(tree, table)         # INTERPRETAR EL NODO FUNCION
        if isinstance(value, Excepcion): return value
        self.tipo = result.tipo

        return value 

"""
    Creditos: 
        Jose Francisco Puac - Repositorio del Curso
        Se utilizo como una base para el proyecto
        Eriksson Hernández - Desarollador
"""