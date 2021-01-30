import turtle as T
from turtle import *
from crea_assi import assi
from tkinter import *
#---------------------------------
#def

def punto():
    global i, Alfabeto, d_retta
    x_pos = int(x.get())
    y_pos = int(y.get())
    x_pos*=10
    y_pos*=10
    T.penup()
    T.goto(x_pos,y_pos)
    T.dot()
    T.write(Alfabeto[i],font=("Arial",12,"normal"))
    if i > 25:
        i = 0 
    T.pencolor("red")
    T.pendown()
    T.goto(x_pos, 0)
    T.pencolor("black")
    T.write(x_pos/10,font=("Arial",12,"normal"))
    T.penup()
    T.goto(x_pos, y_pos)
    T.pendown()
    T.pencolor("red")
    T.goto(0, y_pos)
    T.pencolor("black")
    T.write(y_pos/10,font =("Arial",12,"normal"))
    d_retta[Alfabeto[i]] = (x_pos, y_pos)
    i += 1

def retta():
    global Alfabeto, d_retta, i
    punto1_pos=punto1.get().upper()
    punto2_pos=punto2.get().upper()
    T.penup()
    T.goto(d_retta[punto1_pos])
    T.pendown()
    T.goto(d_retta[punto2_pos])

def return_to_axes():
    T.reset()
    assi()
#---------------------------------
#Schermi
schermo2=Tk()
schermo2.title("Comandi")
schermo2.geometry("700x700")

schermo = T.Screen()
schermo.setup(width = 1.0, height = 1.0)
#---------------------------------
#Tk
x = StringVar()
y = StringVar()
punto1=StringVar()
punto2=StringVar()

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
Button(schermo2, background="red", text="Reset", command=return_to_axes, font=('verdana', 32)).place(height=62, x=5, y=365)
#---------------------------------
#Creazione assi cartesiani
assi()
#---------------------------------
#Iterables
d_retta = {}
Alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
i = 0
#---------------------------------
#notes
#sotto i button i blocchi vanno messi di +75y
#sotto le entry i blocchi vanno messi di +105y
#---------------------------------
done()