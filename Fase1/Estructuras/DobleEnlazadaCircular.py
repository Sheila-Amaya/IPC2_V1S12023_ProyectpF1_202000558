from Estructuras.NodoDEC import *
class CicularDobleEnlazada:

    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def estaVacia(self):
        return self.primero == None
    
    def agregarFinal(self, dato):
        nuevo_nodo = Nodo(dato)  # Creamos un nuevo nodo con el dato 
        
        if self.estaVacia(): # Si la lista está vacía, el nuevo nodo se convierte en el primer y único elemento
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo  # El nuevo nodo se enlaza consigo mismo
            nuevo_nodo.anterior = nuevo_nodo  # El nuevo nodo se enlaza consigo mismo
        else: # Si la lista no está vacía, se actualizan los enlaces de los nodos existentes
            nuevo_nodo.siguiente = self.primero  # El siguiente del nuevo nodo es el primer nodo actual
            nuevo_nodo.anterior = self.ultimo  # El anterior del nuevo nodo es el último nodo actual
            self.primero.anterior = nuevo_nodo  # El anterior del primer nodo actual se actualiza al nuevo nodo
            self.ultimo.siguiente = nuevo_nodo  # El siguiente del último nodo actual se actualiza al nuevo nodo
            self.ultimo = nuevo_nodo  # Actualizamos el puntero del último nodo a ser el nuevo nodo

    def recorrerInicio(self):
        temp = self.primero
        while temp:
            print(temp.dato)  # Imprime el dato del nodo actual
            aux = aux.siguiente  # Avanza al siguiente nodo asignándolo a la variable 'aux'
            if aux == self.primero:  # Si se ha vuelto al primer nodo, se ha recorrido toda la lista
                break
            
    def buscar(self, dato):
        if self.esta_vacia():
            return False
        
        nodo_actual = self.primero
        while nodo_actual:
            if nodo_actual.dato == dato:  # Si se encuentra el dato buscado
                return True
            else:
                nodo_actual = nodo_actual.siguiente
                if nodo_actual == self.primero:  # Si se ha recorrido toda la lista sin encontrar el dato
                    return False

    def eliminar(self, dato):
        if self.esta_vacia():
            return

        nodo_actual = self.primero
        while nodo_actual:
            if nodo_actual.dato == dato:  # Si se encuentra el dato buscado
                if nodo_actual == self.primero:  # Si el nodo a eliminar es el primer nodo
                    self.primero = nodo_actual.siguiente
                    self.primero.anterior = self.ultimo
                    self.ultimo.siguiente = self.primero
                elif nodo_actual == self.ultimo:  # Si el nodo a eliminar es el último nodo
                    self.ultimo = nodo_actual.anterior
                    self.ultimo.siguiente = self.primero
                    self.primero.anterior = self.ultimo
                else:  # Si el nodo a eliminar está en medio de la lista
                    nodo_actual.anterior.siguiente = nodo_actual.siguiente
                    nodo_actual.siguiente.anterior = nodo_actual.anterior
                return
            
            nodo_actual = nodo_actual.siguiente
            if nodo_actual == self.primero:  # Si se ha recorrido toda la lista sin encontrar el dato
                return

    def recorrerPeliculas(self):
        pelicula_actual = self.primero
        while pelicula_actual:
            print()
            print("\t\tTítulo:", pelicula_actual.dato.titulo)
            print("\t\tDirector:", pelicula_actual.dato.director)
            print("\t\tAño:", pelicula_actual.dato.anio)
            print("\t\tFecha:", pelicula_actual.dato.fecha)
            print("\t\tHora:", pelicula_actual.dato.hora)
            print("\t\tPrecio (Q):", pelicula_actual.dato.precio)
            print()
            pelicula_actual = pelicula_actual.siguiente
            if pelicula_actual == self.primero:
                break