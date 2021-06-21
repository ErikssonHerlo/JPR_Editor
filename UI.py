
# Imports
import os
import re
from tkinter import filedialog
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
from grammar import interfaz as compilar

# ******************************************* METODOS ********************************************
# Actualizar lineas
def lineas(*args):
    lineasEditor.delete("all")

    cont = entradaTexto.index("@1,0")
    while True:
        dline = entradaTexto.dlineinfo(cont)
        if dline is None:
            break
        y = dline[1]
        strline = str(cont).split(".")[0]
        lineasEditor.create_text(2, y, anchor="nw", text=strline,
                          font=("Consolas", 10))
        cont = entradaTexto.index("%s+1line" % cont)

# Actualizar posicion
def posicion(event=None):
    actualizarArchivoLbl()
    posicionFilaColumna.config(
        text="Fila: " + str(entradaTexto.index(INSERT)).replace(".", ", Columna: "))

# Llamar metodos
def actualizarLineas(event):
    posicion()
    lineas()

#Actualizar label del archivo modificado
def actualizarArchivoLbl():
    text_archivo = archivoNombre.cget("text") 
    last_char = text_archivo[-1]
    if last_char != "*":
        archivoNombre.config(text = archivoNombre.cget("text")+"*")

#Actualizar label de archivo guardado
def actualizarArchivoLblGuardar():
    text_archivo = archivoNombre.cget("text") 
    last_char = text_archivo[-1]
    if last_char == "*" and archivo != "":
        archivoNombre.config(text = archivo)

def recorrerInput(i):  
    lista = []
    val = ''
    counter = 0
    while counter < len(i):
            if re.search(r'[a-z|0-9|.|A-Z]', i[counter]):
                val += i[counter]
            elif i[counter] == "\"":
                if len(val) != 0:
                    l = []
                    l.append("cadena")
                    l.append(val)
                    lista.append(l)
                    val = ''
                val = i[counter]
                counter += 1

                while counter < len(i):
                    if i[counter] == "\"":
                        val += i[counter]
                        l = []
                        l.append("cadena")
                        l.append(val)
                        lista.append(l)
                        val = ''
                        break
                    val += i[counter]
                    counter += 1
            elif i[counter] == "#":
                if len(val) != 0:
                    l = []
                    l.append("comentario")
                    l.append(val)
                    lista.append(l)
                    val = ''
                val = i[counter]
                counter += 1
                if i[counter] == "*":
                   while counter < len(i):
                        if i[counter] == "#":
                            val += i[counter]
                            l = []
                            l.append("comentario")
                            l.append(val)
                            lista.append(l)
                            val = ''
                            break
                        val += i[counter]
                        counter += 1 
                else:    
                    while counter < len(i):
                        if i[counter] == "\n":
                            val += i[counter]
                            l = []
                            l.append("comentario")
                            l.append(val)
                            lista.append(l)
                            val = ''
                            break
                        val += i[counter]
                        counter += 1
            elif i[counter] == "\'":
                if len(val) != 0:
                    l = []
                    l.append("variable")
                    l.append(val)
                    lista.append(l)
                    val = ''
                val = i[counter]
                counter += 1
                while counter < len(i):
                    if i[counter] == "\'":
                        val += i[counter]
                        l = []
                        l.append("cadena")
                        l.append(val)
                        lista.append(l)
                        val = ''
                        break
                    val += i[counter]
                    counter += 1
            else:
                if len(val) != 0:
                    l = []
                    l.append("variable")
                    l.append(val)
                    lista.append(l)
                    val = ''
                l = []
                l.append("normal")
                l.append(i[counter])
                lista.append(l)
            counter +=1
    for s in lista:
        if s[1] == 'var' or s[1] == 'func' or s[1] == 'read' or s[1] == 'tolower' or s[1] == 'toupper' or s[1] == 'lenght' or s[1] == 'truncate' or s[1] == 'round' or s[1] == 'typeof' or s[1] == 'return' or s[1] == 'break' or s[1] == 'switch' or s[1] == 'case' or s[1] == 'default' or s[1] == 'false' or s[1] == 'true' or s[1] == 'while' or s[1] == 'for' or s[1] == 'continue' or  s[1] == 'else' or s[1] == 'if' or s[1] == 'null' or s[1] == 'boolean' or s[1] == 'string' or s[1] == 'int' or s[1] == 'double' or s[1] == 'char' or s[1] == 'print' or s[1] == 'main':
            s[0] = 'reservada'
        elif re.search(r'\d+',s[1]) or re.search(r'\d+\.\d+',s[1]):
            if re.search(r'\"(\\\'|\\"|\\\\|\\n|\\t|[^\'\\\"])*?\"',s[1]):
                s[0] = 'cadena'
            elif re.search(r'\#\*(.|\n)*?\*\#|\#.*\n',s[1]):
                s[0] = 'comentario'
            elif re.search(r'[a-z|A-Z]',s[1]):
                s[0]= "normal"
            else:
                s[0] = 'numero'
        elif re.search(r'\"(\\\'|\\"|\\\\|\\n|\\t|[^\'\\\"])*?\"',s[1]):
            s[0] = 'cadena'
        elif re.search(r'\#\*(.|\n)*?\*\#|\#.*\n',s[1]):
            s[0] = 'comentario'
    return lista        


