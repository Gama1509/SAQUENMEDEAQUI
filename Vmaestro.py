from tkinter import *
from tkinter import messagebox
lista1=[] 
class Maestro:
    def mostrarinterfazregistromaestro():
        window=Tk()
        window.resizable(False,False)
        window.title("Registro profesor")
        window.geometry("500x300")
        window.config(bg="purple")

        panel=Frame()
        panel.pack()
        panel.config(width="500",height="500")
        panel.config(bg="purple")

        nombre=Label(window,text="Nombre completo")
        nombre.pack()
        nombre.place(x=95,y=0)
        nombree=Entry(window)
        nombree.pack()
        nombree.place(x=220,y=0)
        nombree.config(width=40)

        
        edad=Label(window,text="Edad")
        edad.pack()
        edad.place(x=167,y=30)
        edade=Entry(window)
        edade.pack()
        edade.place(x=220,y=30)
        edade.config(width=40)

        rfc=Label(window,text="RFC")
        rfc.pack()
        rfc.place(x=172,y=60)
        rfce=Entry(window)
        rfce.pack()
        rfce.place(x=220,y=60)
        rfce.config(width=40)

        listaescolaridad=["Licenciatura","Maestria","Doctorado"]
        valor=StringVar()
        valor.set(listaescolaridad[0])
        escolaridad=Label(window,text="Escolaridad")
        escolaridad.pack()
        escolaridad.place(x=133,y=90)
        menuescolaridad=OptionMenu(window,valor,*listaescolaridad)
        menuescolaridad.config(width=20)
        menuescolaridad.pack()
        menuescolaridad.place(x=220,y=90)

        listaturnos=["Matutino","Vespertino","Ambos"]
        opcion=StringVar()
        opcion.set(listaturnos[0])
        turno=Label(window,text="Turno en el que enseña")
        turno.pack()
        turno.place(x=70,y=135)
        menuturnos=OptionMenu(window,opcion,*listaturnos)
        menuturnos.config(width=20)
        menuturnos.pack()
        menuturnos.place(x=220,y=135)

        
        correo=Label(window, text="Correo electrónico")
        correo.pack()
        correo.place(x=95,y=180) 
        correoe=Entry(window)
        correoe.pack()
        correoe.place(x=220,y=180)
        correoe.config(width=40)

        def registrar():
            tnombre=nombree.get().upper()
            tedad=edade.get().replace(" ",(""))
            trfc=rfce.get().upper().replace(" ",(""))
            escolaridad=valor.get()
            turno=opcion.get()
            tcorreo=correoe.get().upper().replace(" ",(""))
            if len(tnombre)<1 or any(char.isdigit() for char in tnombre):
                    messagebox.showerror("Error","El nombre no lleva numeros y debe tener una longitud mayor a 0")
            else:
                lista1.append(tnombre)
                if tedad.isdigit()!=True:
                    messagebox.showerror("Error","La edad solo lleva digitos")
                else:
                    if len(tedad)<0 or len(tedad)>2:
                        messagebox.showerror("Error","La edad debe llevar 2 digitos")
                    else:
                        lista1.append(tedad)
                        if len(trfc)!=13:
                            messagebox.showerror("Error","El RFC lleva 13 caracteres")
                        else:
                            lista1.append(trfc)
                            lista1.append(escolaridad)
                            lista1.append(turno)
                            if len(tcorreo)<1:
                                messagebox.showerror("Error","Debe escribir algo en el campo del correo")
                            else:
                                lista1.append(tcorreo)
                                messagebox.showinfo("Exito","Registro hecho exitosamente")
                                nombree.delete(0,END)
                                edade.delete(0,END)
                                rfce.delete(0,END)
                                correoe.delete(0,END)
                                print(lista1)

        def volver():
            window.destroy()
            from Vopcionesmaestro import Opcionesmaestro
            Opcionesmaestro.mostraropciones()

        enviar=Button(window,text="Registrar",command=registrar)
        enviar.pack()
        enviar.place(x=245,y=220)
        regresara=Button(window,text="Volver",command=volver)
        regresara.pack()
        regresara.place(x=250,y=270)
        mainloop()

    def mostrarinterfazconsultamaestro():
        window=Tk()
        window.resizable(False,False)
        window.title("Consulta maestro")
        window.geometry("500x300")
        window.config(bg="purple")

        panel=Frame()
        panel.pack()
        panel.config(width="500",height="500")
        panel.config(bg="purple")


        buscarl=Label(window,text="Ingrese un nombre")
        buscarl.pack()
        buscarl.place(x=0,y=0)

        buscare=Entry(window)
        buscare.pack()
        buscare.place(x=150,y=0)
        
        def botonbuscar():
            tbuscar=buscare.get().upper()
            if len(tbuscar)<1 or any(char.isdigit() for char in tbuscar):
                    messagebox.showerror("Error","El nombre no lleva numeros y debe tener una longitud mayor a 0")
            else:
                for x in range(len(lista1)):
                    if tbuscar==lista1[x]:
                        nombreb=lista1[x]
                        edadb=lista1[x+1]
                        rfcb=lista1[x+2]
                        escolaridadb=lista1[x+3]
                        turnob=lista1[x+4]
                        correb=lista1[x+5]
                        nombrem=Label(window,text="Nombre: "+nombreb)
                        nombrem.pack()
                        nombrem.place(x=0,y=30)
                        edadm=Label(window,text="Edad: "+edadb)
                        edadm.pack()
                        edadm.place(x=0,y=60)
                        rfcm=Label(window,text="RFC: "+rfcb)
                        rfcm.pack()
                        rfcm.place(x=0,y=90)
                        escolaridadm=Label(window,text="Escolaridad: "+escolaridadb)
                        escolaridadm.pack()
                        escolaridadm.place(x=0,y=120)
                        turnom=Label(window,text="Turno en el que enseña: "+turnob)
                        turnom.pack()
                        turnom.place(x=0,y=150)
                        correom=Label(window,text="Correo electrónico: "+correb)
                        correom.pack()
                        correom.place(x=0,y=180)
                        buscare.delete(0,END)
        
        def volver():
            window.destroy()
            from Vopcionesmaestro import Opcionesmaestro
            Opcionesmaestro.mostraropciones()
        buscarboton=Button(window,text="Buscar",command=botonbuscar)
        buscarboton.pack()
        buscarboton.place(x=300,y=0)
        regresara=Button(window,text="Volver",command=volver)
        regresara.pack()
        regresara.place(x=400,y=270)
        aviso=Label(window,text="Si el registro no existe al presionar el boton no pasara nada")
        aviso.pack()
        aviso.place(x=0,y=270)
        mainloop()
    def mostrarinterfazeliminarmaestro():
        window=Tk()
        window.resizable(False,False)
        window.title("Eliminar registro de profesor")
        window.geometry("500x300")
        window.config(bg="purple")

        panel=Frame()
        panel.pack()
        panel.config(width="500",height="500")
        panel.config(bg="purple")


        buscarl=Label(window,text="Ingrese un nombre")
        buscarl.pack()
        buscarl.place(x=0,y=0)

        buscare=Entry(window)
        buscare.pack()
        buscare.place(x=150,y=0)
        
        def botoneliminar():
            tbuscar=buscare.get().upper()
            if len(tbuscar)<1 or any(char.isdigit() for char in tbuscar):
                    messagebox.showerror("Error","El nombre no lleva numeros y debe tener una longitud mayor a 0")
            else:
                for x in range(len(lista1)):
                    if tbuscar==lista1[x]:
                        nombreb=lista1[x]
                        edadb=lista1[x+1]
                        rfcb=lista1[x+2]
                        escolaridadb=lista1[x+3]
                        turnob=lista1[x+4]
                        correb=lista1[x+5]
                        buscare.delete(0,END)
                lista1.remove(nombreb)
                lista1.remove(edadb)
                lista1.remove(rfcb)
                lista1.remove(escolaridadb)
                lista1.remove(turnob)
                lista1.remove(correb)
        def mostrar():
            print(lista1)
        def volver():
            window.destroy()
            from Vopcionesmaestro import Opcionesmaestro
            Opcionesmaestro.mostraropciones()
        buscarboton=Button(window,text="Eliminar",command=botoneliminar)
        buscarboton.pack()
        buscarboton.place(x=300,y=0)
        regresara=Button(window,text="Volver",command=volver)
        regresara.pack()
        regresara.place(x=400,y=270)
        aviso=Label(window,text="Si el registro no existe al presionar el boton no pasara nada")
        aviso.pack()
        aviso.place(x=0,y=270)
        aviso1=Label(window,text="Si la eliminacion se hizo exitosamente se borrara el texto que escribio")
        aviso1.pack()
        aviso1.place(x=0,y=240)
        ver=Button(window,text="Ver",command=mostrar)
        ver.pack()
        ver.place(x=400,y=240)
        mainloop()
