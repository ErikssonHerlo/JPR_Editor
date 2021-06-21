from abc import ABC, abstractmethod

class Instruccion(ABC):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        super().__init__()

    @abstractmethod
    def interpretar(self, tree, table):
        pass

"""
    Creditos: 
        Jose Francisco Puac - Repositorio del Curso
        Se utilizo como una base para el proyecto
        Eriksson Hernández - Desarollador
"""