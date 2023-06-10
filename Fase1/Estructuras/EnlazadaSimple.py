from Estructuras.NodoS import *
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

class EnlazadaSimple():
    
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