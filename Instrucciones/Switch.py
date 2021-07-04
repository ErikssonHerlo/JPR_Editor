from Instrucciones.Break import Break
from Abstract.Instruccion import Instruccion
from Abstract.NodoAST import NodoAST
from TS.Excepcion         import Excepcion
from Instrucciones.Continue import Continue
from Instrucciones.Return import Return

class Switch(Instruccion):
    def __init__(self, condicionSwitch, listaCase,default, fila, columna):
        self.condicionSwitch = condicionSwitch
        self.listaCase = listaCase
        self.default = default
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        condicionSwitch = self.condicionSwitch.interpretar(tree,table)
        if isinstance(condicionSwitch,Excepcion): return condicionSwitch

        if self.listaCase != None:
            for instruccion in self.listaCase:
                condicionCase = instruccion.condicion.interpretar(tree,table)

                if condicionCase == condicionSwitch:
                    for instruccionCase in instruccion.instrucciones:
                        result = instruccionCase.interpretar(tree,table)
                        if isinstance(result,Excepcion):
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        
                        if isinstance(result,Break): return None
                        if isinstance(result,Continue): return result
                        if isinstance(result,Return): return result

        if self.default != None:
            for instruccionesDefault in self.default:
                result = instruccionesDefault.interpretar(tree,table)
                if isinstance(result,Excepcion):
                    tree.getExcepciones().append(result)
                    tree.updateConsola(result.toString())
                    return None

    def getNodo(self):
        nodo = NodoAST("SWITCH")

        instrucciones = NodoAST("CASES")
        for instr in self.listaCase:
            instrucciones.agregarHijoNodo(instr.getNodo())
        nodo.agregarHijoNodo(instrucciones)
        return nodo    



"""
    Creditos: 
        Jose Francisco Puac - Repositorio del Curso
        Se utilizo como una base para el proyecto
        Eriksson Hernández - Desarollador
"""

