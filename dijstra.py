import sys
import heapq

class Vertice:
    def __init__(self, nodo):
        self.id = nodo
        self.adyacente = {}
        #setear peso al infito
        self.distancia = sys.maxsize
        #recorrido?
        self.recorrido = False
        #predecesor
        self.predecesor = None
    
    #nodo siguiente
    def agregar_adyacente(self, ady, peso = 0):
        self.adyacente[ady] = peso
    
    #mostrar nombre del vertice
    def get_nodo(self):
        return self.id

    #
    def mostar_peso(self, vecino):
        return self.adyacente[vecino]

    #settear distiancia
    def set_distiancia(self, dist):
        self.distancia = dist
    
    #mostrar distancia
    def get_distancia(self):
        return self.distancia
    
    #¿que nodo estaba antes?
    def set_predecesor(self, ant):
        self.predecesor = ant
    
    #mostrar nodo anterior
    def get_predecesor(self):
        return self.predecesor
    
    #este nodo ya ha sido recorrido
    def set_recorrido(self):
        self.recorrido = True

    #muestrame todos los nodos
    def __str__(self):
        return str(self.id) + 'Adyacente a : ' + str([x.id for x in self.adyacente])

class Grafo:
    def __init__(self,num_ver,dicc_vertices):  ## modifique esto para ingresar los datos en el constructor del grafo, modificalo si quieres
        self.dicc_vertices = {}
        self.num_vertices = num_ver
        self.Matriz = [] # Matriz de adyacencia del grafo 
    #iterador con un objeto de tipo "Vertice"
    def __iter__(self):
        return iter(self.dicc_vertices.values())
    
    #añade un vertice al diccionario del grafo
    def anadir_vertice(self, noda):
        self. num_vertices += 1
        nuevo_vertice = Vertice(noda)
        self.dicc_vertices[noda] = nuevo_vertice
        return nuevo_vertice

    #muestrame el Vertice "x"
    def get_verticeN(self, n):
        if n in self.dicc_vertices:
            return self.dicc_vertices[n]
        else:
            return None
    
    #desde y para pueden ser vertices no existentes
    #si los vertices no existen se crean primero 
    #finalmente se le asigna el valor a cada uno de los vertices mediante parametros
    # + el peso asignado por parametro
    def agregar_adyacencia(self, desde, para, peso = 0):
        if desde not in self.dicc_vertices:
            self.anadir_vertice(desde)
        if para not in self.dicc_vertices:
            self.anadir_vertice(para)
        
        self.dicc_vertices[desde].agregar_adyacente(self.dicc_vertices[para], peso)
        self.dicc_vertices[para].agregar_adyacente(self.dicc_vertices[desde], peso)
    
    #muestra solo los nombres de los vertices sin sus valores
    def mostrar_vertices(self):
        return self.dicc_vertices.keys()
    
    def set_predecesor(self, actual):
        self.predecesor = actual

    def get_predecesor(self):
        return self.predecesor
    def set_matriz(self):  # Crea la matriz de adyacencia llena de ceros, dada la cantidad de vertices
        for i in range(self.num_vertices):
            self.Matriz.append([0]*self.num_vertices)
    def mostrar_matriz(self): # Muestra por pantalla la matriz
         for i in range(self.num_vertices):
             print(self.Matriz[i-1])
def elmascorto(v, camino):
    ''' hace el camino mas corto desde v.predecesor'''
    if v.predecesor:
        camino.append(v.predecesor.get_nodo())
        elmascorto(v.precedesor, camino)
    return 

#ahora debemos ver el grafo como un heap


