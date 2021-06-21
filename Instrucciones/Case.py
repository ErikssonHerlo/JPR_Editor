from Abstract.Instruccion import Instruccion
from Instrucciones.Break import Break
from TS.Excepcion         import Excepcion
from TS.TablaSimbolos     import TablaSimbolos

class Case(Instruccion):
    def __init__(self, condicion, instrucciones, fila, columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        condicion = self.condicion.interpretar(tree,table)
        if isinstance(condicion,Excepcion): return condicion

    def getInstrucciones(self):
        return self.instrucciones

"""
    Creditos: 
        Jose Francisco Puac - Repositorio del Curso
        Se utilizo como una base para el proyecto
        Eriksson Hernández - Desarollador
"""