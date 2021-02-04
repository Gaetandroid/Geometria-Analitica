from tkinter import *

class tk_punto:
    def __init__(self, schermo, variabile_1, variabile_2, funzione, insieme_widget):
        self.schermo=schermo
        self.variabile_1=variabile_1
        self.variabile_2=variabile_2
        self.funzione=funzione
        self.insieme_widget=insieme_widget
    def get_schermo_punto(self):
        self.schermo.title("Comandi")
        self.schermo.geometry("300x300")
    def get_valori_punto(self):
        x_entry=Entry(self.schermo, width=3, textvariable=self.variabile_1, font=('verdana', 50))
        x_entry.place(height=100, x=5, y=80)
        y_entry=Entry(self.schermo, width=3, textvariable=self.variabile_2, font=('verdana', 50))
        y_entry.place(height=100, x=150, y=80)
        self.insieme_widget=[x_entry, y_entry]
    def button_punto(self):
        button=Button(self.schermo, background="green", text="Punto", command=self.funzione, font=('verdana', 32))
        button.place(height=62, x=5, y=5)
        self.insieme_widget.append(button)
        return self.insieme_widget

class tk_2_punti:
    def __init__(self, schermo,  variabile_1, variabile_2, funzione, insieme_widget):
        self.schermo=schermo
        self.variabile_1=variabile_1
        self.variabile_2=variabile_2
        self.funzione=funzione
        self.insieme_widget=insieme_widget
    def get_schermo_2_punti(self):
        self.schermo.title("Comandi")
        self.schermo.geometry("550x300")
    def get_valori_2_punti(self):
        punto_1_entry=Entry(self.schermo, width=3, textvariable=self.variabile_1, font=('verdana', 50))
        punto_1_entry.place(height=100, x=5, y=80)
        punto_2_entry=Entry(self.schermo, width=3, textvariable=self.variabile_2, font=('verdana', 50))
        punto_2_entry.place(height=100, x=150, y=80)
        self.insieme_widget=[punto_1_entry, punto_2_entry]
    def button_2_punti(self, testo):
        button=Button(self.schermo, background="dodgerblue", text=testo, command=self.funzione, font=('verdana', 32))
        button.place(height=62, x=5, y=5)
        self.insieme_widget.append(button)
        return self.insieme_widget        