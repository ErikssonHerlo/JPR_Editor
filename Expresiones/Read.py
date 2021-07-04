from Abstract.NodoAST import NodoAST
from Abstract.Instruccion import Instruccion
from TS.Tipo import TIPO


import tkinter as tk
from tkinter import simpledialog

class Read(Instruccion):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna
        self.tipo = TIPO.CADENA

    def interpretar(self, tree, table):
        tree.getSalidaTexto().insert('insert', tree.getConsola())
        tree.getSalidaTexto().see('end')
        
        entradaRead = simpledialog.askstring("Entrada de Texto","Ingrese un valor")



        tree.getSalidaTexto().delete('1.0', 'end')
        tree.updateConsola('Entrada: ' + entradaRead)
        return entradaRead

    def getNodo(self):
        nodo = NodoAST("READ")
        return nodo 

"""
    Creditos: 
        Jose Francisco Puac - Repositorio del Curso
        Se utilizo como una base para el proyecto
        Eriksson Hernández - Desarollador
"""