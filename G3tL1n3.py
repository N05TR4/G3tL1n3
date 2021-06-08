from tkinter import *
from tkinter import messagebox

from requests import get, exceptions



ventana = Tk()
ventana.geometry("600x350+400+125")
ventana.title("G3tL1n3")
#ventana.iconbitmap("mini-goo.ico")
ventana.config(background="#000000")
Titulo = Label(text="G3tL1n3", font=("Cambria", 20), bg="#000000", fg="white", width="500", height="2")
Titulo.pack()
Titulo1 = Label(text="Creador: N05TR@  Version: 1.0", font=("Cambria", 10), bg="#000000", fg="white", width="500", height="1")
Titulo1.pack()
Titulo1 = Label(text="", font=("Cambria", 15), bg="#ffffff", fg="white", width="500", height="1")
Titulo1.place(x = 0, y = 322)

def mensaje():
    acerca = '''
    Aplicacion: G3tL1n3.
    Version: 1.0
    Lenguaje de Programacion: Python 3.8.5
    Creador: N05TR4.
    Fecha: 18/05/2021.
    '''
    messagebox.showinfo(title= "Informacion", message= acerca)


# Creando barra de menu
menubarra = Menu(ventana)
ventana.config(menu = menubarra)
filemenu = Menu(menubarra)
filemenu = Menu(menubarra, tearoff=0)
filemenu.add_command(label="ACERCA DE", command = mensaje )
filemenu.add_separator()
filemenu.add_command(label="SALIR", command = ventana.quit)
menubarra.add_cascade(label = "OPCIONES", menu = filemenu)


# Variable principal
verificar = StringVar()

# Barra de Captura de los datos
verificar_entry = Entry(textvariable=verificar, width=50)
verificar_entry.place(x=50, y=100)

def check_connection():

    try:

        get(verificar.get(), timeout=4)
        messagebox.showinfo(title="Informacion", message="Estado Activo")


    except exceptions.ConnectionError:
        messagebox.showwarning(title="Informacion", message="Estado Inactivo")






# creando boton
btnVerificar = Button(ventana, text="Buscar", font = ("Cambria", 12), command = check_connection, width = "10", fg = "black",
                   height = "1", bg="#ffffff")
btnVerificar.place(x=400, y=95)




if __name__ == '__main__':
    ventana.mainloop()