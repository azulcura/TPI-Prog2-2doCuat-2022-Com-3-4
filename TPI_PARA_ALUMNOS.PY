from datetime import date
import sqlite3

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

                if opcionAutomovil ==1:
                    marca = input("Por favor ingrese la marca del automovil: ")
                    modelo = input("Por favor ingrese el modelo del automovil: ")
                    precio = input("Por favor ingrese el precio del automovil: ")
                    cantidadDisponibles = input("Por favor ingrese la cantidad de unidades disponibles: ")
                    nuevo_automovil = Automovil(marca,modelo,precio,cantidadDisponibles)
                    nuevo_automovil.cargar_automovil()
                if opcionAutomovil ==2:
                    marca = input("Por favor ingrese el nombre de la marca: ")
                    modelo = input("Por favor ingrese el nombre del modelo: ")
                    precio = input("Por favor ingrese el nuevo precio: ")
                    automovil_a_modificar=Automovil(marca,modelo,precio)
                    automovil_a_modificar.modificar_automoviles()
                if opcionAutomovil==3:
                    marca=input("Ingrese marca del automovil a eliminar: ")
                    modelo=input("Ingrese el modelo del automovil a eliminar: ")
                    automovil_a_eliminar=Automovil(marca,modelo)
                    automovil_a_eliminar.eliminar_automovil()
                if opcionAutomovil==4:
                    marca=input("Ingrese marca del automovil que desea cargar disponibilidad: ")
                    modelo=input("Ingrese modelo del automovil que desea cargar disponibilidad: ")
                    cargar_disponibilidad_auto= Automovil(marca,modelo)
                    cargar_disponibilidad_auto.cargar_disponibilidad()
                if opcionAutomovil==5:
                    Automovil.listar_automoviles(Automovil)
                if opcionAutomovil==0:
                    break
                if opcionAutomovil<0 or opcionAutomovil>6:
                    print("ERROR. OPCION FUERA DE RANGO.")
                    break
                
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
                if opcionMotocicletas ==1:
                    marca = input("Ingrese la marca de la motocicleta: ")
                    modelo = input("Ingrese el modelo de la motocicleta: ")
                    cilindrada = input("Ingrese la cilindrada: ")
                    color = input("Ingrese color de la motocicleta: ")
                    precio = int(input("Ingrese el precio: "))
                    cantidadDisponibles=int(input("Ingrese cantidad disponible: "))
                    nueva_motocicleta = Motocicleta(marca,modelo,cilindrada,precio,color, cantidadDisponibles)
                    nueva_motocicleta.cargar_motocicleta()
                if opcionMotocicletas==2:
                    marca = input("Por favor ingrese el nombre de la marca: ")
                    modelo = input("Por favor ingrese el nombre del modelo: ")
                    cargar_disponibilidad_moto=Motocicleta(marca,modelo,cantidadDisponibles)
                    cargar_disponibilidad_moto.incrementar_disponibilidad()
                if opcionMotocicletas ==3:
                    Motocicleta.actualizar_motocicleta(Motocicleta)
                if opcionMotocicletas==4:
                    marca = input("Por favor ingrese la marca de la motocicleta: ")
                    modelo = input("Por favor ingrese el modelo de la motocicleta: ")
                    Motocicleta_a_eliminar=Motocicleta(marca, modelo)
                    Motocicleta_a_eliminar.eliminar_motocicleta()
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
                    marca = input("Por favor ingrese el nombre de la marca: ")
                    modelo = input("Por favor ingrese el nombre del modelo: ")
                    precio = int(input("Por favor ingrese el nuevo precio: "))
                    motocicleta_a_modificar=Motocicleta(marca,modelo,precio)
                    motocicleta_a_modificar.modificar_motocicleta()
                if opcionMotocicletas==0:
                    break
                if opcionMotocicletas<0 or opcionMotocicletas>6:
                    print("ERROR. OPCION FUERA DE RANGO.")
                    break
            if nro==0:
                break
            if nro <0 or nro >2:
                print("ERROR. OPCION FUERA DE RANGO")
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
        conexion.miCursor.execute("CREATE TABLE MOTOCICLETAS (id_moto INTEGER PRIMARY KEY , modelo  VARCHAR(30), marca  VARCHAR(30), cilindrada  VARCHAR(30), precio INTEGER NOT NULL, color  VARCHAR(30), cantidadDisponibles INTEGER NOT NULL, fechaUltimoPrecio DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP)")   
        conexion.miConexion.commit()       
        conexion.cerrarConexion()

    def motocicletas_historico(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DROP TABLE IF EXISTS MOTOCICLETAS_HISTORICO")
        conexion.miCursor.execute("CREATE TABLE MOTOCICLETAS_HISTORICO (id_moto INTEGER , modelo  VARCHAR(30), marca  VARCHAR(30), cilindrada  VARCHAR(30), precio INTEGER, color  VARCHAR(30), cantidadDisponibles INTEGER, fechaUltimoPrecio DATETIME)")
        conexion.miConexion.commit()     
        conexion.cerrarConexion()

   

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
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET precio='{}' where marca='{}' and modelo='{}' ".format(self.precio,self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Automovil modificado correctamente")
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
            conexion.miCursor.execute("UPDATE AUTOMOVILES SET cantidadDisponibles=cantidadDisponibles + 1 where marca='{}' and modelo='{}'".format(self.marca, self.modelo))
            conexion.miConexion.commit()
            print("Cantidad disponible modificada correctamente")
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
            print(autos)
        except:
            print("ERROR. No se han podido listar los automoviles")
        finally:
            conexion.cerrarConexion()




