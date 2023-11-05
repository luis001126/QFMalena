import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import Menu
from tkinter import messagebox as mBox 

def acciones():
    seleccion = lista.current()
    if seleccion == 0:
        import benceno
    else:
        import tolueno

def Salir():
    root.destroy()
    root.quit()

def mensaje1():
    mBox.showinfo('Funcionamiento :',
    'Paso1: Seleccionar la sustancia quimica a calcular, '
    'Paso2: pinchar el boton de CALCULAR '
    'Paso3: Leer los resultados en la ventana emergente '
    'Paso4: Pinchar el boton <--SALIR--> para cerrar la ventana.')

def mensaje2():
    mBox.showinfo(title="Referencia",
                  message="Este programa fue diseñado por Luis Alexis Rojas Rondan"
                          "para Malena Arias Muñoz, para mas informacion pongase en contacto por "
                          "medio de el siguinte correo electrónico: luisalexisrojasrondan@gmail.com ")




root = Tk()
root.title('Calculo de propiedades de Q-F')
root.geometry('400x300')
root.resizable(0,0)

#fondo de pantalla
imagen = PhotoImage(file='foto1.png')
Label(root,image=imagen,bd=12).pack()

#Menu
barramenu = Menu(root)
root.config(menu=barramenu)
ayuda=Menu(barramenu, tearoff=0)
ayuda.add_command(label="Ayuda",command=mensaje1)
ayuda.add_separator()
ayuda.add_command(label="Refrencias",command=mensaje2)
barramenu.add_cascade(label="Acerca de: ", menu=ayuda)

#Creacion de una etiqueta para la seleccion de las sustancias quimicas
var1 = StringVar()
var1.set("Seleccione la sustancia quimica :")
label1 = Label(root,textvariable=var1,height = 2)
label1.place(x=0,y=100)

#primera lista despl
lista = ttk.Combobox(state='readonly',values=['Benceno [C6H6]','Tolueno [C6H5CH3]'],width=20)
lista.place(x=200,y=108)
lista.current(0)
#boton 1

boton1 = Button(root, text = "CALCULAR",width=15, command=acciones)
boton1.place(x=50,y=250)

#Boton para salir

boton2=Button(root,text="<--SALIR-->",command=Salir)
boton2.place(x=250, y= 250)

root.mainloop()
