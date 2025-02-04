from datetime import date
import sqlite3
from wsgiref.validate import validator

class ProgramaPrincipal:

    def menu(self):
        while True:
            print(" ")
            print("Menu de opciones Concesionaria")
            print(" ")
            print("1- MENU AUTOMOVILES")
            print("2- MENU MOTOCICLETAS")
            print("0- Salir")
            nro = int(input("Por favor ingrese un número: "))
            if nro == 1:
                print("Has Ingresado al MENU AUTOMOVILES")
                print("1-Cargar automovil")
                print("2-Modificar precio automovil")
                print("3-Borrar automovil")
                print("4-Cargar disponibilidad del automovil")
                print("5-Listar automoviles")
                print("0-Volver al menu")
                
                opcionAutomovil= int(input("Por favor ingrese una opción: "))
                validar=False
                
                if opcionAutomovil ==1:
                    while(not validar):
                     marca = input("Por favor ingrese la marca del automovil: ")
                     validar=self.validarCaracter(marca)
                    validar=False

                    modelo = input("Por favor ingrese el modelo del automovil: ")

                    while(not validar):
                        precio = input("Por favor ingrese el precio del automovil: ")
                        validar=self.validarPrecio(precio)
                    validar=False

                    while(not validar):
                        cantidadDisponibles=input("Ingrese cantidad disponible: ")
                        validar=self.validarNumero(cantidadDisponibles)
                    validar=False

                    nuevo_automovil = Automovil(marca,modelo,precio,cantidadDisponibles)
                    nuevo_automovil.cargar_automovil()
                if opcionAutomovil ==2:
                    while(not validar):
                        marca = input("Por favor ingrese el nombre de la marca: ")
                        validar=self.validarCaracter(marca)
                    validar=False

 
                    modelo = input("Por favor ingrese modelo: ")
                        

                    while(not validar):
                        precio = input("Por favor ingrese el nuevo precio: ")
                        validar=self.validarPrecio(precio)
                    validar=False

                    
                    automovil_a_modificar=Automovil(marca,modelo,precio)
                    automovil_a_modificar.modificar_automoviles()
                if opcionAutomovil==3:

                    while(not validar):
                        marca=input("Ingrese marca del automovil a eliminar: ")
                        validar=self.validarCaracter(marca)
                    validar=False

                    modelo=input("Ingrese el modelo del automovil a eliminar: ")
                        
                    automovil_a_eliminar=Automovil(marca,modelo)
                    automovil_a_eliminar.eliminar_automovil()
                if opcionAutomovil==4:

                    while(not validar):
                        marca=input("Ingrese marca del automovil que desea cargar disponibilidad: ")
                        validar=self.validarCaracter(marca)
                    validar=False
         
                    modelo=input("Ingrese modelo del automovil que desea cargar disponibilidad: ")
                        

                    cargar_disponibilidad_auto= Automovil(marca,modelo)
                    cargar_disponibilidad_auto.cargar_disponibilidad()
                if opcionAutomovil==5:
                    Automovil.listar_automoviles(Automovil)
                if opcionAutomovil==0:
                    print("Volviendo al menu Consesionaria")     
                elif opcionAutomovil<0 or opcionAutomovil>5:
                    print("ERROR..Opcion fuera de rango")
                
               # --------------------listo menu automovil-----------------------------------------#

            if nro ==2:
                print("Has Ingresado al MENU MOTOCICLETAS")
                print("1-Cargar motocicletas")
                print("2-Cargar disponibilidad motocicleta")
                print("3-Actualizar precio motocicletas")
                print("4-Borrar motocicletas")
                print("5-LISTADOS")
                print("6-Modificar motocicleta")
                print("0-Volver al menu")
                opcionMotocicletas= int(input("Por favor ingrese una opción: "))
                validar=False
                if opcionMotocicletas ==1:
                    while(not validar):
                        marca = input("Ingrese la marca de la motocicleta: ")
                        validar=self.validarCaracter(marca)
                    validar=False
                   
                    #A cilindrada y modelo no le pusimos validaciones ya que pueden ser ambos. 
                    
                    modelo = input("Ingrese el modelo de la motocicleta: ")
                        
                    cilindrada = input("Ingrese la cilindrada: ")
                   
                    while(not validar):
                        color = input("Ingrese el color de la motocicleta: ")
                        validar=self.validarCaracter(color)
                    validar=False
                    
                    while(not validar):
                        precio = input("Ingrese el precio: ")
                        validar=self.validarPrecio(precio)
                    validar=False
                   
                    while(not validar):
                        cantidadDisponibles=input("Ingrese cantidad disponible: ")
                        validar=self.validarNumero(cantidadDisponibles)
                    validar=False


                    nueva_motocicleta = Motocicleta(marca,modelo,cilindrada,precio,color, cantidadDisponibles)
                    nueva_motocicleta.cargar_motocicleta()
                if opcionMotocicletas==2:
                    Motocicleta.incrementar_disponibilidad(Motocicleta)
                if opcionMotocicletas ==3:
                    Motocicleta.actualizar_motocicleta(Motocicleta)
                if opcionMotocicletas==4:
                    Motocicleta.eliminar_motocicleta(Motocicleta)
                if opcionMotocicletas==5:
                    print("1-Listado por fecha \n 2-Listado historico \n 3- Listado por Marca y Modelo \n 4-Listado por color")
                    opcionlistado=int(input("Selecciona una opcion: "))
                    if opcionlistado==1:
                        Motocicleta.listar_motocicletas_fecha(Motocicleta)
                    if opcionlistado==2:
                        Motocicleta.listar_motocicletas_historico(Motocicleta)
                    if opcionlistado==3:
                        Motocicleta.listar_motocicleta_marca_modelo(Motocicleta)
                    if opcionlistado==4:
                        Motocicleta.listar_motocicleta_color(Motocicleta)
                if opcionMotocicletas ==6:
                    Motocicleta.modificar_motocicleta(Motocicleta)
                if opcionMotocicletas==0:
                    print("Volviendo al menu Consesinaria")
                if 0<opcionMotocicletas>6:
                    print("OPCION FUERA DE RANGO.")
                    break
            if nro==0:
                break
            if 0>nro>2:
                print("OPCION FUERA DE RANGO")
                break
    
    def crearTablas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS AUTOMOVILES")
        conexion.miCursor.execute("CREATE TABLE AUTOMOVILES (id_automovil INTEGER PRIMARY KEY , marca  VARCHAR(30) ,modelo  VARCHAR(30),precio FLOAT NOT NULL, cantidadDisponibles INTEGER NOT NULL,UNIQUE(marca,modelo))")    
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS MOTOCICLETAS")
        conexion.miCursor.execute("CREATE TABLE MOTOCICLETAS (id_moto INTEGER PRIMARY KEY , marca VARCHAR(30), modelo VARCHAR(30), cilindrada  VARCHAR(30), precio INTEGER NOT NULL, color  VARCHAR(30), cantidadDisponibles INTEGER NOT NULL, fechaUltimoPrecio DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP)")   
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

    def motocicletas_historico(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS MOTOCICLETAS_HISTORICO")
        conexion.miCursor.execute("CREATE TABLE MOTOCICLETAS_HISTORICO (id_moto INTEGER , marca  VARCHAR(30), modelo  VARCHAR(30), cilindrada  VARCHAR(30), precio INTEGER, color  VARCHAR(30), cantidadDisponibles INTEGER, fechaUltimoPrecio DATETIME)")
        conexion.miConexion.commit()     
        conexion.cerrarConexion()

    def validarCaracter(self,validar):
        if(validar.isalpha()!=True or len(validar)>=30):
            print("Error. Intente nuevamente")
            return False
        return True

    def validarNumero(self,validar):
        if(validar.isnumeric()==False or int(validar)<=0):
            print("Error. ingrese nuevamente")
            return False
        return True

    def validarPrecio(self,precio):
        if  precio.isnumeric()==False or float(precio)<=0 : 
            print("Error. ingrese nuevamente")
            return False
        return True
    

       
   
class Automovil:
    def __init__(self, marca, modelo,precio=None,cantidadDisponibles=None):
        self.marca = marca
        self.modelo = modelo
        self.precio=precio
        self.cantidadDisponibles=cantidadDisponibles
        
    def cargar_automovil(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO AUTOMOVILES(marca,modelo,precio,cantidadDisponibles) VALUES('{}', '{}','{}','{}')".format(self.marca, self.modelo,self.precio,self.cantidadDisponibles))
            conexion.miConexion.commit()
            print("Automovil cargado exitosamente")
        except:
            print("Error al agregar un automovil")
        finally:
            conexion.cerrarConexion()
    
    
    def modificar_automoviles(self):
        conexion = Conexiones()
        conexion.abrirConexion()

        try:
            conexion.miCursor.execute("SELECT marca, modelo FROM AUTOMOVILES")
            marca_modelo= conexion.miCursor.fetchall()
            if marca_modelo==[]:
                print("Tabla vacia")
            else:
                for marca_modelo in marca_modelo:
                    if marca_modelo[0] ==self.marca and marca_modelo[1]==self.modelo:
                        conexion.miCursor.execute("UPDATE AUTOMOVILES SET precio='{}' where marca='{}' and modelo='{}' ".format(self.precio,self.marca,self.modelo))
                        conexion.miConexion.commit()
                        print("Automovil eliminado correctamente")
                    else:
                        print("El automovil ingresado no existe")
        except:
            print('Error al actualizar un automovil')
        finally:
            conexion.cerrarConexion()  
    def eliminar_automovil(self):
        conexion=Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT marca, modelo FROM AUTOMOVILES")
            marca_modelo= conexion.miCursor.fetchall()
            if marca_modelo==[]:
                print("Tabla vacia")
            else:
                for marca_modelo in marca_modelo:
                    if marca_modelo[0] ==self.marca and marca_modelo[1]==self.modelo:
                        conexion.miCursor.execute("DELETE FROM AUTOMOVILES where marca='{}'and modelo='{}'" .format(self.marca,self.modelo))
                        conexion.miConexion.commit()
                        print("Automovil eliminado correctamente")
                    else:
                        print("El automovil ingresado no existe")
        except:
            print("ERROR. No se ha podido eliminar el automovil")
        finally:
            conexion.cerrarConexion()

    def cargar_disponibilidad(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        
        try:
            conexion.miCursor.execute("SELECT marca, modelo FROM AUTOMOVILES")
            marca_modelo= conexion.miCursor.fetchall()
            if marca_modelo==[]:
                print("Tabla vacia")
            else:
                for marca_modelo in marca_modelo:
                    if marca_modelo[0]==self.marca and marca_modelo[1]==self.modelo:
                        conexion.miCursor.execute("UPDATE AUTOMOVILES SET cantidadDisponibles=cantidadDisponibles + 1 where marca='{}' and modelo='{}'".format(self.marca, self.modelo))
                        conexion.miConexion.commit()
                        print("Cantidad disponible modificada correctamente")
                    else:
                        print("El automovil ingresado no existe")
        except:
            print("ERROR. No se ha podido actualizar la cantidad disponible")
        finally:
            conexion.cerrarConexion()
    def listar_automoviles(self):
        conexion=Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM AUTOMOVILES")
            autos = conexion.miCursor.fetchall()
            if autos==[]:
                print("Tabla vacia")
            else:
                for autos in autos:
                 print(f'ID: {autos[0]}\nMarca: {autos[1]}\nModelo: {autos[2]}\nPrecio: {autos[3]}\nCantidad disponible: {autos[4]}')   
        except:
            print("ERROR. No se han podido listar los automoviles")
        finally:
            conexion.cerrarConexion()




class Motocicleta:
    def __init__(self,marca,modelo,cilindrada,precio,color,cantidadDisponibles):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada
        self.precio=precio
        self.color = color
        self.cantidadDisponibles=cantidadDisponibles
        

    def cargar_motocicleta(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("INSERT INTO MOTOCICLETAS(marca,modelo,cilindrada,precio,color,cantidadDisponibles) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(self.marca,self.modelo,self.cilindrada,self.precio,self.color,self.cantidadDisponibles))
            conexion.miConexion.commit()
            print("Motocicleta cargada exitosamente")
        except:
            print("Error al agregar una motocicleta")
        finally:
            conexion.cerrarConexion()

    def actualizar_motocicleta(self):
        programa.motocicletas_historico() 
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS") 
            motocicletas = conexion.miCursor.fetchall() 
            for moto in motocicletas:
                id, modelo, marca, cilindrada, precio, color, cantidadDisponibles, fecha = moto 
                conexion.miCursor.execute("INSERT INTO MOTOCICLETAS_HISTORICO(id_moto,modelo,marca,cilindrada,precio,color,cantidadDisponibles,fechaUltimoPrecio) VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(id,modelo,marca,cilindrada,precio,color,cantidadDisponibles,fecha))
                conexion.miConexion.commit()
                conexion.miCursor.execute("UPDATE MOTOCICLETAS SET precio= precio*1.1, fechaUltimoPrecio=CURRENT_TIMESTAMP")
                conexion.miConexion.commit()
            print("Motocicletas actualizadas correctamente")
        except:
            print("Error al actualizar precios")
        finally:
            conexion.cerrarConexion()
    def eliminar_motocicleta(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            id=input("Ingrese el ID de la motocicleta a eliminar: ")

            conexion.miCursor.execute("DELETE FROM MOTOCICLETAS where id_moto='{}'".format(id))
            conexion.miConexion.commit()
            print("Motocicleta eliminada exitosamente")
        except:
            print("ERROR. No se ha podido eliminar la motocicleta")
        finally:
            conexion.cerrarConexion()

    def incrementar_disponibilidad(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            id = input("Ingrese el ID de la motocicleta a incrementar: ")
            conexion.miCursor.execute("UPDATE MOTOCICLETAS SET cantidadDisponibles= cantidadDisponibles+1 where id_moto= '{}'".format(id))
            conexion.miConexion.commit()
            print("Motocicleta incrementada exitosamente")
        except:
            print("ERROR. No se ha podido incrementar la Motocicleta")
        finally:
            conexion.cerrarConexion() 

    def listar_motocicletas_fecha(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            anio= input("ingrese año buscar AAAA \n") 
            mes=input("ingrese mes buscar  MM:\n")        
            dia= input("ingrese dia buscar DD: \n")                     
            fecha= str(anio)+"-"+str(mes)+"-"+str(dia)+" 23:59"            
            print("fecha seleccionada :"+ fecha +"\n" )             
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS_HISTORICO where fechaUltimoPrecio <= '{}'".format(fecha))             
            motocicletas_historico = conexion.miCursor.fetchall()     
            for i in range(len(motocicletas_historico)): 
                moto=motocicletas_historico[i] 
                print(f'ID: {moto[0]}\nMarca: {moto[1]}\nModelo: {moto[2]}\nCilindrada: {moto[3]}\nPrecio: {moto[4]}\nColor: {moto[5]}\nCantidad Disponible: {moto[6]}\nFecha Ultimo Precio: {moto[7]}')                              
        except:
            print("ERROR. No se ha podido mostrar el listado")
        finally:
            conexion.cerrarConexion() 

    def listar_motocicletas_historico(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS_HISTORICO")
            motocicletas_historico = conexion.miCursor.fetchall()
            for moto in motocicletas_historico:
                print("-----------LISTADO HISTORICO---------------")
                print(f'ID: {moto[0]}\nMarca: {moto[1]}\nModelo: {moto[2]}\nCilindrada: {moto[3]}\nPrecio: {moto[4]}\nColor: {moto[5]}\nCantidad Disponible: {moto[6]}\nFecha Ultimo Precio: {moto[7]}')
                print("----------------------------------")
        except:
            print("Error al mostrar motocicletas")
        finally:
            conexion.cerrarConexion()
    def listar_motocicleta_marca_modelo(self):
        conexion=Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS")
            motocicletas = conexion.miCursor.fetchall()
            marca= input("ingrese marca a buscar: ")
            modelo=input("ingrese modelo: ")
            print("-------------LISTADO POR MARCA Y MODELO-----------------")     
            for moto in motocicletas:
                if moto[1] == marca and moto[2]==modelo:
                        print(f'ID: {moto[0]}\nMarca: {moto[1]}\nModelo: {moto[2]}\nCilindrada: {moto[3]}\nPrecio: {moto[4]}\nColor: {moto[5]}\nCantidad Disponible: {moto[6]}\nFecha Ultimo Precio: {moto[7]}')
                        break  
                else:
                    "Listado inexistente."   
        except:
            print("ERROR. No se ha podido mostrar el listado")
        finally:
            conexion.cerrarConexion()
    def listar_motocicleta_color(self):
        conexion=Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS")
            motocicletas = conexion.miCursor.fetchall()
            color = input("ingrese color a buscar: ")
            print("-------------LISTADO COLOR------------------")     
            for moto in motocicletas:
                if moto[5] == color:
                        print(f'ID: {moto[0]}\nMarca: {moto[1]}\nModelo: {moto[2]}\nCilindrada: {moto[3]}\nPrecio: {moto[4]}\nColor: {moto[5]}\nCantidad Disponible: {moto[6]}\nFecha Ultimo Precio: {moto[7]}')
                        break  
                else:
                    "Listado inexistente."   
        except:
            print("ERROR. No se ha podido mostrar el listado")
        finally:
            conexion.cerrarConexion()
    def modificar_motocicleta(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            id=input("Ingresa el ID de la motocicleta a modificar: ")
            precio=input("Ingresa el nuevo precio: ")
            conexion.miCursor.execute("UPDATE MOTOCICLETAS SET precio='{}' where id_moto= '{}' " .format(precio,id))
            conexion.miConexion.commit()
            print("Motocicleta modificada correctamente")
        except:
            print('ERROR AL MODIFICAR')
        finally:
            conexion.cerrarConexion()
    

class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Concesionaria")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()   


            
programa = ProgramaPrincipal()
programa.crearTablas()
programa.menu()