class Motocicleta:
    def __init__(self,marca,modelo,cilindrada=None,precio=None,color=None,cantidadDisponibles=None):
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
            conexion.miCursor.execute("INSERT INTO MOTOCICLETAS(modelo,marca,cilindrada,precio,color,cantidadDisponibles) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(self.modelo,self.marca,self.cilindrada,self.precio,self.color,self.cantidadDisponibles))
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
            conexion.miCursor.execute("DELETE FROM MOTOCICLETAS where marca='{}' and modelo='{}'".format(self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Se han eliminado las motocicletas que tengan la misma marca y modelo ingresado")
        except:
            print("ERROR. No se ha podido eliminar la motocicleta")
        finally:
            conexion.cerrarConexion()

    def incrementar_disponibilidad(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        try:
            conexion.miCursor.execute("UPDATE MOTOCICLETAS SET cantidadDisponibles= cantidadDisponibles+1 where marca= '{}' and modelo= '{}' ".format(self.marca, self.modelo))
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
            conexion.miCursor.execute("SELECT * FROM MOTOCICLETAS")
            motocicletas = conexion.miCursor.fetchall()
            fecha = input("ingrese una fecha formato AAAA/MM/DD: ")
            print("-------------LISTADO POR FECHA------------------")     
            for moto in motocicletas:
                print(f'ID: {moto[0]}\nMarca: {moto[1]}\nModelo: {moto[2]}\nCilindrada: {moto[3]}\nPrecio: {moto[4]}\nColor: {moto[5]}\nCantidad Disponible: {moto[6]}\nFecha Ultimo Precio: {moto[7]}')
                if moto[7] == fecha:
                    break     
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
            marca = input("ingrese marca a buscar: ")
            modelo=input("ingrese modelo a buscar: ")
            print("-------------LISTADO POR MARCA Y MODELO------------------")     
            for moto in motocicletas:
                if moto[1] == marca:
                    if moto[2]==modelo:
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
            conexion.miCursor.execute("SELECT marca FROM MOTOCICLETAS")
            marca = str(conexion.miCursor.fetchall())
            conexion.miCursor.execute("SELECT modelo FROM MOTOCICLETAS")
            modelo = str(conexion.miCursor.fetchall())

            conexion.miCursor.execute("UPDATE MOTOCICLETAS SET precio='{}', fechaUltimoPrecio = CURRENT_TIMESTAMP where marca='{}' and modelo='{}' ".format(self.precio,self.marca,self.modelo))
            conexion.miConexion.commit()
            print("Motocicleta/s modificada/s correctamente")
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