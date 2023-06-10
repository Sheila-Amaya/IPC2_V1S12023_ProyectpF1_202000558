from Estructuras.NodoDE import *

class ListaDobleEnlazada:
    
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.size = 0
        
    def estaVacia(self):
        return self.primero is None
    
    def agregarUltimo(self, dato):
        if self.estaVacia():
            self.primero = self.ultimo = Nodo(dato)
        else:
            nuevo_nodo = Nodo(dato)
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
        self.size += 1
        
    def recorrerInicio(self):
        temp = self.primero
        while temp is not None:
            print("\n\tNombre cine: "+temp.dato.nombre)
            print("\tSalas: ")
            temp.dato.sala.recorrerSalas() #LISTA SIMPLE
            temp = temp.siguiente
            
    def recorrerFinal(self):
        temp = self.ultimo
        while temp is not None:
            temp = temp.anterior
            
    def size(self):
        return self.size
    
    def eliminar(self):
        if self.estaVacia():
            print("La lista está vacía")
        elif self.primero.siguiente is None:
            self.primero = self.ultimo = None
            self.size = 0
        else:
            self.primero = self.primero.siguiente
            self.primero.anterior = None
            self.size -= 1