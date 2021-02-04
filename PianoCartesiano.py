import turtle as T
from turtle import *
from tkinter import *
from crea_assi import assi
from iterables import *
from def_punto import t_crea_punto, retta_passante, distanza_punti
from def_tk import tk_punto, tk_2_punti

schermo2=Tk()
schermo2.title("Comandi")
schermo2.geometry("100x100")
schermo = T.Screen()
schermo.setup(width = 1.0, height = 1.0)

def delete_widget(widget):
    for elements in widget:
        elements.destroy()

def crea_punto():
    global wid
    delete_widget(wid)
    punto_class=tk_punto(schermo2, x, y, punto, wid)
    punto_class.get_schermo_punto()
    punto_class.get_valori_punto()
    wid=punto_class.button_punto()

def punto():
    global i, i_scritte, d_retta, Alfabeto
    valore_punto=t_crea_punto(i, d_retta, Alfabeto)
    crea_punto_1=valore_punto.get_punto(x, y)
    crea_punto_2=valore_punto.ds_punto()
    crea_punto_scritta=valore_punto.scritta_punto(counter_scritta=i_scritte)
    i=crea_punto_1[0]
    d_retta=crea_punto_1[1]
    i_scritte+=1

def crea_segmento():
    global wid
    delete_widget(wid)
    retta_class=tk_2_punti(schermo2, punto1, punto2, segmento, wid)
    retta_class.get_schermo_2_punti()
    retta_class.get_valori_2_punti()
    wid=retta_class.button_2_punti("Segmento tra 2 punti")

def segmento():
    global i, d_retta
    valore_retta=retta_passante(i, d_retta)
    crea_retta_1=valore_retta.get_retta(punto1, punto2)

def crea_distanza():
    global wid
    delete_widget(wid)
    distanza_class=tk_2_punti(schermo2, punto1, punto2, distanza, wid)
    distanza_class.get_schermo_2_punti()
    distanza_class.get_valori_2_punti()
    wid=distanza_class.button_2_punti("Distanza fra 2 punti")

def distanza():
    global i, i_scritte, d_retta
    val_distanza=distanza_punti(i, d_retta)
    val_distanza.get_retta(punto1, punto2)
    val_distanza.distanza_2_punti(punto1, punto2)
    val_distanza.scritta_distanza(counter_scritta=i_scritte)
    i_scritte+=1

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

menubar = Menu(schermo2)
a=StringVar()
b=StringVar()
creamenu = Menu(menubar, tearoff=0)
creamenu.add_command(label="Crea punto", command=crea_punto)
creamenu.add_command(label="Segmento fra 2 punti", command=crea_segmento)
creamenu.add_command(label="Distanza 2 punti", command=crea_distanza)
#creamenu.add_separator()
#creamenu.add_command(label="reset", command=reset)


menubar.add_cascade(label="Creazione", menu=creamenu)
menubar.add_command(label="Reset", command=reset)
editmenu = Menu(menubar, tearoff=0)
schermo2.config(menu=menubar)
schermo2.mainloop()

#---------------------------------
done()
