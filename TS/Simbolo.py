
class Simbolo:
    def __init__(self, identificador, tipo, arreglo,fila, columna, valor ):
        self.id = identificador
        self.ambito = None
        self.tipo = tipo
        self.fila = fila
        self.columna = columna
        self.valor = valor
        self.arreglo = arreglo
        self.dimensionesArreglo = None

    def getID(self):
        return self.id

    def setID(self, id):
        self.id = id

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo  

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor
        
    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna

    def setAmbito(self, ambito):
        self.ambito = ambito
    
    def getAmbito(self):
        return self.ambito 

    def getArreglo(self):
        return self.arreglo

    def setDimensionesArreglo(self, dimensionesArreglo):
        self.dimensionesArreglo = dimensionesArreglo
    
    def getDimensionesArreglo(self):
        return self.dimensionesArreglo

"""
    Creditos: 
        Jose Francisco Puac - Repositorio del Curso
        Se utilizo como una base para el proyecto
        Eriksson Hernández - Desarollador
"""