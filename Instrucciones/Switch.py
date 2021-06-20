from Instrucciones.Break import Break
from Abstract.Instruccion import Instruccion
from TS.Excepcion         import Excepcion

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

        if self.default != None:
            for instruccionesDefault in self.default:
                result = instruccionesDefault.interpretar(tree,table)
                if isinstance(result,Excepcion):
                    tree.getExcepciones().append(result)
                    tree.updateConsola(result.toString())
                    return None












"""
    def interpretar(self, tree, table):
        if self.listaCase == None:
            if self.default != None:
                self.default.interpretar(tree,table)
        else:
            result = False
            for case in self.listaCase:
                valorCase = case.interpretar(tree,table)
                
                if isinstance(valorCase, Excepcion): return valorCase
                valorCondicion = self.condicion.interpretar(tree,table)
                
                if isinstance(valorCondicion,Excepcion): return 2
                if valorCondicion == valorCase:
                    result = case.interpretar(tree, table)

                    #Analiza si el case tiene break
                    if (result): 
                        break
                    else:
                        if self.default != None:
                            self.default.interpretar(tree,table) #Vuelve a realizar el analisis para adentrarse en el default
            

    def instruccionesInterprete(self, instruccion, tree, table):

    # Realiza las acciones
        if isinstance(instruccion, list): 
            for element in instruccion:
                self.instruccionesInterprete(element, tree,table)
        else:              
            value = instruccion.interpretar(tree,table)
            if isinstance(value, Excepcion) :
                tree.getExcepciones().append(value)
                tree.updateConsola(value.toString())
"""