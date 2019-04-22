from matriz import matriz_ady
from tools import Limpiar 
import msvcrt

def menu (aristas_grafo,vertices):

    salir = False  ## condicional que el while salga del ciclo
    opcion = None   ## opcion escogida
    
    while (not salir):
        Limpiar()
        print('Tarea 1 de Grafos y lenguajes formales')
        print('\tMenu principal')
        print('\t 1) Mostrar matriz de adyacencia') 
        print('\t 2) Verificar si el grafo es conexo')
        print('\t 3) Cantidad de caminos entre vertices')
        print('\t 4) Dijkstra')
        print('\t 5) Salir')
        opcion = int(input('Ingrese una opcion: '))
        if(opcion==1):
            Limpiar()
            print("Matriz de adyacencia del grafo. \nColumnas y filas ordenadas de arriba/abajo, izq./der. respectivamente \nsegun la lista de vertices:\n\n")
            print("Orden de vertices: ",end="")
            for i in range(0,len(vertices)):
                print(str(vertices[i])+", ",end="")
            print("\n")
            matriz_ady(aristas_grafo,vertices)
            print("\nPresione una tecla para continuar...")
            msvcrt.getch()
        elif (opcion==2):
            pass
            print("Presione una tecla para continuar...")
            msvcrt.getch()
        elif (opcion==3):
            pass
            print("Presione una tecla para continuar...")
            msvcrt.getch()
        elif (opcion==4):
            pass
            print("Presione una tecla para continuar...")
            msvcrt.getch()
        elif (opcion==5):
            salir=True
    