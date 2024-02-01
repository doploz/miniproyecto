from tkinter import *

def miFuncion():
    print("Este mensaje es de julian")

ventana = Tk()
ventana.title("Hola mundo")
ventana.geometry("400x200")

lbl = Label(ventana, text="ESte es un Label")
lbl.pack()

btn = Button(ventana, fg="blue", bg = "orange",text="Presionar",command = miFuncion)
btn.place(relx=0.1,rely=0.1,relwidth=10,height=10)

ventana.mainloop()

