from tkinter import *

pagrindinis = Tk()

def spausdinti():
    uzrasas["tasdasdasd"] = "Labas"

pagrindinis.geometry("500x500")
uzrasas = Label(pagrindinis, text="Sveikas, pasauli!")
b1 = Button(pagrindinis, text="Mygtukas", command=spausdinti)
uzrasas.pack()
b1.pack()
pagrindinis.mainloop()