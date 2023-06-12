from Estructuras.NodoS import *
from rich.console import Console

class EnlazadaSimple:
    
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.console = Console()
    
    def estaVacia(self): #Si la lista esta vacia
        return self.primero == None #si no he agregado nada
    
    def agregarUltimo(self,dato):
        if self.estaVacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            temp = self.ultimo #guarda el dato en una variable temporal
            self.ultimo = temp.siguiente = Nodo(dato)

    def recorrer(self):
        temp = self.primero
        while temp != None:
            print("\n\tRol: "+temp.dato.rol)
            print("\tNombre: "+temp.dato.nombre)
            print("\tApellido: "+temp.dato.apellido)
            print("\tCorreo: "+temp.dato.correo)
            print("\tContraseña: "+temp.dato.contrasena+"\n")
            temp = temp.siguiente
            
    def eliminarUltimo(self):
        temp = self.primero
        while temp.siguiente != self.ultimo:
            temp = temp.siguiente
        temp.siguiente = None
        self.ultimo = temp
        
    def buscarPorCorreo(self, correo):
        #console = Console()
        temp = self.primero
        while temp:
            if temp.dato.correo == correo:
                #console.print("[/cyan]El correo {} ha sido encontrado.[/cyan]".format(correo))
                return temp.dato  # Devuelve el nodo si se encuentra el correo
            temp = temp.siguiente
        #console.print("[/red]El correo {} no ha sido encontrado.[/red]".format(correo))
        return None  # Devuelve None si no se encuentra el correo
    
    def buscarPorRol(self, rol):
        #console = Console()
        temp = self.primero
        while temp:
            if temp.dato.correo == rol:
                return temp.dato  # Devuelve el nodo si se encuentra el correo
            temp = temp.siguiente
        return None  # Devuelve None si no se encuentra el correo

    
    def modificarPorCorreo(self, correo):
        console = Console()
        temp = self.primero
        while temp:
            if temp.dato.correo == correo:
                print()
                nuevoNombre = console.input("[yellow]\tIngrese el nuevo nombre: [/yellow]")
                nuevoApellido = console.input("[yellow]\tIngrese el nuevo apellido: [/yellow]")
                nuevoTelefono = console.input("[yellow]\tIngrese el nuevo teléfono: [/yellow]")
                nuevoCorreo = console.input("[yellow]\tIngrese el nuevo correo: [/yellow]")
                nuevaContrasena = console.input("[yellow]\tIngrese la nueva contraseña: [/yellow]")
                
                temp.dato.nombre = nuevoNombre
                temp.dato.apellido = nuevoApellido
                temp.dato.telefono = nuevoTelefono
                temp.dato.correo = nuevoCorreo
                temp.dato.contrasena = nuevaContrasena
                
                console.print("[cyan]\tLos datos del correo {} han sido modificados.\n[/cyan]".format(correo))
                return True
            temp = temp.siguiente
        
        console.print("[/red]El correo {} no ha sido encontrado.[/red]".format(correo))
        return False

    def eliminarPorCorreo(self, correo):
        temp = self.primero
        previo = None
        
        while temp:
            if temp.dato.correo == correo:
                if previo:
                    previo.siguiente = temp.siguiente
                    if temp == self.ultimo:
                        self.ultimo = previo
                else:
                    self.primero = temp.siguiente
                    if temp == self.ultimo:
                        self.ultimo = None
                print("La información correspondiente al correo {} ha sido eliminada del sistema.".format(correo))
                return
            previo = temp
            temp = temp.siguiente
        
        print("No se encontró ninguna información correspondiente al correo {} en el sistema.".format(correo))
        
    def recorrerSalas(self): #Lista almacenada dentro de una LD
        temp = self.primero
        while temp != None:
            print("\n\t\tNumero: "+temp.dato.num)
            print("\t\tAsientos: "+temp.dato.asientos+"\n")
            temp = temp.siguiente
            
    def modificarSalas(self):
        opcion = 's'
        while opcion.lower() == 's':
            nombre_sala = input("\n\tIngrese el numero de la sala a modificar: ")
            temp = self.primero
            while temp is not None:
                if temp.dato.num == nombre_sala:
                    print("\n\tDatos actuales de la sala:")
                    print("\tNúmero: " + temp.dato.num)
                    print("\tAsientos: " + temp.dato.asientos+"\n")

                    print("\n\tIngrese los nuevos datos de la sala:")
                    nuevo_numero = input("\tNuevo número: ")
                    nuevo_asientos = input("\tNuevo número de asientos: ")

                    temp.dato.num = nuevo_numero
                    temp.dato.asientos = nuevo_asientos

                    break

                temp = temp.siguiente

            if temp is None:
                print("\tNo se encontró la sala en la lista")

            opcion = input("\t¿Desea modificar otra sala? (s/n): ")

    def recorrerCategorias(self):
        temp = self.primero
        while temp:
            print("\n\tNombre de la categoría:", temp.dato.nombre)
            print("\tPeliculas:")
            temp.dato.pelicula.recorrerPeliculas()  # Llama al método recorrerPeliculas de la lista doblemente circular enlazada
            temp = temp.siguiente
            if temp == self.primero:
                break

    def mostrarPeliculas(self):
        temp = self.primero
        contador = 1
        while temp:
            print("\n\tCategoría:", temp.dato.nombre)
            pelicula_actual = temp.dato.pelicula.primero
            while pelicula_actual: #Recorrido de la DEC
                print("\t\t",contador,". Título:", pelicula_actual.dato.titulo)
                pelicula_actual = pelicula_actual.siguiente
                if pelicula_actual == temp.dato.pelicula.primero:
                    break
                contador += 1
            temp = temp.siguiente
            if temp == self.primero:
                break

    def buscarPorCategoria(self, categoria):
        #console = Console()
        temp = self.primero
        while temp:
            if temp.dato.nombre == categoria:
                return temp.dato  # Devuelve el nodo si se encuentra el correo
            temp = temp.siguiente
        return None  # Devuelve None si no se encuentra el correo

    def buscarCategoria(self, categoria):
        if self.estaVacia():
            print("La lista está vacía")
        else:
            temp = self.primero
            while temp is not None:
                if temp.dato.nombre == categoria:  # se busca el elemento a través de su atributo
                    # Mostrar los datos actuales 
                    print("\n\tDatos actuales de la categoria:")
                    print("\tNombre categoria: " + temp.dato.nombre)
                    print("\tPeliculas:")
                    temp.dato.pelicula.recorrerPeliculas()  
                    
                    # Solicitar los nuevos datos de la categoria
                    print("\tIngrese los nuevos de la categoria:")
                    nuevo_nombre = input("\tNombre: ")
                    
                    # Modificar los datos del cine
                    temp.dato.nombre = nuevo_nombre
                    # Modificar las salas del cine
                    opcion = input("\nDesea modificar las peliculas de la categoria? (s/n): ")
                    if opcion.lower() == "s":
                        temp.dato.pelicula.modificarPeliculas()
                        
                    print("\n\tElemento modificado")
                    return
                temp = temp.siguiente
            print("\n\tNo se encontró el elemento en la lista")

    def eliminarPorCategoria(self, categoria):
        temp = self.primero
        previo = None
        
        while temp:
            if temp.dato.nombre == categoria:
                if previo:
                    previo.siguiente = temp.siguiente
                    if temp == self.ultimo:
                        self.ultimo = previo
                else:
                    self.primero = temp.siguiente
                    if temp == self.ultimo:
                        self.ultimo = None
                print("\tLa información correspondiente a la categoria {} ha sido eliminada del sistema.".format(categoria))
                return
            previo = temp
            temp = temp.siguiente
        
        print("\tNo se encontró ninguna información correspondiente a la categoria {} en el sistema.".format(categoria))
        

