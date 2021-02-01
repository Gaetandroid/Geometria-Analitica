import turtle as T
from turtle import *
from tkinter import *

from crea_assi import assi
from iterables import *
from def_punto import crea_punto, retta_passante

schermo2=Tk()
schermo2.title("Comandi")
schermo2.geometry("700x700")

schermo = T.Screen()
schermo.setup(width = 1.0, height = 1.0)

def punto():
    global i, d_retta, Alfabeto
    valore_punto=crea_punto(i, d_retta, Alfabeto)
    crea_punto_1=valore_punto.get_punto(x, y)
    crea_punto_2=valore_punto.ds_punto()
    crea_punto_scritta=valore_punto.scritta_punto()
    i=crea_punto_1[0]
    d_retta=crea_punto_1[1]

def retta():
    global i, d_retta
    valore_retta=retta_passante(i, d_retta)
    crea_retta_1=valore_retta.get_retta(punto1, punto2)

def reset():
    global i, d_retta
    d_retta={}
    i=0
    T.reset()
    assi()
    x.set("")
    y.set("")
    punto1.set("")
    punto2.set("")    

x = StringVar()
y = StringVar()
punto1=StringVar()
punto2=StringVar()

assi()

x_entry=Entry(schermo2, width=3, textvariable=x, font=('verdana', 50))
x_entry.place(height=100, x=5, y=80)
y_entry=Entry(schermo2, width=3, textvariable=y, font=('verdana', 50))
y_entry.place(height=100, x=150, y=80)

punto_1_entry=Entry(schermo2, width=3, textvariable=punto1, font=('verdana', 50))
punto_1_entry.place(height=100, x=5, y=260)
punto_2_entry=Entry(schermo2, width=3, textvariable=punto2, font=('verdana', 50))
punto_2_entry.place(height=100, x=150, y=260)

Button(schermo2, background="green", text="Punto", command=punto, font=('verdana', 32)).place(height=62, x=5, y=5)
Button(schermo2, background="dodgerblue", text="Retta passante per 2 punti", command=retta, font=('verdana', 32)).place(height=62, x=5, y=185)
Button(schermo2, background="red", text="Reset", command=reset, font=('verdana', 32)).place(height=62, x=5, y=365)
#---------------------------------
done()