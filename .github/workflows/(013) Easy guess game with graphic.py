from tkinter import *
import random
t = Tk()
t.title("wybierz guzik")
t.geometry("300x350")

def wstaw_przyciski():
    ile_przycisków = 8
    global przyciski #numbers of button for all program
    przyciski = []
    dobry = random.randint (0,ile_przycisków-1)
    for i in range (ile_przycisków): 
        if i == dobry:
            przyciski.append(Button(t,text = "kliknij mnie",command=trafiony)) #if the answer is right the massage will be trafiony
        else:
            przyciski.append(Button(t,text = "kliknij mnie",command=pudlo))
    for i in przyciski:
        i.pack(fill=BOTH,expand=YES)



def trafiony():
    for i in przyciski:
        i.destroy()
    global etykieta
    etykieta = Label(t, text = "Trafiłeś!")
    etykieta.pack(fill=BOTH,expand=YES)
    t.after(5000,restart) #reset game afte 5000ms

def restart ():
    etykieta.destroy()
    wstaw_przyciski()

def pudlo():
    for i in przyciski:
        i.destroy()
    global etykieta
    etykieta = Label(t, text = "Trafiłeś zle!")
    etykieta.pack(fill=BOTH,expand=YES)
    t.after(5000,restart)

wstaw_przyciski()
