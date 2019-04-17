import os
import msvcrt
from dijstra import Grafo,Vertice

def creaGrafo():
    vN = []
    p = []
    dicc_vertices = {}
    print('Tarea 1 de grafos y lenguajes formales')
    print('Se debe ingresar los datos del grafo para realizar las operaciones posteriormente')
    while(True):
        try:
            num_ver = int(input('\tNumero de vertices: '))
            for i in range(0, num_ver):
                vN.append(str(input("\tNombre vertice " + str(i+1) +": ")))
            num_ar = int(input('\tNumero de aristas: '))
            for i in range(0,num_ar):
                p.append(int(input("\tPeso arista "+ str(i+1) +": ")))
            break
        except ValueError:
            print('Datos mal ingresados, intente nuevamente.......')
    for i in range(0,num_ver):  ## Aqui se crea el diccionario con el nombre y el vertice correspondiente. (falta agregar la adyacencia)
        x = Vertice(vN[i])
        dicc_vertices[vN[i]] = x
    Grafo1 = Grafo(num_ver,dicc_vertices)  ## pasé los datos con el constructor pero si quieres modificarlo ahi ve tu no tengo problem
    return Grafo1

def Limpiar():
    if (os.name=='nt'): ## limpia la pantalla dependiendo del sistema operativo
        var = 'cls'
    else:
        var = 'clear'
    return os.system(var)

def sonAdyacentes():
    pass
#falta confirmar adyacencia

def menu(grafo):  ## menu principal 
    salir = False  ## condicional que el while salga del ciclo
    opcion = None   ## opcion escogida
    while (not salir):
        Limpiar()
        print('Tarea 1 de Grafos y lenguajes formales')
        print('\tMenu principal')
        print('\t 1) Mostrar matriz de adyacencia') 
        print('\t 2) Verificar si un grafo es conexo')
        print('\t 3) Cantidad de caminos entre vertices')
        print('\t 4) Dijkstra')
        print('\t 9) Salir')
        opcion = int(input('Ingrese una opcion: '))
        if(opcion==1):
            Limpiar()
            print('Esta es la matriz de adyacencia del grafo')
            ##grafo.set_matriz()
            ## si tira error es porque falta setear la matriz
            grafo.mostrar_matriz()
            print("Presione una tecla para continuar...")
            msvcrt.getch()
        elif (opcion==2):
            pass
            # print("Presione una tecla para continuar...")
            # msvcrt.getch()
        elif (opcion==3):
            pass
            # print("Presione una tecla para continuar...")
            # msvcrt.getch()
        elif (opcion==4):
            pass
            # print("Presione una tecla para continuar...")
            # msvcrt.getch()
        elif (opcion==5):
            pass
            # print("Presione una tecla para continuar...")
            # msvcrt.getch()
        elif (opcion==9):
            salir=True
def main ():
    Limpiar()
    grafo = creaGrafo() ## Estoy retornando el grafo que se crea aqui 
    menu(grafo)  ## aqui lo paso por al menu general
    # datosNuevos = IngresoDatos()
    # ##return datosNuevos.show()
    # ##Se esta retornando desde la funcion "IngresoDatos"
    sonAdyacentes()

main()