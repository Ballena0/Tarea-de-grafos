from tools import Limpiar
import msvcrt

class Arista:
    peso = 0
    vertice_inicial = ""
    vertice_final = ""

def creaGrafo():

    vertices=[]
    print ("Para crear el grafo, ingrese los siguientes datos:\n")
    while(True):### Proceso para definir aristas, y de camino, el grafo.
        try:
            num_aristas = int(input("\tNumero de Aristas: "))
            aristas_grafo = [Arista() for i in range(num_aristas)]
            for i in range(0, num_aristas):
                aristas_grafo[i].peso=int(input("\tPeso de arista " + str(i+1) +": "))
                aristas_grafo[i].vertice_inicial=str(input("\tVertice inicial arista " + str(i+1) +": "))
                aristas_grafo[i].vertice_final=str(input("\tVertice final arista " + str(i+1) +": "))
            break
        except ValueError:
            print('Datos mal ingresados, intente nuevamente.......')
    Limpiar()
    for i in range(0,len(aristas_grafo)):### Recorre el arreglo de aristas (vertices iniciales), en busqueda de vertices que agregar al arreglo "vertices", si no estan agregados, los agrega.
        ya_existe=0
        if (len(vertices)==0):
            vertices.append(aristas_grafo[i].vertice_inicial)
        for j in range(0,len(vertices)):
            if (aristas_grafo[i].vertice_inicial == vertices[j]):
                ya_existe=1
        if (ya_existe==0):
            vertices.append(aristas_grafo[i].vertice_inicial)
    for i in range(0,len(aristas_grafo)):### Recorre el arreglo de aristas (vertices finales), en busqueda de vertices que agregar al arreglo "vertices", si no estan agregados, los agrega.
        ya_existe=0
        if (len(vertices)==0):
            vertices.append(aristas_grafo[i].vertice_final)
        for j in range(0,len(vertices)):
            if (aristas_grafo[i].vertice_final == vertices[j]):
                ya_existe=1
        if (ya_existe==0):
            vertices.append(aristas_grafo[i].vertice_final)
    
    while(True):### Proceso poara agregar nodos aislados al grafo.
        try:
            Limpiar()
            ya_existe=0
            nodos_aislados=int(input("¿Desea agregar nodos aislados al grafo?\n 1) Si.\n 2) No.\n\nIngrese numero de opcion: "))
            if(int(nodos_aislados)==2):
                break
            if(int(nodos_aislados)==1):
                Limpiar()
                print("Ingrese 'fin' para terminar...")
                while(True):
                    try:
                        agregar_nodo_aislado=input("Ingresar nombre del nodo: ")
                        if not(agregar_nodo_aislado=="fin"):
                            for i in range(len(vertices)):
                                if(agregar_nodo_aislado==vertices[i]):
                                    ya_existe=1
                                    print("El vertice nombrado ya esta agregado...")
                            if(ya_existe==0):
                                vertices.append(agregar_nodo_aislado)
                                print("Vertice agregado con exito...")
                            ya_existe=0
                        else:
                            break
                            
                    except ValueError:
                        print('Datos mal ingresados, intente nuevamente.......')
            if(agregar_nodo_aislado=="fin"):
                break
        except ValueError:
            print('Datos mal ingresados, intente nuevamente.......')
    Limpiar()
    print("Nombre de vertices creados:\n\n")
    for i in range(0,len(vertices)):
        print("Vertice: "+str(vertices[i]))
    print("\nProceso de creacion del grafo finalizado, presione una tecla para continuar...")
    msvcrt.getch()
    return (aristas_grafo,vertices)

