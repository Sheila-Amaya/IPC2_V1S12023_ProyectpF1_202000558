from rich.console import Console
from rich.panel import Panel
from rich.text import Text

class Menu:
    def __init__(self):
        self.console = Console()

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
        console.print("\t[red]3. Salir[/red]")

        while True: # Asegura que el menú se muestre repetidamente hasta que el usuario elija la opción de salir
            # Solicita al usuario que seleccione una opción del menú
            opcion = console.input("\n\tSeleccione una opción: ")

            if opcion == "1":
                console.print("\tHas seleccionado la opción 1.", style="green")
                print()

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
                        self.sesionUsuario()
                        print()
                        break

                    elif subopcion == "3":
                        console.print("\tVolviendo al menú principal...", style="bold yellow")
                        break

                    else:
                        console.print("\tOpción inválida. Por favor, selecciona una opción válida.", style="bold red")


            elif opcion == "2":
                console.print("\tHas seleccionado la opción 2.", style="green")
                # Aquí puedes agregar la lógica correspondiente a la opción 2

            elif opcion == "3":
                console.print("\t¡Hasta luego!\n", style="bold red")
                exit(0)

            else:
                console.print("\tOpción inválida. Por favor, selecciona una opción válida.", style="bold red")

    def sesionUsuario(self):
        usuario = self.console.input("\tIngresa tu nombre de usuario: ")
        contrasena = self.console.input("\tIngresa tu contraseña: ")

        # verifica las credenciales del administrador
        if usuario == "a" and contrasena == "a":
            print()
            self.console.print("\tIngreso exitoso como usuario.\n", style="green")
            print()
            self.menuUsuario()# metodo para iniciar sesion como administrador
        else:
            self.console.print("\tCredenciales incorrectas. Vuelve a intentarlo.\n", style="bold red")

    def menuUsuario(self):
        title = Text("\t\t      MENU USUARIO", style="bold")
        # Ajusta el padding izquierdo y derecho del panel
        panel = Panel(title, border_style="bold yellow", width=70, padding=(0, 2, 0, 2))  
        self.console.print(panel)

        # Imprime las opciones del menú 
        self.console.print("\t[cyan]1. Ver listado de películas[/cyan]")
        self.console.print("\t[red]2. Regresar[/red]")
        
        while True:  # asegura que el menú se muestre repetidamente hasta que el usuario elija la opción de salir
            # Solicita al usuario que seleccione una opción del menú
            opcion = self.console.input("\n\tSeleccione una opción: ")

            if opcion == "1":
                self.console.print("\tHas seleccionado la opción 1.", style="green")
                
            elif opcion == "2":
                self.console.print("\tVolviendo al menú principal...", style="bold yellow")
                print()
                self.mostrar_menu()

    def sesionAdmi(self):
        usuario = self.console.input("\tIngresa tu nombre de usuario: ")
        contrasena = self.console.input("\tIngresa tu contraseña: ")

        # verifica las credenciales del administrador
        if usuario == "admi" and contrasena == "admi":
            print()
            self.console.print("\tIngreso exitoso como administrador.\n", style="green")
            print()
            self.menuAdmi()# metodo para iniciar sesion como administrador
        else:
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
        self.console.print("\t[red]4. Salir[/red]")
        
        while True:  # asegura que el menú se muestre repetidamente hasta que el usuario elija la opción de salir
            # Solicita al usuario que seleccione una opción del menú
            opcion = self.console.input("\n\tSeleccione una opción: ")

            if opcion == "1":
                self.console.print("\tHas seleccionado la opción 1.", style="green")
                print()
                while True:
                    title = Text("\t\t         GESTIONAR USUARIOS", style="bold")
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
                        self.console.print("\tHas seleccionado cargar archivo.", style="green")

                    elif subopcion == "2":
                        self.console.print("\tHas seleccionado crear usuario.", style="green")
                        
                    elif subopcion == "3":
                        self.console.print("\tHas seleccionado Modificar usuario.", style="green")
                        
                    elif subopcion == "4":
                        self.console.print("\tHas seleccionado Eliminar usuarios.", style="green")
                        
                    elif subopcion == "5":
                        self.console.print("\tHas seleccionado Mostrar usuario.", style="green")

                    elif subopcion == "6":
                        self.console.print("\tVolviendo al menú principal...", style="bold yellow")
                        print()
                        self.menuAdmi()

                    else:
                        self.console.print("\tOpción inválida. Por favor, selecciona una opción válida.\n", style="bold red")

            elif opcion == "2":#GESTION DE CATEGORIAS Y PELICULAS
                self.console.print("\tHas seleccionado la opción 2.\n", style="green")
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
                        self.console.print("\tHas seleccionado cargar archivo.", style="green")

                    elif subopcion == "2":
                        self.console.print("\tHas seleccionado Añadir pelicula.", style="green")
                        
                    elif subopcion == "3":
                        self.console.print("\tHas seleccionado Modificar pelicula.", style="green")
                        
                    elif subopcion == "4":
                        self.console.print("\tHas seleccionado Eliminar pelicula.", style="green")
                        
                    elif subopcion == "5":
                        self.console.print("\tHas seleccionado Mostrar peliculas", style="green")

                    elif subopcion == "6":
                        self.console.print("\tVolviendo al menú principal...", style="bold yellow")
                        print()
                        self.menuAdmi()

                    else:
                        self.console.print("\tOpción inválida. Por favor, selecciona una opción válida.\n", style="bold red")

            elif opcion == "3": #GESTIONAR SALAS
                self.console.print("\tHas seleccionado la opción 3.", style="green")
                print()
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
                        self.console.print("\tHas seleccionado cargar archivo.", style="green")
                        print()

                    elif subopcion == "2":
                        self.console.print("\tHas seleccionado Añadir cine.", style="green")
                        print()
                        
                    elif subopcion == "3":
                        self.console.print("\tHas seleccionado Modificar cine.", style="green")
                        print()
                        
                    elif subopcion == "4":
                        self.console.print("\tHas seleccionado Eliminar cine.", style="green")
                        print()
                        
                    elif subopcion == "5":
                        self.console.print("\tHas seleccionado Mostrar cine", style="green")
                        print()

                    elif subopcion == "6":
                        self.console.print("\tVolviendo al menú principal...", style="bold yellow")
                        print()
                        self.menuAdmi()

                    else:
                        self.console.print("\tOpción inválida. Por favor, selecciona una opción válida.\n", style="bold red")

            elif opcion == "4": #SALIR PARA EL MENU DEL ADMINISTRADOR
                self.console.print("\tVolviendo al menú principal...", style="bold yellow")
                print()
                self.mostrar_menu()

            else:
                self.console.print("\tOpción inválida. Por favor, selecciona una opción válida.\n", style="bold red")