def resaltarPalabras():
    contenido = entradaTexto.get(1.0, END)
    entradaTexto.delete(1.0, "end")
    for s in recorrerInput(contenido):
        entradaTexto.insert(INSERT, s[1], s[0])


#Path del archivo en memoria
archivo=""


#Abrir archivo
def abrir():       
    global archivo
    archivo = filedialog.askopenfilename(title = "Abrir Archivo", initialdir = "C:/",filetypes=[("jpr files", ".jpr")])
    entrada = open(archivo)
    content = entrada.read()
    entradaTexto.delete(1.0, END)
    entradaTexto.insert(INSERT, content)
    entrada.close()
    lineas()
    archivoNombre.config(text = archivo)
    resaltarPalabras()



#Nuevo archivo
def nuevoArchivo(e = None):   
    global archivo
    entradaTexto.delete(1.0, END)
    archivo = ""
    archivoNombre.config(text = "Archivo sin guardar")
    resaltarPalabras()

#Guardar archivo
def guardarArchivo():    
    global archivo
    if archivo == "":
        guardarComo()
    else:
        guardarc = open(archivo, "w")
        guardarc.write(entradaTexto.get(1.0, END))
        guardarc.close()
        actualizarArchivoLblGuardar()
        resaltarPalabras

#Guardar como archivo
def guardarComo():      #GUARDAR COMO
    global archivo
    guardar = filedialog.asksaveasfilename(title = "Guardar Archivo", initialdir = "C:/",filetypes=[("jpr files", ".jpr")],defaultextension='.jpr')
    fguardar = open(guardar, "w+")
    fguardar.write(entradaTexto.get(1.0, END))
    fguardar.close()
    archivo = guardar
    archivoNombre.config(text = guardar)
    actualizarArchivoLblGuardar()
    resaltarPalabras()

#Compilacion
def compilarArchivo(e = None):
    consolaTexto.delete(1.0, END)
    contenido = compilar(entradaTexto.get(1.0, END),tablaErrores)
    consolaTexto.insert(INSERT,contenido)
    resaltarPalabras()


# ******************************************* COMPONENTES ********************************************

#-----------------------------------------Declaracion del tk
root = Tk()
root.title("JPR Editor")
# Frame principal
frame = Frame(root, bg="#331e91")
frame.grid(sticky='news')
# Canvas
canvas = Canvas(frame, bg="#331e91")
canvas.grid(row=0, column=1)
# Frame del canvas
frameEditors = Frame(canvas, bg="#331e91")
canvas.create_window((0, 0), window=frameEditors, anchor="nw")
#canvas.columnconfigure()
canvas.configure(width=1450, height=750)

#------------------------------------Componentes de la Interfaz

