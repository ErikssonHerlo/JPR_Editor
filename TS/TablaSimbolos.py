from TS.Excepcion import Excepcion
from TS.Tipo import OperadorAritmetico, TIPO

variables = []
class TablaSimbolos:
    def __init__(self, anterior = None):
        self.tabla = {} # Diccionario Vacio
        self.anterior = anterior
        

    def setTabla(self, simbolo):      # Agregar una variable a un ambito
        if simbolo.id.lower() in self.tabla :
            return Excepcion("Semantico", "Variable " + simbolo.id + " ya existe", simbolo.fila, simbolo.columna)
        else:
            self.tabla[simbolo.id.lower()] = simbolo
            encontro=True
            if len(variables)>0:
                for variable in variables:
                    if variable.id==simbolo.id:
                        encontro=True
                        break
                    else:
                        encontro=False
                if encontro==False:
                    variables.append(simbolo)
            else:
                variables.append(simbolo)
                
            return None

    def getTabla(self, id):            # obtener una variable
        try:
            tablaActual = self
            while tablaActual != None: # While solo para tablaActual != None
                if id.lower() in tablaActual.tabla :
                    return tablaActual.tabla[id.lower()]           # RETORNA SIMBOLO
                else:
                    tablaActual = tablaActual.anterior
            return None
        except:
            return None

    def actualizarTabla(self, simbolo):
        tablaActual = self
        while tablaActual != None:
            if simbolo.id.lower() in tablaActual.tabla :
                if tablaActual.tabla[simbolo.id.lower()].getTipo() == simbolo.getTipo() or tablaActual.tabla[simbolo.id.lower()].getTipo()== TIPO.VAR or simbolo.getTipo()== TIPO.NULO:
                    if simbolo.getTipo()== TIPO.NULO:
                        tablaActual.tabla[simbolo.id.lower()].setTipo(TIPO.VAR)
                    else:
                        tablaActual.tabla[simbolo.id.lower()].setTipo(simbolo.getTipo())
                    tablaActual.tabla[simbolo.id.lower()].setValor(simbolo.getValor())
                    for variable in variables:
                        if variable.id==simbolo.id:
                            variable.setValor(simbolo.getValor())
                            variable.setTipo(tablaActual.tabla[simbolo.id.lower()].getTipo())
                            break            
                    return None #VARIABLE ACTUALIZADA
                elif simbolo.getTipo() == OperadorAritmetico.INCREMENTO or simbolo.getTipo() == OperadorAritmetico.DECREMENTO:
                    if (tablaActual.tabla[simbolo.id.lower()].getTipo() == TIPO.ENTERO or tablaActual.tabla[simbolo.id.lower()].getTipo() == TIPO.DECIMAL):
                        valorAnterior = tablaActual.tabla[simbolo.id.lower()].getValor()
                        tablaActual.tabla[simbolo.id.lower()].setValor(valorAnterior+simbolo.getValor())
                        return None
                return Excepcion("Semantico", "Tipo de Dato diferente en Asignacion", simbolo.getFila(), simbolo.getColumna())
            else:
                tablaActual = tablaActual.anterior
        return Excepcion("Semantico", "Variable No encontrada en Asignacion", simbolo.getFila(), simbolo.getColumna())


    def getVariables(self):
        return variables
        
    def vaciarVariables(self):
        global variables
        variables=[]

    def setAmbito(self,ambito):
        self.ambito = ambito

    def getAmbito(self):
        return self.ambito


"""
    Creditos: 
        Jose Francisco Puac - Repositorio del Curso
        Se utilizo como una base para el proyecto
        Eriksson Hern??ndez - Desarollador
"""
