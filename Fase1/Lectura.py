import xml.etree.ElementTree as ET
from Estructuras.EnlazadaSimple import *
from usuario import *
from Estructuras.DobleEnlazada import *
from cine import *
from sala import *
from Estructuras.DobleEnlazadaCircular import *
from categoria import *
from pelicula import *

class Lectura:
    
    def lecturaU(self,ruta): #GESTIONAR USUARIOS > LISTA SIMPLE
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
            return listaUsuario

        except:
            print(' Error al cargar el archivo...\n')  # Mensaje de error cuando ocurre una excepción al cargar el archivo

    def lecturaS(self, ruta): #SALAS > DOBLEMENTE ENLAZADA
        try:
            tree = ET.parse(ruta)
            root = tree.getroot()

            listaCine = ListaDobleEnlazada()

            for elemento in root: #raiz = cines
                #CINE
                nombre = ""
                #SALAS
                salas = EnlazadaSimple()

                if elemento.tag == "cine":
                    for subelemento in elemento: # etiquetas dentro de cine, nombre, salas
                        if subelemento.tag == "nombre":
                            nombre = subelemento.text
                        if subelemento.tag == "salas":
                            for sub in subelemento:
                                if sub.tag == "sala": 
                                    numero = ""
                                    asientos = ""
                                    for s in sub:
                                        if s.tag == "numero":
                                            numero = s.text
                                        if s.tag == "asientos":
                                            asientos = s.text
                                    salas.agregarUltimo(Sala(numero, asientos))
                    listaCine.agregarUltimo(Cine(nombre, salas))

            #listaCine.recorrerInicio()
            #cine = input("ingrese el cine: ")
            #listaCine.eliminarPorCine(cine)
            #listaCine.modificarPorCine(cine)
            
            #listaCine.recorrerInicio()

            return listaCine, salas
        except:
            print('Error al cargar el archivo...\n')  # Mensaje de error cuando ocurre una excepción al cargar el archivo

    def lecturaCP(self, ruta):
        try:
            tree = ET.parse(ruta)  # Parsea el archivo XML y crea un objeto de árbol
            root = tree.getroot()  # Obtiene la etiqueta raíz del árbol
            
            listaCategorias = EnlazadaSimple()
            
            # Itera sobre los elementos hijos de la raíz (raiz=categorias)
            for elemento in root:
                # Verifica si el elemento actual tiene la etiqueta "categoria"
                if elemento.tag == "categoria":
                    nombre = ""
                    listaPeliculas = CicularDobleEnlazada()  # Crea una nueva instancia de la lista de películas para cada categoría
                    
                    # Itera sobre los subelementos de la etiqueta "categoria" -> nombre, peliculas
                    for subelemento in elemento:
                        if subelemento.tag == "nombre":
                            nombre = subelemento.text
                        
                        elif subelemento.tag == "peliculas":
                            # Itera sobre las etiquetas "pelicula" dentro de "peliculas"
                            for sub in subelemento:
                                if sub.tag == "pelicula":
                                    titulo = ""
                                    director = ""
                                    anio = ""
                                    fecha = ""
                                    hora = ""
                                    precio = float(42)
                                    
                                    # Itera sobre las subetiquetas de "pelicula" y extrae los datos
                                    for s in sub:
                                        if s.tag == "titulo":
                                            titulo = s.text
                                        elif s.tag == "director":
                                            director = s.text
                                        elif s.tag == "anio":
                                            anio = s.text
                                        elif s.tag == "fecha":
                                            fecha = s.text
                                        elif s.tag == "hora":
                                            hora = s.text
                                    
                                    listaPeliculas.agregarFinal(Pelicula(titulo, director, anio, fecha, hora, precio))
                    
                    listaCategorias.agregarUltimo(Categoria(nombre, listaPeliculas))
            
            #listaCategorias.recorrerCategorias()
            
            return listaCategorias, listaPeliculas
        
        except Exception as e:
            print('Error al cargar el archivo')
            
#ruta = r"C:\Users\amaya\OneDrive\Documents\GitHub\IPC2_V1S12023_ProyectpF1_202000558\Fase1\xml prueba\C1.xml"
#lector = Lectura()
#lista = lector.lecturaCP(ruta)