# Barra del Menu
menu = Menu(frameEditors)
nuevoItem = Menu(menu,tearoff=0)
nuevoItem.add_command(label='Nuevo',command=nuevoArchivo)
nuevoItem.add_command(label='Abrir',command=abrir)
nuevoItem.add_command(label='Guardar',command=guardarArchivo)
nuevoItem.add_command(label='Guardar como',command=guardarComo)
menu.add_cascade(label='Archivo', menu=nuevoItem)
nuevoItem1 = Menu(menu,tearoff=0)
nuevoItem1.add_command(label='Compilar',command=compilarArchivo)
nuevoItem1.add_command(label='Debug',command=abrir)
menu.add_cascade(label='Herramientas', menu=nuevoItem1)
nuevoItem2 = Menu(menu,tearoff=0)
nuevoItem2.add_command(label='Reporte de Errores',command=compilarArchivo)
nuevoItem2.add_command(label='Arbol Sintactico',command=abrir)
menu.add_cascade(label='Reportes', menu=nuevoItem1)
root.config(menu=menu)

#---------------------------Titulos
tituloPrincipal = Label(frameEditors,text="JPR Interprete",font="Helvetica 18",fg="black")
tituloPrincipal.grid(row=0,column=0,sticky="e",pady=10)
#tituloPrincipal.place(x=605, y = 8015, width=, height=64)
tituloEditor = Label(frameEditors,text="Editor",font="Helvetica 18",fg="black")
tituloEditor.grid(row=1,column=0,sticky="ew",pady=10)
tituloConsola = Label(frameEditors,text="Consola",font="Helvetica 18",fg="black")
tituloConsola.grid(row=1,column=1,sticky="ew",pady=10)
#Label Tabla de Simbolos
simbolosLbl = Label(frameEditors,text="Tabla de Simbolos",font="Helvetica 18",fg="black")
simbolosLbl.grid(row=5,column=0,sticky="ew",pady=30)
#Label Tabla de Errores
erroresLbl = Label(frameEditors,text="Tabla de Errores",font="Helvetica 18",fg="black")
erroresLbl.grid(row=5,column=1, sticky="ew")
#Boton de compilacion
#compilarButton= Button(frameEditors,text="Compilar",width=10,command=compilarArchivo)
#compilarButton.grid(row=1,column=0,sticky="s")


#Label Ubicacion / Nombre del Archivo
tituloArchivo= Label(frameEditors, text="Nombre del Archivo:",width=17,background="snow",fg="gray9")
tituloArchivo.grid(column=0, row=2,sticky="nw",padx=25)
archivoNombre= Label(frameEditors, text="Archivo sin guardar",width=47,background="snow",fg="gray9")
archivoNombre.place(x=170, y = 105, width=510, height=20)
#archivoLbl.grid(column=1, row=2,sticky="nw",padx=55)

# Label de Posicion Fila, Columna
tituloPosicion= Label(frameEditors, text="Posición del Cursor:",width=47,background="snow",fg="gray9")
tituloPosicion.place(x=350, y = 438, width=150, height=20)
posicionFilaColumna= Label(frameEditors, text="Fila: 0, Columna: 0",width=20,background="white",fg="#0d51cf")
posicionFilaColumna.grid(column=0, row=2,sticky="se",padx=55)
# ScrolledText de entrada
entradaTexto = scrolledtext.ScrolledText(frameEditors, undo=True, width=75, height=17)
entradaTexto.grid(column=0, row=2, pady=30, padx=60)
# ScrolledText de la consola
consolaTexto = scrolledtext.ScrolledText(frameEditors, undo=True, width=75, height=17,bg="black",foreground="white")
consolaTexto.grid(column=1, row=2, pady=30, padx=50)
# Canvas de fila del editor
lineasEditor = Canvas(frameEditors, width=30, height=293, background='#8076ee') #gray60 #7366ff
lineasEditor.grid(column=0, row=2,padx=25,sticky="w")



#Colores de las Palabras Reservadas
entradaTexto.tag_config('reservada' , foreground='blue')
entradaTexto.tag_config('cadena'    , foreground='#ff5500')
entradaTexto.tag_config('numero'    , foreground='#C90FF2')#C90FF2
entradaTexto.tag_config('comentario', foreground='gray')
entradaTexto.tag_config('variable'  , foreground='green')
entradaTexto.tag_config('operacion' , foreground='red')
entradaTexto.tag_config('signo'     , foreground='green')

