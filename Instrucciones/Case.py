from Abstract.Instruccion import Instruccion
from Abstract.NodoAST import NodoAST
from Instrucciones.Break import Break
from Instrucciones.Return import Return
from Instrucciones.Continue import Continue
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
        if isinstance(condicion,Excepcion): 
            tree.getExcepciones().append(condicion)
            tree.updateConsola(condicion.toString())
            return condicion
        
        if isinstance(condicion, Break): return True
        if isinstance(condicion, Return): return condicion
        if isinstance(condicion, Continue): return condicion


    def getInstrucciones(self):
        return self.instrucciones

    def getNodo(self):
        nodo = NodoAST("CASE")

        instrucciones = NodoAST("INSTRUCCIONES")
        for instr in self.instrucciones:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo 
"""
    Creditos: 
        Jose Francisco Puac - Repositorio del Curso
        Se utilizo como una base para el proyecto
        Eriksson Hernández - Desarollador
"""