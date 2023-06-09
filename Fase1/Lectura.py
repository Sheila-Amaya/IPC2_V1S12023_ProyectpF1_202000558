import xml.etree.ElementTree as ET
from Estructuras.EnlazadaSimple import *
from usuario import *

class Lectura():
    
    def lecturaU(ruta): #GESTIONAR USUARIOS > LISTA SIMPLE
        try:
            tree = ET.parse(ruta)
            root = tree.getroot()
            
            listaUsuario = EnlazadaSimple()
            
            for elemento in root: #root etiqueta usuarios
                
                #USUARIO
                rol = ""
                nombre = ""
                apellido = ""
                telefono = ""
                correo = ""
                contrasena = ""
                
                if elemento.tag == "usuario":
                    for subelememto in elemento: #sub elemento son las etiquetas dentro de usuario
                        #print(subelememto)
                        if subelememto.tag == "rol":
                            rol = subelememto.text
                        elif subelememto.tag == "nombre":
                            nombre = subelememto.text
                        elif subelememto.tag == "apellido":
                            apellido = subelememto.text
                        elif subelememto.tag == "telefono":
                            telefono = subelememto.text
                        elif subelememto.tag == "correo":
                            correo = subelememto.text
                        elif subelememto.tag == "contrasena":
                            contrasena = subelememto.text
                    listaUsuario.agregarUltimo(Usuario(rol,nombre,apellido,telefono,correo,contrasena))
                
            #listaUsuario.recorrer()
                
            #correo = input("ingrese el correo: ")
            #listaUsuario.eliminarPorBusqueda(correo)
            #listaUsuario.eliminarPorBusqueda(correo)
            #listaUsuario.modificarPorCorreo(correo)
            #listaUsuario.recorrer()

        except:
            print(' Error al cargar el archivo...\n')  # Mensaje de error cuando ocurre una excepción al cargar el archivo

    def lecturaCP(ruta): #CATEGORIA Y PELICULAS > DOBLE ENLAZADA CIRCULAR
        try:
            tree = ET.parse(ruta)  # Parsea el archivo XML y crea un objeto de árbol
            root = tree.getroot()  # Obtiene la etiqueta raíz del árbol
            
            
            # Itera sobre los elementos hijos de la raíz (raiz=categorias)
            for elemento in root:
                #print(root)
                # Verifica si el elemento actual tiene la etiqueta "categoria"
                if elemento.tag == "categoria":
                    # si tiene la etiqueta categoria itera sobre los subelementos de la etiqueta "categoria" -> mombre , pelicula
                    for subelemento in elemento: #itera sobre la etiqueta categorias 
                        #print(subelemento) # Imprime el subelemento actual
                        
                        #CATEGORIA
                        nombre = ""
                        #PELICULA
                        titulo = ""
                        director = ""
                        anio = 0
                        fecha = ""
                        hora = ""
                        
                        if subelemento.tag == "nombre":
                            nombre = subelemento.text
                            #print("\ncategoria nombre: "+subelemento.text+"\n") #imprime el contenido del tag
                        elif subelemento.tag == "peliculas":
                            for sub in subelemento: 
                                #print(sub) #sub es la etiqueta pelicula
                                if sub.tag == "pelicula":
                                    for s in sub: #itera sobre la etiqueta sub y extrae las sub etiquetas
                                        if s.tag == "titulo":
                                            titulo = s.text
                                        elif s.tag == "director":
                                            director = s.text
                                        elif s.tag == "anio":
                                            anio = int(s.text)
                                        elif s.tag == "fecha":
                                            fecha = s.text
                                        elif s.tag == "hora":
                                            hora = s.text
        except:
            print(' Error al cargar el archivo...\n')  # Mensaje de error cuando ocurre una excepción al cargar el archivo

    def lecturaS(ruta ): #SALAS > DOBLEMENTE ENLAZADA
        try:
            tree = ET.parse(ruta)
            root = tree.getroot()
            
            for elemento in root: #raiz = cines
                
                #CINE
                nombre = ""
                #SALAS
                numero = ""
                asientos = 0
                
                if elemento.tag == "cine":
                    for subelemento in elemento: # etiquetas dentro de cine, nombre ,salas
                        if subelemento.tag == "nombre":
                            nombre = subelemento.text
                            #print("\n"+subelemento.text)
                        if subelemento.tag == "salas":
                            for sub in subelemento:
                                if sub.tag == "sala": 
                                    for s in sub:
                                        if s.tag == "numero":
                                            numero = s.text
                                        if s.tag == "asientos":
                                            asientos = int(s.text)
            
        except:
            print(' Error al cargar el archivo...\n')  # Mensaje de error cuando ocurre una excepción al cargar el archivo


    # Llama a la función con la ruta del archivo XML
    #lecturaCP("C:\\Users\\amaya\\OneDrive\\Documents\\GitHub\\IPC2_V1S12023_ProyectpF1_202000558\\Fase1\\xml prueba\\C1.xml")
    #lecturaU("C:\\Users\\amaya\\OneDrive\\Documents\\GitHub\\IPC2_V1S12023_ProyectpF1_202000558\\Fase1\\xml prueba\\U2.xml")
    #lecturaS("C:\\Users\\amaya\\OneDrive\\Documents\\GitHub\\IPC2_V1S12023_ProyectpF1_202000558\\Fase1\\xml prueba\\S3.xml")