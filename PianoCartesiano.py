#import
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
x_entry.place(height=100, x=5, y=100)
y_entry=Entry(schermo2, width=3, textvariable=y, font=('verdana', 50))
y_entry.place(height=100, x=150, y=100)

punto_1_entry=Entry(schermo2, width=3, textvariable=punto1, font=('verdana', 50))
punto_1_entry.place(height=100, x=5, y=300)
punto_2_entry=Entry(schermo2, width=3, textvariable=punto2, font=('verdana', 50))
punto_2_entry.place(height=100, x=150, y=300)

Button(schermo2, text="Punto", command=punto, font=('verdana', 32)).place(height=62, x=5, y=5)
Button(schermo2, text="Retta passante per 2 punti", command=retta, font=('verdana', 32)).place(height=62, x=5, y=210)
#---------------------------------
#Creazione assi cartesiani
assi()
#---------------------------------
d_retta = {}
Alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
i = 0
T.pendown()
T.onscreenclick(T.goto)
#---------------------------------
#fine
done()