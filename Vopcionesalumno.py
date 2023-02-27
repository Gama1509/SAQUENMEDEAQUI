from tkinter import *
from Valumno import *
class Opcionesalumno:
    def mostraropciones():
        ventanaopcionesalumno=Tk()
        ventanaopcionesalumno.resizable(False,False)
        ventanaopcionesalumno.title("Menú de opciones alumnos")
        ventanaopcionesalumno.geometry("500x300")
        ventanaopcionesalumno.config(bg="red")

        panel=Frame()
        panel.pack()
        panel.config(width="500",height="500")
        panel.config(bg="red")

        def botonregistro():
            try:
                ventanaopcionesalumno.destroy()
                Alumno.mostrarinterfazregistroalumno()
            except:
                print("error")
        def botonconsulta():
                ventanaopcionesalumno.destroy()
                Alumno.mostrarinterfazconsultaalumno()
        def botoneliminar():
                ventanaopcionesalumno.destroy()
                Alumno.mostrarinterfazeliminaralumno()
        
        def botonregreso():
             ventanaopcionesalumno.destroy()
             from index import Index
             Index.mostrarindex()

        registrar=Button(ventanaopcionesalumno,text="Registrar",command=botonregistro)
        registrar.pack()
        registrar.place(x=230,y=0)
        consultar=Button(ventanaopcionesalumno,text="Consultar",command=botonconsulta)
        consultar.pack()
        consultar.place(x=228,y=75)
        eliminar=Button(ventanaopcionesalumno,text="Eliminar registro",command=botoneliminar)
        eliminar.pack()
        eliminar.place(x=210,y=150)
        regresar=Button(ventanaopcionesalumno,text="Volver",command=botonregreso)
        regresar.pack()
        regresar.place(x=235,y=225)
        mainloop()

            
    