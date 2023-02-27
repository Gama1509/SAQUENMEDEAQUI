from tkinter import *
from Vmaestro import *
class Opcionesmaestro:
    def mostraropciones():
        window=Tk()
        window.resizable(False,False)
        window.title("Menú de opciones")
        window.geometry("500x300")
        window.config(bg="purple")

        panel=Frame()
        panel.pack()
        panel.config(width="500",height="500")
        panel.config(bg="purple")

        def botonregistro():
            try:
                window.destroy()
                Maestro.mostrarinterfazregistromaestro()
            except:
                print("error")
        def botonconsulta():
                window.destroy()
                Maestro.mostrarinterfazconsultamaestro()
        def botoneliminar():
                window.destroy()
                Maestro.mostrarinterfazeliminarmaestro()
        def botonregreso():
             window.destroy()
             from index import Index
             Index.mostrarindex()

        registrar=Button(window,text="Registrar",command=botonregistro)
        registrar.pack()
        registrar.place(x=230,y=0)
        consultar=Button(window,text="Consultar",command=botonconsulta)
        consultar.pack()
        consultar.place(x=228,y=75)
        eliminar=Button(window,text="Eliminar",command=botoneliminar)
        eliminar.pack()
        eliminar.place(x=210,y=150)
        regresar=Button(window,text="Volver",command=botonregreso)
        regresar.pack()
        regresar.place(x=235,y=255)
        
        mainloop()
