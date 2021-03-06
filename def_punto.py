import turtle as T
from turtle import *
from crea_assi import assi
from tkinter import *

class t_crea_punto:
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
        valore1.set("")
        valore2.set("")
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
    def scritta_punto(self, counter_scritta):
        T.goto(500, -40*counter_scritta+500)
        T.pencolor("black")
        cordinate_punto="{}=({}, {})".format(self.lista[self.counter-1], self.x_pos/10, self.y_pos/10)
        T.write(cordinate_punto, font =("Arial", 20, "normal"))
        

class retta_passante:
    def __init__(self, counter, dizionario):
        self.counter = counter
        self.dizionario = dizionario
    def get_retta(self, valore1, valore2):
        punto1_pos=valore1.get().upper()
        punto2_pos=valore2.get().upper()
        T.penup()
        T.goto(self.dizionario[punto1_pos])
        T.pendown()
        T.pensize(2)
        T.goto(self.dizionario[punto2_pos])
        T.pensize(0)
        


class distanza_punti(retta_passante):
    def __init__(self, counter, dizionario):
        super().__init__(counter, dizionario)
        self.counter=counter
        self.dizionario=dizionario
        self.punto1_pos=""
        self.punto2_pos=""
        self.distanza=0
    def distanza_2_punti(self, valore1, valore2):
        self.punto1_pos=valore1.get().upper()
        self.punto2_pos=valore2.get().upper()
        cordinate_a=self.dizionario[self.punto1_pos]
        x_a=cordinate_a[0]/10
        y_a=cordinate_a[1]/10
        cordinate_b=self.dizionario[self.punto2_pos]
        x_b=cordinate_b[0]/10
        y_b=cordinate_b[1]/10
        self.distanza=(((x_b-x_a)**2)+((y_b-y_a)**2))**(1/2)
    def scritta_distanza(self, counter_scritta):
        T.penup()
        T.goto(500, -40*counter_scritta+500)
        T.pendown()
        T.pencolor("black")
        valore_distanza="{}{}={}".format(self.punto1_pos, self.punto2_pos, self.distanza)
        T.write(valore_distanza, font =("Arial", 20, "normal"))

