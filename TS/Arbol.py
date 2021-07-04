import tkinter


class Arbol:
    def __init__(self, instrucciones ):
        self.instrucciones = instrucciones
        self.funciones = []
        self.excepciones = []
        self.consola = ""
        self.salidaTexto = None
        self.TSglobal = None
        self.dot = ""
        self.contador = 0

    def getInstrucciones(self):
        return self.instrucciones

    def setInstrucciones(self, instrucciones):
        self.instrucciones = instrucciones

    def getExcepciones(self):
        return self.excepciones

    def setExcepciones(self, excepciones):
        self.excepciones = excepciones

    def getConsola(self):
        return self.consola
    
    def setConsola(self, consola):
        self.consola = consola

    def updateConsola(self,cadena):
        self.consola += str(cadena) + '\n'

    def getTSGlobal(self):
        return self.TSglobal
    
    def setTSglobal(self, TSglobal):
        self.TSglobal = TSglobal

    def getFunciones(self):
        return self.funciones

    def getFuncion(self, nombre):
        for funcion in self.funciones:
            if funcion.nombre == nombre:
                return funcion
        return None
    
    def addFuncion(self, funcion):
        self.funciones.append(funcion)

    def getSalidaTexto(self):
        return self.salidaTexto

    def setSalidaTexto(self, salidaTexto):
        self.salidaTexto = salidaTexto

    def imprimirErrores(self, tablaErrores):
        for limpieza in tablaErrores.get_children():
            tablaErrores.delete(limpieza)

        i = 1
        for error in self.excepciones:                   #CAPTURA DE ERRORES LEXICOS Y SINTACTICOS
            tablaErrores.insert("",tkinter.END,text = i,value = [i,error.tipo, error.descripcion, error.fila, error.columna])
            i = i + 1


    def getDot(self, raiz): ## DEVUELVE EL STRING DE LA GRAFICA EN GRAPHVIZ
        self.dot = ""
        self.dot += "digraph {\n"
        self.dot += "n0[label=\"" + raiz.getValor().replace("\"", "\\\"") + "\"];\n"
        self.contador = 1
        self.recorrerAST("n0", raiz)
        self.dot += "}"
        return self.dot

    def recorrerAST(self, idPadre, nodoPadre):
        for hijo in nodoPadre.getHijos():
            nombreHijo = "n" + str(self.contador)
            self.dot += nombreHijo + "[label=\"" + hijo.getValor().replace("\"", "\\\"") + "\"];\n"
            self.dot += idPadre + "->" + nombreHijo + ";\n"
            self.contador += 1
            self.recorrerAST(nombreHijo, hijo)  
"""
    Creditos: 
        Jose Francisco Puac - Repositorio del Curso
        Se utilizo como una base para el proyecto
        Eriksson Hernández - Desarollador
"""