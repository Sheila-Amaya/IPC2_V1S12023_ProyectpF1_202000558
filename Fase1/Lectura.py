import xml.etree.ElementTree as ET

def lecturaCP(ruta):
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
                    if subelemento.tag == "nombre":
                        print("\ncategoria nombre: "+subelemento.text+"\n") #imprime el contenido del tag
                    elif subelemento.tag == "peliculas":
                        for sub in subelemento: 
                            #print(sub) #sub es la etiqueta pelicula
                            if sub.tag == "pelicula":
                                for s in sub: #itera sobre la etiqueta sub y extrae las sub etiquetas
                                    if s.tag == "titulo":
                                        print(s.text)
                                    elif s.tag == "director":
                                        print(s.text)
                                    elif s.tag == "anio":
                                        print(s.text)
                                    elif s.tag == "fecha":
                                        print(s.text)
                                    elif s.tag == "hora":
                                        print(s.text+"\n")
    except:
        print(' Error al cargar el archivo...\n')  # Mensaje de error cuando ocurre una excepción al cargar el archivo

def lecturaU(ruta):
    try:
        tree = ET.parse(ruta)
        root = tree.getroot()
        
        for elemento in root: #root etiqueta usuarios
            if elemento.tag == "usuario":
                for subelememto in elemento: #sub elemento son las etiquetas dentro de usuario
                    #print(subelememto)
                    if subelememto.tag == "rol":
                        print("\n"+subelememto.text)
                    elif subelememto.tag == "nombre":
                        print(subelememto.text)
                    elif subelememto.tag == "apellido":
                        print(subelememto.text)
                    elif subelememto.tag == "telefono":
                        print(subelememto.text)
                    elif subelememto.tag == "correo":
                        print(subelememto.text)
                    elif subelememto.tag == "contrasena":
                        print(subelememto.text)
        
    except:
        print(' Error al cargar el archivo...\n')  # Mensaje de error cuando ocurre una excepción al cargar el archivo


def lecturaS(ruta ):
    try:
        tree = ET.parse(ruta)
        root = tree.getroot()
        
        for elemento in root: #raiz = cines
            if elemento.tag == "cine":
                for subelemento in elemento: # etiquetas dentro de cine, nombre ,salas
                    if subelemento.tag == "nombre":
                        print("\n"+subelemento.text)
                    if subelemento.tag == "salas":
                        for sub in subelemento:
                            if sub.tag == "sala": 
                                for s in sub:
                                    if s.tag == "numero":
                                        print(s.text)
                                    if s.tag == "asientos":
                                        print(s.text)
        
    except:
        print(' Error al cargar el archivo...\n')  # Mensaje de error cuando ocurre una excepción al cargar el archivo


# Llama a la función con la ruta del archivo XML
#lecturaCP("C:\\Users\\amaya\\OneDrive\\Documents\\GitHub\\IPC2_V1S12023_ProyectpF1_202000558\\Fase1\\xml prueba\\C1.xml")
#lecturaU("C:\\Users\\amaya\\OneDrive\\Documents\\GitHub\\IPC2_V1S12023_ProyectpF1_202000558\\Fase1\\xml prueba\\U2.xml")
lecturaS("C:\\Users\\amaya\\OneDrive\\Documents\\GitHub\\IPC2_V1S12023_ProyectpF1_202000558\\Fase1\\xml prueba\\S3.xml")