#Boton Label de Compilacion

imagenCompilar = PhotoImage(file = "./Resources/Ejecutar2.png")
imagenCompilar.configure(width=64)
compilarLabel = Label(frameEditors,image = imagenCompilar,bg="white",width=50)
compilarLabel.config(cursor="hand1")
compilarLabel.place(x=705, y = 215, width=64, height=64)
#compilarLabel.grid(row=2,column=0,sticky="s")
compilarLabel.bind("<Button>",compilarArchivo)



#Tabla De Simbolos en la UI
tablaSimbolosUI=ttk.Treeview(frameEditors,height=7)
tablaSimbolosUI['columns']=('#', 'Identificador', 'Tipo', 'Dimension', 'Valor', 'Ambito', 'Referencias')
tablaSimbolosUI.column('#0', width=0, stretch=NO)
tablaSimbolosUI.column('#', anchor=CENTER, width=10)
tablaSimbolosUI.column('Identificador', anchor=CENTER, width=110)
tablaSimbolosUI.column('Tipo', anchor=CENTER, width=80)
tablaSimbolosUI.column('Dimension', anchor=CENTER, width=110)
tablaSimbolosUI.column('Valor', anchor=CENTER, width=80)
tablaSimbolosUI.column('Ambito', anchor=CENTER, width=80)
tablaSimbolosUI.column('Referencias', anchor=CENTER, width=110) 
tablaSimbolosUI.heading('#0', text='', anchor=CENTER)
tablaSimbolosUI.heading('#', text='#', anchor=CENTER)
tablaSimbolosUI.heading('Identificador', text='Identificador', anchor=CENTER)
tablaSimbolosUI.heading('Tipo', text='Tipo', anchor=CENTER)
tablaSimbolosUI.heading('Dimension', text='Dimension', anchor=CENTER)
tablaSimbolosUI.heading('Valor', text='Valor', anchor=CENTER)
tablaSimbolosUI.heading('Ambito', text='Ambito', anchor=CENTER)
tablaSimbolosUI.heading('Referencias', text='Referencias', anchor=CENTER)
tablaSimbolosUI.grid(column=0, row=6,padx=25,sticky="ew")

#--------Tabla Reporte de ERRORES
tablaErrores=ttk.Treeview(frameEditors,height=7)
tablaErrores['columns']=('#', 'Tipo', 'Descripcion', 'Linea', 'Columna')
tablaErrores.column('#0', width=0, stretch=NO)
tablaErrores.column('#', anchor=CENTER, width=20, stretch=NO)
tablaErrores.column('Tipo', anchor=CENTER, width=100)
tablaErrores.column('Descripcion', anchor=CENTER, width=350)
tablaErrores.column('Linea', anchor=CENTER, width=90)
tablaErrores.column('Columna', anchor=CENTER, width=100)
tablaErrores.heading('#0', text='', anchor=CENTER)
tablaErrores.heading('#', text='#', anchor=CENTER)
tablaErrores.heading('Tipo', text='Tipo', anchor=CENTER)
tablaErrores.heading('Descripcion', text='Descripcion', anchor=CENTER)
tablaErrores.heading('Linea', text='Linea', anchor=CENTER)
tablaErrores.heading('Columna', text='Columna', anchor=CENTER)
tablaErrores.grid(row=6,column=1)



# Acciones del teclado para el Editor
entradaTexto.bind('<Return>', actualizarLineas)
entradaTexto.bind('<BackSpace>', actualizarLineas)
entradaTexto.bind('<<Change>>', actualizarLineas)
entradaTexto.bind('<Configure>', actualizarLineas)
entradaTexto.bind('<Motion>', actualizarLineas)
entradaTexto.bind('<KeyPress>', posicion)
entradaTexto.bind('<Button>', posicion)
entradaTexto.bind('<Key>', actualizarLineas)
entradaTexto.bind('<Enter>', actualizarLineas)


# Main loop
root.mainloop()

"""
Creditos: 
    Jose Francisco Puac - Repositorio del Curso
    Se utilizo como una base para el proyecto
    Eriksson Hernández - Desarollador
"""