from tkinter import *
from tkinter import messagebox

lista1=[]
class Alumno:
    
    def mostrarinterfazregistroalumno():
        window=Tk()
        window.resizable(False,False)
        window.title("Registro alumno")
        window.geometry("500x300")
        window.config(bg="red")

        panel=Frame()
        panel.pack()
        panel.config(width="500",height="500")
        panel.config(bg="red")

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

        curp=Label(window,text="CURP")
        curp.pack()
        curp.place(x=163,y=60)
        curpe=Entry(window)
        curpe.pack()
        curpe.place(x=220,y=60)
        curpe.config(width=40)


        boleta=Label(window,text="Boleta")
        boleta.pack()
        boleta.place(x=160,y=90)
        boletae=Entry(window)
        boletae.pack()
        boletae.place(x=220,y=90)
        boletae.config(width=40)
        
         
        listaopciones=["2IM1","2IM2","2IM3","2IM4","2IM5","2IM6","2IM7","2IM8","2IM9","2IM10","4IM1","4IM2","4IM3","4IM4","4IM5","4IM6","4IM7","4IM8","4IM9","4IM10","6IM1","6IM2","6IM3","6IM6","6IM5","6IM6","6IM7","6IM8","6IM9","6IM10","2IV1","2IV2","2IV3","2IV4","2IV5","2IV6","2IV7","2IV8","2IV9","2IV10","4IV1","4IV4","4IV3","4IV4","4IV5","4IV6","4IV7","4IV8","4IV9","4IV10","6IV1","6IV6","6IV3","6IV6","6IV5","6IV6","6IV7","6IV8","6IV9","6IV10"]
        valor=StringVar(window)
        valor.set(listaopciones[0])
        grupo=Label(window,text="Grupo")
        grupo.pack()
        grupo.place(x=160,y=120)
        grupomenu=OptionMenu(window,valor,*listaopciones)
        grupomenu.pack()
        grupomenu.place(x=220,y=120)
        
        
        correo=Label(window, text="Correo electrónico")
        correo.pack()
        correo.place(x=95,y=160) 
        correoe=Entry(window)
        correoe.pack()
        correoe.place(x=220,y=160)
        correoe.config(width=40)
        
        def registrar():
            tnombre=nombree.get().upper()
            tedad=edade.get().replace(" ",(""))
            tcurp=curpe.get().upper().replace(" ",(""))
            tboleta=boletae.get().upper().replace(" ",(""))
            tcorreo=correoe.get().upper().replace(" ",(""))
            seleccionada=valor.get()

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
                        if len(tcurp)!=18:
                            messagebox.showerror("Error","El CURP lleva 18 caracteres")
                        else:
                            lista1.append(tcurp)
                            if tboleta.isdigit()!=True:
                                messagebox.showerror("Error","La boleta solo lleva digitos")
                            else:
                                if len(tboleta)!=10:
                                    messagebox.showerror("Error","La boleta debe llevar 10 digitos")
                                else:
                                    lista1.append(tboleta)
                                    lista1.append(seleccionada)
                                    if len(tcorreo)<1:
                                        messagebox.showerror("Error","Debe escribir algo en el campo del correo")
                                    else:
                                        lista1.append(tcorreo)
                                        messagebox.showinfo("Exito","Registro hecho exitosamente")
                                        nombree.delete(0,END)
                                        edade.delete(0,END)
                                        curpe.delete(0,END)
                                        boletae.delete(0,END)
                                        correoe.delete(0,END)
                                        print(lista1)

        def volver():
            window.destroy()
            from Vopcionesalumno import Opcionesalumno
            Opcionesalumno.mostraropciones()

        enviar=Button(window,text="Registrar",command=registrar)
        enviar.pack()
        enviar.place(x=245,y=200)
        regresara=Button(window,text="Volver",command=volver)
        regresara.pack()
        regresara.place(x=250,y=250)
        mainloop()

    def mostrarinterfazconsultaalumno():
        window=Tk()
        window.resizable(False,False)
        window.title("Consulta alumno")
        window.geometry("500x300")
        window.config(bg="red")

        panel=Frame()
        panel.pack()
        panel.config(width="500",height="500")
        panel.config(bg="red")


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
                        curpb=lista1[x+2]
                        boletab=lista1[x+3]
                        grupob=lista1[x+4]
                        correb=lista1[x+5]
                        nombrem=Label(window,text="Nombre: "+nombreb)
                        nombrem.pack()
                        nombrem.place(x=0,y=30)
                        edadm=Label(window,text="Edad: "+edadb)
                        edadm.pack()
                        edadm.place(x=0,y=60)
                        curpm=Label(window,text="CURP: "+curpb)
                        curpm.pack()
                        curpm.place(x=0,y=90)
                        boletam=Label(window,text="Boleta: "+boletab)
                        boletam.pack()
                        boletam.place(x=0,y=120)
                        grupom=Label(window,text="Grupo: "+grupob)
                        grupom.pack()
                        grupom.place(x=0,y=150)
                        correom=Label(window,text="Correo electrónico: "+correb)
                        correom.pack()
                        correom.place(x=0,y=180)
                        buscare.delete(0,END)
        
        def volver():
            window.destroy()
            from Vopcionesalumno import Opcionesalumno
            Opcionesalumno.mostraropciones()
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
    
    def mostrarinterfazeliminaralumno():
        window=Tk()
        window.resizable(False,False)
        window.title("Eliminar registro de alumno")
        window.geometry("500x300")
        window.config(bg="red")

        panel=Frame()
        panel.pack()
        panel.config(width="500",height="500")
        panel.config(bg="red")


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
                        curpb=lista1[x+2]
                        boletab=lista1[x+3]
                        grupob=lista1[x+4]
                        correb=lista1[x+5]
                        buscare.delete(0,END)
                lista1.remove(nombreb)
                lista1.remove(edadb)
                lista1.remove(curpb)
                lista1.remove(boletab)
                lista1.remove(grupob)
                lista1.remove(correb)

        def volver():
            window.destroy()
            from Vopcionesalumno import Opcionesalumno
            Opcionesalumno.mostraropciones()
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
        def mostrar():
            print(lista1)
        ver=Button(window,text="Ver",command=mostrar)
        ver.pack()
        ver.place(x=400,y=240)
        mainloop()
