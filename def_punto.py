import turtle as T
from turtle import *
from crea_assi import assi
from tkinter import *

class crea_punto:
    def __init__(self, counter, dizionario, lista):
        self.counter=counter
        self.dizionario=dizionario
        self.lista=lista
        self.x_pos=0
        self.y_pos=0
    
    def get_punto(self, valore1, valore2):
        self.x_pos = float(valore1.get())
        self.y_pos = float(valore2.get())
        self.x_pos*=10
        self.y_pos*=10
        self.dizionario[self.lista[self.counter]] =(self.x_pos, self.y_pos)
        self.counter+=1
        return self.counter, self.dizionario

    def ds_punto(self):
        T.penup()
        T.goto(self.x_pos, self.y_pos)
        T.dot()
        T.write(self.lista[self.counter-1], font=("Arial", 12, "normal"))
        if self.counter > 25:
            self.counter = 0 
        T.pencolor("red")
        T.pendown()
        T.goto(self.x_pos, 0)
        T.pencolor("black")
        T.write(self.x_pos/10, font=("Arial", 12, "normal"))
        T.penup()
        T.goto(self.x_pos, self.y_pos)
        T.pendown()
        T.pencolor("red")
        T.goto(0, self.y_pos)
        T.pencolor("black")
        T.write(self.y_pos/10, font =("Arial", 12, "normal"))
        T.penup()