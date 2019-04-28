from matriz import matriz_ady
from tools import Limpiar 
from grafo import Grafo_conexo,Cantidad_caminos
import msvcrt

def menu (aristas_grafo,vertices,tipo_grafo):

    salir = False  ## condicional que el while salga del ciclo
    opcion = None   ## opcion escogida
    
    while (not salir):
        Limpiar()
        print('Tarea 1 de Grafos y lenguajes formales')
        print('\tMenu principal')
        print('\t 1) Mostrar matriz de adyacencia') 
        print('\t 2) Verificar si el grafo es conexo')
        print('\t 3) Numero de caminos de largo "n" en el grafo.')
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
            matriz_ady(aristas_grafo,vertices,tipo_grafo)
            print("\nPresione una tecla para continuar...")
            msvcrt.getch()
        elif (opcion==2):
            if(Grafo_conexo(aristas_grafo,vertices,tipo_grafo)==0):
                print("\nEl grafo ingresado NO es conexo.")
            else:
                print("\nEl grafo ingresado SI es conexo.")
            print("\nPresione una tecla para continuar...")
            msvcrt.getch()
        elif (opcion==3):
            while(True):
                try:
                    largo=int(input("\nIngrese el largo de camino: "))
                    if(largo>0):
                        print("\nCantidad de caminos de largo "+str(largo)+" en el grafo:"+str(Cantidad_caminos(aristas_grafo,vertices,tipo_grafo,largo)))
                        break
                    else:
                        print('Datos mal ingresados, intente nuevamente.......')
                    
                except ValueError:
                    print('Datos mal ingresados, intente nuevamente.......')
            print("\nPresione una tecla para continuar...")
            msvcrt.getch()
        elif (opcion==4):
            pass
            print("\nPresione una tecla para continuar...")
            msvcrt.getch()
        elif (opcion==5):
            salir=True
