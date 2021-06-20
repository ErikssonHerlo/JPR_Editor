from Instrucciones.Declaracion import Declaracion
from Instrucciones.Asignacion import Asignacion
from Abstract.Instruccion import Instruccion
from Instrucciones.Break import Break
from TS.Excepcion         import Excepcion
from TS.Tipo              import TIPO
from TS.TablaSimbolos     import TablaSimbolos

class For(Instruccion):
    def __init__(self, valorInicial, condicion, incremento_decremento, instrucciones,linea,columna):
        self.condicion = condicion
        self.valorInicial = valorInicial
        self.incremento_decremento = incremento_decremento
        self.instrucciones = instrucciones
        self.linea = linea
        self.columna = columna

    def interpretar(self, tree, table):

        #valorInicial = self.valorInicial.interpretar(tree,table)
        #if isinstance(valorInicial, Excepcion): return valorInicial
       
        isDeclaracion = False
        nuevaTable = None
        if isinstance(self.valorInicial,Declaracion):
            nuevaTable = TablaSimbolos(table)
            valorInicial = self.valorInicial.interpretar(tree,nuevaTable)
            isDeclaracion = True
        else:
            valorInicial = self.valorInicial.interpretar(tree,table)

        while True:
            if isDeclaracion :
                condicion = self.condicion.interpretar(tree, nuevaTable)
            else:
                condicion = self.condicion.interpretar(tree, table)
                

            if isinstance(condicion, Excepcion): return condicion

            if self.condicion.tipo == TIPO.BOOLEANO:
                if bool(condicion) == True:  # VERIFICA SI ES VERDADERA LA CONDICION
                    if isDeclaracion:
                        nuevaTabla = TablaSimbolos(nuevaTable)  # NUEVO ENTORNO
                    else:
                        nuevaTabla = TablaSimbolos(table)  # NUEVO ENTORNO
                        

                    for instruccion in self.instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla)  # EJECUTA INSTRUCCION ADENTRO DEL FOR
                        if isinstance(result, Excepcion):
                            tree.getExcepciones().append(result)
                            tree.updateConsola(result.toString())
                        if isinstance(result, Break): return None
                    
                    self.incremento_decremento.interpretar(tree,nuevaTabla)
                else:
                    break
            else:
                return Excepcion("Semantico", "Tipo de Dato no booleano en la Condicional del Ciclo (For).", self.fila, self.columna)
            


    def instruccionesInterprete(self, instruccion, tree, table):

    # REALIZAR LAS ACCIONES
        if isinstance(instruccion, list):           #agregado
            for elemento in instruccion:
                self.instruccionesInterprete(elemento, tree,table)
        else:              
            value = instruccion.interpretar(tree,table)
            if isinstance(value, Excepcion) :
                tree.getExcepciones().append(value)
                tree.updateConsola(value.toString())