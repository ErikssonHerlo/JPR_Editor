
class Simbolo:
    def __init__(self, identificador, tipo, fila, columna, valor ):
        self.id = identificador
        self.ambito = None
        self.tipo = tipo
        self.fila = fila
        self.columna = columna
        self.valor = valor

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
        self.ambito
    
    def getAmbito(self):
        return self.ambito

"""
    Creditos: 
        Jose Francisco Puac - Repositorio del Curso
        Se utilizo como una base para el proyecto
        Eriksson Hernández - Desarollador
"""