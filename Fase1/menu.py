from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from Estructuras.EnlazadaSimple import *
from Lectura import *
from usuario import *
from Estructuras.DobleEnlazada import *
from cine import *
from sala import *

lector = Lectura() #variable global
class Menu:
    listaUsuario = EnlazadaSimple()
    listaCine = ListaDobleEnlazada()
    listaSala = EnlazadaSimple()
    
    def __init__(self):
        self.console = Console()
        self.admiPorDefecto() #para que se inicialice al ejecutar el programa
    
    def admiPorDefecto(self):
        #se crea el administrador por defecto al iniciar el programa
        rol = "administrador"
        nombre = "admi"
        apellido = "administrador por defecto"
        telefono = "3834657892"
        correo = " admi@gmail.com"
        contrasena = "123"
        self.listaUsuario.agregarUltimo(Usuario(rol,nombre,apellido,telefono,correo,contrasena))

    def mostrar_menu(self):
        console = Console()

        # Imprime el título del panel 
        print()
        title = Text("\t\t    BIENVENIDO USAC-cinema", style="bold")
        # Ajusta el padding izquierdo y derecho del panel
        panel = Panel(title, border_style="bold cyan", width=70, padding=(0, 2, 0, 2))
        console.print(panel)

        # Imprime las opciones del menú 
        console.print("\t[cyan]1. Iniciar sesión[/cyan]")
        console.print("\t[cyan]2. Registrar usuario[/cyan]")
        console.print("\t[cyan]3. Ver listado de películas[/cyan]")
        console.print("\t[red]4. Salir[/red]")

        while True: # Asegura que el menú se muestre repetidamente hasta que el usuario elija la opción de salir
            # Solicita al usuario que seleccione una opción del menú
            opcion = console.input("\n\tSeleccione una opción: ")

            if opcion == "1":
                console.print("\tHas seleccionado la opción 1.\n", style="green")

                while True:
                    title = Text("\t\t        INICIAR SESION", style="bold")
                    panel = Panel(title, border_style="bold green", width=70, padding=(0, 2, 0, 2))
                    console.print(panel)
                    console.print("\t[cyan]1. Iniciar sesión como administrador[/cyan]")
                    console.print("\t[cyan]2. Iniciar sesión como usuario[/cyan]")
                    console.print("\t[red]3. Volver al menú principal[/red]")

                    subopcion = console.input("\n\tSeleccione una opción del menú: ")

                    if subopcion == "1":
                        console.print("\tHas seleccionado Iniciar sesión como administrador.\n", style="green bold")
                        self.sesionAdmi()
                        print()
                        break

                    elif subopcion == "2":
                        console.print("\tHas seleccionado Iniciar sesión como usuario.\n", style="green")
                        # Iniciar sesión como usuario
                        self.sesionCliente()
                        print()
                        break

                    elif subopcion == "3":
                        console.print("\tVolviendo al menú principal...", style="bold yellow")
                        self.mostrar_menu()
                        break

                    else:
                        console.print("\tOpción inválida. Por favor, selecciona una opción válida.", style="bold red")

            elif opcion == "2": #REGISTRAR USUARIO
                console.print("\tHas seleccionado la opción 2.", style="green")
                self.registrarUsuario()
                break
                
            elif opcion == "3": #VER PELICULAS
                console.print("\tHas seleccionado la opción 3.", style="green")
                self.verPeliculas()
                break

            elif opcion == "4":
                console.print("\t¡Hasta luego!\n", style="bold red")
                exit(0)

            else:
                console.print("\tOpción inválida. Por favor, selecciona una opción válida.", style="bold red")

    def verPeliculas():
        pass

    def sesionCliente(self):
        nombre_usuario = self.console.input("\tIngresa tu nombre de usuario: ")
        contrasena = self.console.input("\tIngresa tu contraseña: ")

        temp = self.listaUsuario.primero
        while temp:
            if temp.dato.rol == "cliente" and temp.dato.nombre == nombre_usuario and temp.dato.contrasena == contrasena:
                self.console.print("\n\tIngreso exitoso como cliente.\n", style="green")
                self.menuCliente()  # Método para iniciar sesión como administrador
                print()
                return
            temp = temp.siguiente

        self.console.print("\tCredenciales incorrectas. Vuelve a intentarlo.\n", style="bold red")

    def menuCliente(self):
        title = Text("\t\t       MENU USUARIO", style="bold")
        # Ajusta el padding izquierdo y derecho del panel
        panel = Panel(title, border_style="bold yellow", width=70, padding=(0, 2, 0, 2))  
        self.console.print(panel)

        # Imprime las opciones del menú 
        self.console.print("\t[cyan]1. Ver listado de películas[/cyan]")
        self.console.print("\t[cyan]2.Listado de películas favoritas[/cyan]")
        self.console.print("\t[cyan]3.Comprar boletos[/cyan]")
        self.console.print("\t[cyan]4.Historial de boletos comprados[/cyan]")
        self.console.print("\t[red]5. Regresar[/red]")
        
        while True:  # asegura que el menú se muestre repetidamente hasta que el usuario elija la opción de salir
            # Solicita al usuario que seleccione una opción del menú
            opcion = self.console.input("\n\tSeleccione una opción: ")

            if opcion == "1":
                self.console.print("\tHas seleccionado la opción 1.", style="green")
            elif opcion == "2":
                self.console.print("\tVolviendo al menú principal...", style="bold yellow")
                print()
            elif opcion == "3":
                self.console.print("\tVolviendo al menú principal...", style="bold yellow")
                print()
            elif opcion == "4":
                self.console.print("\tVolviendo al menú principal...", style="bold yellow")
                print() 
            elif opcion == "5":
                self.console.print("\tVolviendo al menú principal...", style="bold yellow")
                print()
                self.mostrar_menu()

    def sesionAdmi(self):
        nombre_usuario = self.console.input("\tIngresa tu nombre de usuario: ")
        contrasena = self.console.input("\tIngresa tu contraseña: ")

        temp = self.listaUsuario.primero
        while temp:
            if temp.dato.rol == "administrador" and temp.dato.nombre == nombre_usuario and temp.dato.contrasena == contrasena:
                print()
                self.console.print("\tIngreso exitoso como administrador.\n", style="green")
                print()
                self.menuAdmi()  # Método para iniciar sesión como administrador
                return
            temp = temp.siguiente

        self.console.print("\tCredenciales incorrectas. Vuelve a intentarlo.\n", style="bold red")

    def menuAdmi(self):
        # Imprime el título del panel 
        title = Text("\t\t     MENU ADMINISTRADOR", style="bold")
        # Ajusta el padding izquierdo y derecho del panel
        panel = Panel(title, border_style="bold magenta", width=70, padding=(0, 2, 0, 2))  
        self.console.print(panel)

        # Imprime las opciones del menú 
        self.console.print("\t[cyan]1. Gestionar Usuarios[/cyan]")
        self.console.print("\t[cyan]2. Gestionar Categorías y películas[/cyan]")
        self.console.print("\t[cyan]3. Gestionar Salas[/cyan]")
        self.console.print("\t[cyan]4. Gestionar boletos comprados[/cyan]")
        self.console.print("\t[red]5. Regresar[/red]")
        
        while True:  # asegura que el menú se muestre repetidamente hasta que el usuario elija la opción de salir
            # Solicita al usuario que seleccione una opción del menú
            opcion = self.console.input("\n\tSeleccione una opción: ")

            if opcion == "1": #GESTION USUARIOS
                self.console.print("\tHas seleccionado la opción 1.\n", style="green")
                self.gestionUsuarios()
                
            elif opcion == "2":#GESTION DE CATEGORIAS Y PELICULAS
                self.console.print("\tHas seleccionado la opción 2.\n", style="green")
                self.gestionarCategorias()

            elif opcion == "3": #GESTIONAR SALAS
                self.console.print("\tHas seleccionado la opción 3.\n", style="green")
                self.gestionarSalas()
                
            elif opcion == "4": #GESTIONAR BOLETOS
                self.console.print("\tHas seleccionado la opción 4.\n", style="green")
                self.gestionarBoletos()

            elif opcion == "": #SALIR PARA EL MENU DEL ADMINISTRADOR
                self.console.print("\tVolviendo al menú principal...", style="bold yellow")
                print()
                self.mostrar_menu()

            else:
                self.console.print("\tOpción inválida. Por favor, selecciona una opción válida.\n", style="bold red")

    def registrarUsuario(self): #Clientes unicamente
        self.console.print("[cyan]\n\tIngrese los datos para el usuario nuevo: \n[/cyan]")

        rol = "cliente"
        nombre = input("\tNombre: ")
        apellido = input("\tApellido: ")
        telefono = input("\tTeléfono: ")
        correo = input("\tCorreo: ")
        contrasena = input("\tContraseña: ")

        # Validar si el correo ya existe en la lista
        if self.listaUsuario.buscarPorCorreo(correo) is not None:
            self.console.print("[red]\n\tYa existe un usuario con el correo ingresado.[/red]\n")
        else:
            self.listaUsuario.agregarUltimo(Usuario(rol, nombre, apellido, telefono, correo, contrasena))
            self.console.print("[green]\n\tUsuario agregado con éxito.[/green]\n")
        self.mostrar_menu()

    def gestionUsuarios(self):
        while True:
                    title = Text("\t\t       GESTIONAR USUARIOS", style="bold")
                    panel = Panel(title, border_style="bold magenta", width=70, padding=(0, 2, 0, 2))  
                    self.console.print(panel)
                    self.console.print("\t[cyan]1. Cargar Archivo [/cyan]")
                    self.console.print("\t[cyan]2. Crear usuario[/cyan]")
                    self.console.print("\t[cyan]3. Modificar usuario[/cyan]")
                    self.console.print("\t[cyan]4. Eliminar usuario[/cyan]")
                    self.console.print("\t[cyan]5. Mostrar usuarios[/cyan]")
                    self.console.print("\t[red]6. Volver al menú principal[/red]")
                        
                    subopcion = self.console.input("\n\tSeleccione una opción: ")

                    if subopcion == "1":
                        self.console.print("\tHas seleccionado cargar archivo.\n", style="green")
                        self.cargarArchivoUsuario()

                    elif subopcion == "2":
                        self.console.print("\tHas seleccionado crear usuario.\n", style="green")
                        self.agregarUsuario()
                        
                    elif subopcion == "3":
                        self.console.print("\tHas seleccionado Modificar usuario.\n", style="green")
                        self.modificarUsuario()
                        
                    elif subopcion == "4":
                        self.console.print("\tHas seleccionado Eliminar usuarios.\n", style="green")
                        self.eliminarUsuario()
                        
                    elif subopcion == "5":
                        self.console.print("\tHas seleccionado Mostrar usuario.\n", style="green")
                        self.mostrarUsuario()
                    
                    elif subopcion == "6":
                        self.console.print("\tVolviendo al menú principal...", style="bold yellow")
                        print()
                        self.menuAdmi()

                    else:
                        self.console.print("\tOpción inválida. Por favor, selecciona una opción válida.\n", style="bold red")

    def cargarArchivoUsuario(self):
        console = Console()
        while True:
            console.print("\tIngrese la ruta del archivo: ", style="bold yellow")
            ruta = input('\t »  ')
            
            datosArchivo = lector.lecturaU(ruta)
            
            if self.listaUsuario.estaVacia():
                # Si la lista está vacía, simplemente asignar los datos del archivo a la lista
                self.listaUsuario = datosArchivo
            else:
                # Si la lista no está vacía, agregar los datos del archivo al final de la lista existente
                ultimoNodo = self.listaUsuario.ultimo
                ultimoNodo.siguiente = datosArchivo.primero
                self.listaUsuario.ultimo = datosArchivo.ultimo
            
            console.print("\t[green]Archivo cargado exitosamente.[/green]")

            opcion = input("\n\tDesea agregar otro archivo? (s/n): ")
            if opcion.lower() != "s\n":
                break
        self.gestionUsuarios()

    def agregarUsuario(self):
        self.console.print("[cyan]\tIngrese los datos del usuario: [/cyan]")

        rol = input("\tRol: ")
        nombre = input("\tNombre: ")
        apellido = input("\tApellido: ")
        telefono = input("\tTeléfono: ")
        correo = input("\tCorreo: ")
        contrasena = input("\tContraseña: ")

        # Validar si el correo ya existe en la lista
        if self.listaUsuario.buscarPorCorreo(correo) is not None:
            self.console.print("[red]\n\tYa existe un usuario con el correo ingresado.[/red]\n")
        else:
            self.listaUsuario.agregarUltimo(Usuario(rol, nombre, apellido, telefono, correo, contrasena))
            self.console.print("[green]\n\tUsuario agregado con éxito.[/green]\n")
        self.gestionUsuarios()

    def modificarUsuario(self):
        self.console.print("[cyan]\tIngrese el correo del usuario el cual desea modificar: [/cyan]")
        correo = input("\tCorreo: ")
        self.listaUsuario.modificarPorCorreo(correo)

    def eliminarUsuario(self):
        self.console.print("[cyan]\tIngrese el correo del usuario el cual desea eliminar: [/cyan]")
        correo = input("\tCorreo: ")
        self.listaUsuario.eliminarPorCorreo(correo)

    def mostrarUsuario(self):
        if self.listaUsuario is not None:
            self.listaUsuario.recorrer()
        else:
            print("\tNo se encontraron datos disponibles.\n")

    def gestionarSalas(self):
        while True:
                    title = Text("\t\t        GESTIONAR SALAS", style="bold")
                    panel = Panel(title, border_style="bold magenta", width=70, padding=(0, 2, 0, 2))  
                    self.console.print(panel)
                    self.console.print("\t[cyan]1. Cargar Archivo [/cyan]")
                    self.console.print("\t[cyan]2. Añadir cine[/cyan]")
                    self.console.print("\t[cyan]3. Modificar cine[/cyan]")
                    self.console.print("\t[cyan]4. Eliminar cine[/cyan]")
                    self.console.print("\t[cyan]5. Mostrar cines[/cyan]")
                    self.console.print("\t[red]6. Volver al menú principal[/red]")
                        
                    subopcion = self.console.input("\n\tSeleccione una opción: ")

                    if subopcion == "1":
                        self.console.print("\tHas seleccionado cargar archivo.\n", style="green")
                        self.cargarArhivosSala()

                    elif subopcion == "2":
                        self.console.print("\tHas seleccionado Añadir cine.\n", style="green")
                        self.agregarSala()
                        
                    elif subopcion == "3":
                        self.console.print("\tHas seleccionado Modificar cine.\n", style="green")
                        self.modificarSala()
                        
                    elif subopcion == "4":
                        self.console.print("\tHas seleccionado Eliminar cine.\n", style="green")
                        self.eliminarSala()
                        
                    elif subopcion == "5":
                        self.console.print("\tHas seleccionado Mostrar cine.\n", style="green")
                        self.mostrarSala()

                    elif subopcion == "6":
                        self.console.print("\tVolviendo al menú principal...", style="bold yellow")
                        print()
                        self.menuAdmi()

                    else:
                        self.console.print("\tOpción inválida. Por favor, selecciona una opción válida.\n", style="bold red")

    def cargarArhivosSala(self):
        console = Console()
        lector = Lectura()  # Crear una instancia de la clase Lectura
        while True:
            console.print("\tIngrese la ruta del archivo: ", style="bold yellow")
            ruta = input('\t »  ')
            
            resultado = lector.lecturaS(ruta)  # Obtener el resultado de la función lecturaS

            if resultado is not None:
                self.listaCine, self.listaSala = resultado  # Desempaquetar los resultados en las variables
                console.print("\t[green]Archivo cargado exitosamente.[/green]")
            else:
                console.print("\t[red]Error al cargar el archivo.[/red]")
            
            opcion = input("\n\tDesea agregar otro archivo? (s/n): ")
            if opcion.lower() != "s\n":
                break
        self.gestionarSalas()

    def agregarSala(self):
        self.console.print("[cyan]\n\tIngrese los datos para el cine nuevo: \n[/cyan]")

        nombre = input("\tNombre del cine: ")

        # Buscar el cine por nombre en la lista
        cine = self.listaCine.buscarCine(nombre)

        if cine is not None:
            opcion = input("\n\tEl cine ya existe. ¿Desea agregar más salas al cine? (s/n): ")
            if opcion.lower() == "s":
                while True:
                    numero = input("\tNúmero de sala: ")
                    asientos = input("\tCantidad de asientos: ")

                    sala = Sala(numero, asientos)

                    cine.sala.agregarUltimo(sala)

                    opcion = input("\n\t¿Desea agregar otra sala al cine? (s/n): ")
                    print()
                    if opcion.lower() != "s":
                        break
                self.console.print("[green]\n\tSalas agregadas con éxito al cine existente.[/green]\n")
            else:
                self.console.print("[yellow]\n\tNo se agregaron nuevas salas al cine existente.[/yellow]\n")
        else:
            # El cine no existe, se agrega uno nuevo con su lista de salas
            salas = EnlazadaSimple()
            while True:
                numero = input("\tNúmero de sala: ")
                asientos = input("\tCantidad de asientos: ")

                sala = Sala(numero, asientos)

                salas.agregarUltimo(sala)

                opcion = input("\n\t¿Desea agregar otra sala al cine? (s/n): ")
                if opcion.lower() != "s":
                    break
            self.listaCine.agregarUltimo(Cine(nombre, salas))
            self.console.print("[green]\n\tCine y salas agregados con éxito.[/green]\n")

        self.gestionarSalas()

        self.gestionarSalas()

    def modificarSala(self):
        self.console.print("[cyan]\tIngrese el nombre del cine el cual desea modificar: [/cyan]")
        cine = input("\tNombre del Cine: ")
        self.listaCine.modificarPorCine(cine)

    def eliminarSala(self):
        self.console.print("[cyan]\tIngrese el nombre del cine el cual desea eliminar: [/cyan]")
        cine = input("\tNombre del Cine: ")
        self.listaCine.eliminarPorCine(cine)

    def mostrarSala(self):
        if self.listaCine is not None:
            self.listaCine.recorrerInicio()
        else:
            print("\tNo se encontraron datos disponibles.\n")

    def gestionarCategorias(self):
        while True:
                    title = Text("\t\t   GESTIONAR CATEGORIAS Y PELICULAS", style="bold")
                    panel = Panel(title, border_style="bold magenta", width=70, padding=(0, 2, 0, 2))  
                    self.console.print(panel)
                    self.console.print("\t[cyan]1. Cargar Archivo [/cyan]")
                    self.console.print("\t[cyan]2. Añadir pelicula[/cyan]")
                    self.console.print("\t[cyan]3. Modificar pelicula[/cyan]")
                    self.console.print("\t[cyan]4. Eliminar pelicula[/cyan]")
                    self.console.print("\t[cyan]5. Mostrar peliculas[/cyan]")
                    self.console.print("\t[red]6. Volver al menú principal[/red]")
                        
                    subopcion = self.console.input("\n\tSeleccione una opción: ")

                    if subopcion == "1":
                        self.console.print("\tHas seleccionado cargar archivo.\n", style="green")
                        self.cargarArhivosCategorias()

                    elif subopcion == "2":
                        self.console.print("\tHas seleccionado Añadir pelicula.\n", style="green")
                        self.agregarCategoria()
                        
                    elif subopcion == "3":
                        self.console.print("\tHas seleccionado Modificar pelicula.\n", style="green")
                        self.modificarCategoria()
                        
                    elif subopcion == "4":
                        self.console.print("\tHas seleccionado Eliminar pelicula.\n", style="green")
                        self.eliminarCategoria()
                        
                    elif subopcion == "5":
                        self.console.print("\tHas seleccionado Mostrar peliculas.\n", style="green")
                        self.modificarCategoria()

                    elif subopcion == "6":
                        self.console.print("\tVolviendo al menú principal...\n", style="bold yellow")
                        self.menuAdmi()

                    else:
                        self.console.print("\tOpción inválida. Por favor, selecciona una opción válida.\n", style="bold red")

    def cargarArhivosCategorias(self):
        pass
    def agregarCategoria(self):
        pass
    def modificarCategoria(self):
        pass
    def modificarCategoria(self):
        pass
    def eliminarCategoria(self):
        pass
    def mostrarCategoria(self):
        pass

    def gestionarBoletos(self):
        pass
