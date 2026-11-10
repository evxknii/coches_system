from coches import coches
from tkinter import Label, Entry, Button, Tk, messagebox
print("\033c")

class App:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestion de Coches")
        self.ventana.geometry("800x700")
        self.ventana.resizable(1,1) # para poder modificar el tamaño desde la interfaz
        self.main()

    ## ...Vistas   
    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def terminarSistema(self):
        input("....:::: GRACIAS POR UTILIZAR NUESTRO SISTEMA, \n  vuelve pronto ::::...")

    def opcionInvalida(self):
        input("\n\t.... ¡Opcion invalidad, vuelve a intentarlo!.... ") 
        
    def menu_acciones(self):
        self.borrarPantalla()
        tipo="Coches"
        Label(self.ventana,text=f"....:::: Menu de {tipo} ::::...\n").pack(pady=10)
        Button(self.ventana,text="1.-Agregar",command=self.insertar_view).pack(pady=5)
        Button(self.ventana,text="2.-Borrar",command=self.eliminar_view).pack(pady=5)
        Button(self.ventana,text="3.-Modificar",command=self.modificar_view).pack(pady=5)
        Button(self.ventana,text="4.-Mostrar",command=self.consultar_view).pack(pady=5)
        Button(self.ventana,text="5.-Regresar",command=self.main).pack(pady=5)

    def main(self):
        self.borrarPantalla()
        Label(self.ventana, text="\n...::: M E N U  P R I N C I P A L :::...").pack(pady=10)
        Button(self.ventana,text="1.- Coches", command=self.menu_acciones).pack(pady=5)
        Button(self.ventana,text="2.- Salir", command=self.ventana.quit).pack(pady=5)

    def insertar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="... Ingresar los datos del coche ...").pack(pady=10)
        Label(self.ventana, text="Marca: ").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)

        Label(self.ventana, text="Color: ").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)

        Label(self.ventana, text="Modelo: ").pack(pady=5)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)

        Label(self.ventana, text="Velocidad: ").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)

        Label(self.ventana, text="Potencia: ").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)

        Label(self.ventana, text="Asientos: ").pack(pady=5)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)
        Button(self.ventana,text="Guardar",command=self.insertar_controller).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)

    def eliminar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingresar el ID del coche a Eliminar...").pack(pady=10)

        Label(self.ventana, text="ID: ").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.pack(pady=5)


        Button(self.ventana,text="Eliminar",command=self.eliminar_controller).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)


    def modificar_view(self):
        self.borrarPantalla()
        Label(self.ventana, text="...Ingresar el ID del coche a modificar...").pack(pady=10)
        
        Label(self.ventana, text="ID: ").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        Label(self.ventana, text="Nueva Marca: ").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.pack(pady=5)

        Label(self.ventana, text="Nuevo Color: ").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)

        Label(self.ventana, text="Nuevo Modelo: ").pack(pady=5)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)

        Label(self.ventana, text="Nueva Velocidad: ").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)

        Label(self.ventana, text="Nueva Potencia: ").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)

        Label(self.ventana, text="Nuevos Asientos: ").pack(pady=5)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)

        
        Button(self.ventana,text="Guardar",command=self.modificar_controller).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)

    def consultar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text=" ::: Consultar los coches :::").pack(pady=10)
        filas=""
        filas=self.consultar_controlles(filas)
        Label(self.ventana,text=f"{filas}").pack(pady=10)
        Button(ventana,text="Regresar",command=self.menu_acciones).pack(pady=10)


    ## ...Controlador


    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(title="... Exitoso ...",message="...¡Accion Realizada con Exito!...")
        else:
            input("...¡Esta Accion no pudo realizarse en este momento !...")
            messagebox.showerror(title="...¡ Verifica por favor !...",message="...¡Esta Accion no pudo realizarse en este momento !...")

    def insertar_controller(self):
        coche1=coches.Coches(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta=coche1.insertar()
        self.respuesta_sql(respuesta)
        del coche1 

    def eliminar_controller(self):
        id=self.id.get()
        respuesta=coches.coches.eliminar(id)
        self.respuesta_sql(respuesta)


    def consultar_controller(self):
        registros=coches.Coches.consultar()    
        num_coche=1
        if len(registros)>0:
            for fila in registros:
                filas=filas+f"\n\tCoche #: {num_coche}\nID: {fila[0]},\tMarca: {fila[1]}\n\tColor: {fila[2]}\tModelo: {fila[3]},\n\tVelocidad: {fila[4]},\tPotencia: {fila[5]}\n\tAsientos: {fila[6]}"
                num_coche+=1
        else:
            filas="..¡No se encontraro informacion en la BD!"
        return filas



    def menu_coches(self):
        opc =True
        while opc:
            self.borrarPantalla()
            opc=self.menu_acciones("Coches")
            match opc:
                case "1":
                    ##solicitar datos y crear objeto de Coches
                    cochesito= self.datos_coches("Coches")
                    coches1= coches.Coches(cochesito['marca'],cochesito['color'],cochesito['modelo'],cochesito['velocidad'],cochesito['potencia'],cochesito['asientos'])
                    respuesta= coches1.insertar()
                    self.respuesta_sql(respuesta)
                    ##borrar objeto que no utilizas
                    del coches1
                case "2":
                    self.borrarPantalla()
                    # En lugar de solo .strip(), conviértelo a entero int()
                    id = int(input("Ingrese el ID del coche a eliminar: ").strip())
                    respuesta=coches.Coches.eliminar(id)
                    self.respuesta_sql(respuesta)
                case "3":
                    self.borrarPantalla()
                    id= input("Ingrese el ID del coche a actualizar: ").strip()
                    cochesito=self.datos_coches(id)
                    coches1 = coches.Coches(
                        cochesito['marca'],
                        cochesito['color'],
                        cochesito['modelo'],
                        cochesito['velocidad'],
                        cochesito['potencia'],
                        cochesito['asientos']
                    )
                    respuesta=coches1.actualizar(id)
                    self.respuesta_sql(respuesta)
                    del coches1
                case "4":
                    self.borrarPantalla()
                    registros=coches.Coches.consultar()
                    
                    num_coche=1
                    if len(registros)>0:
                        for fila in registros:
                            print(f"\n\tCoche numero #: {num_coche}\n\t\tID: {fila[0]},\n\t\tMarca: {fila[1]}\n\t\tColor: {fila[2]}\n\t\tModelo: {fila[3]},\n\t\tVelocidad: {fila[4]},\n\t\tPotencia: {fila[5]}\n\t\tAsientos: {fila[6]}")
                            num_coche+=1
                            self.esperarTecla()
                    else:
                        print("...!No se encontraro informacion en la BD")
                        self.esperarTecla()

                case "5":
                    opc=False
                case _:
                    self.opcionInvalida()



if __name__ == "__main__":
    ventana = Tk()
    app = App(ventana)
    ventana.mainloop()