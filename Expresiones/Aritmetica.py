#from Abstract.Instruccion import Instruccion
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import TIPO, OperadorAritmetico

class Aritmetica(Instruccion):
    def __init__(self, operador, OperacionIzq, OperacionDer, fila, columna):
        self.operador = operador
        self.OperacionIzq = OperacionIzq
        self.OperacionDer = OperacionDer
        self.fila = fila
        self.columna = columna
        self.tipo = None

    
    def interpretar(self, tree, table):
        izq = self.OperacionIzq.interpretar(tree, table)
        if isinstance(izq, Excepcion): return izq
        if self.OperacionDer != None  and self.OperacionDer!="++"  and self.OperacionDer!="--":
            der = self.OperacionDer.interpretar(tree, table)
            if isinstance(der, Excepcion): return der

        #SUMA
        if self.operador == OperadorAritmetico.MAS: 
            if (self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO) or (self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.BOOLEANO) or (self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.ENTERO) or (self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.BOOLEANO):
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif (self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL) or (self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO) or (self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL) or (self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.BOOLEANO) or (self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.DECIMAL):
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) + self.obtenerVal(self.OperacionDer.tipo, der)
            elif (self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.CADENA) or (self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.CADENA) or (self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.CADENA)  or (self.OperacionIzq.tipo == TIPO.CARACTER and self.OperacionDer.tipo == TIPO.CARACTER)  or (self.OperacionIzq.tipo == TIPO.CARACTER and self.OperacionDer.tipo == TIPO.CADENA) or (self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.ENTERO) or (self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.DECIMAL) or (self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.BOOLEANO) or (self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.CARACTER) or (self.OperacionIzq.tipo == TIPO.CADENA and self.OperacionDer.tipo == TIPO.CADENA):
                self.tipo = TIPO.CADENA
                return str(self.obtenerVal(self.OperacionIzq.tipo, izq)) + str(self.obtenerVal(self.OperacionDer.tipo, der))
            return Excepcion("Semantico", "Tipo Erroneo de operacion para Suma (+).", self.fila, self.columna)
        
        #RESTA
        elif self.operador == OperadorAritmetico.MENOS:
            if (self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO) or (self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.BOOLEANO) or (self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.ENTERO):
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            elif (self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL) or (self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL) or (self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO) or (self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.BOOLEANO) or (self.OperacionIzq.tipo == TIPO.BOOLEANO and self.OperacionDer.tipo == TIPO.DECIMAL):
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) - self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para Resta (-).", self.fila, self.columna)
        
        #MULTIPLICACION
        elif self.operador == OperadorAritmetico.POR:
            if (self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO):
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)
            elif (self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL) or (self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO) or (self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL):
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) * self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para Multiplicacion (*).", self.fila, self.columna)
        
        #DIVISION
        elif self.operador == OperadorAritmetico.DIV:
            if(self.obtenerVal(self.OperacionDer.tipo, der) == 0):
                return Excepcion("Semantico", "No se puede realizar una Division entre cero.", self.fila, self.columna)
            elif (self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO) or (self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL) or (self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO) or (self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL):
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) / self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para Division (/).", self.fila, self.columna)
        
        #POTENCIA
        elif self.operador == OperadorAritmetico.POT: 
            if (self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO):
                self.tipo = TIPO.ENTERO
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)
            elif (self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL) or (self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO) or (self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL):
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) ** self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para Potencia (**).", self.fila, self.columna)
        
        #MODULO/RESIDUO
        elif self.operador == OperadorAritmetico.MOD: 
            if (self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.ENTERO) or (self.OperacionIzq.tipo == TIPO.ENTERO and self.OperacionDer.tipo == TIPO.DECIMAL) or (self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.ENTERO) or (self.OperacionIzq.tipo == TIPO.DECIMAL and self.OperacionDer.tipo == TIPO.DECIMAL):
                self.tipo = TIPO.DECIMAL
                return self.obtenerVal(self.OperacionIzq.tipo, izq) % self.obtenerVal(self.OperacionDer.tipo, der)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para Modulo (%).", self.fila, self.columna)
        
        #NEGACION UNARIA
        elif self.operador == OperadorAritmetico.UMENOS: 
            if self.OperacionIzq.tipo == TIPO.ENTERO:
                self.tipo = TIPO.ENTERO
                return - self.obtenerVal(self.OperacionIzq.tipo, izq)
            elif self.OperacionIzq.tipo == TIPO.DECIMAL:
                self.tipo = TIPO.DECIMAL
                return - self.obtenerVal(self.OperacionIzq.tipo, izq)
            return Excepcion("Semantico", "Tipo Erroneo de operacion para Negacion Unaria (-).", self.fila, self.columna)
        
        #INCREMENTO
        elif self.operador == OperadorAritmetico.INCREMENTO:  
            if (self.OperacionIzq.tipo == TIPO.ENTERO ):
                self.tipo = TIPO.ENTERO
                print(self.obtenerVal(self.OperacionIzq.tipo, izq))
                return self.obtenerVal(self.OperacionIzq.tipo, izq) +1
            elif (self.OperacionIzq.tipo == TIPO.DECIMAL):
                self.tipo = TIPO.DECIMAL
                print(self.obtenerVal(self.OperacionIzq.tipo,izq))
                return self.obtenerVal(self.OperacionIzq.tipo,izq) +1
            return Excepcion("Semantico", "Tipo Erroneo de operacion para Incremento (++).", self.fila, self.columna)
        
        #DECREMENTO
        elif self.operador == OperadorAritmetico.DECREMENTO:         
            if (self.OperacionIzq.tipo == TIPO.ENTERO ):
                self.tipo = TIPO.ENTERO
                print(self.obtenerVal(self.OperacionIzq.tipo, izq))
                return self.obtenerVal(self.OperacionIzq.tipo, izq) -1
            elif (self.OperacionIzq.tipo == TIPO.DECIMAL):
                self.tipo = TIPO.DECIMAL
                print(self.obtenerVal(self.OperacionIzq.tipo,izq))
                return self.obtenerVal(self.OperacionIzq.tipo,izq) -1
            return Excepcion("Semantico", "Tipo Erroneo de operacion para Decremento (--).", self.fila, self.columna)
        
        return Excepcion("Semantico", "Tipo de Operacion no Especificado.", self.fila, self.columna)


    def obtenerVal(self, tipo, val):
        if tipo == TIPO.ENTERO:
            return int(val)
        elif tipo == TIPO.DECIMAL:
            return float(val)
        elif tipo == TIPO.BOOLEANO:
            return bool(val)
        return str(val)
        