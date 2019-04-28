from tools import Limpiar
import msvcrt

class Arista:
    peso = 0
    vertice_inicial = ""
    vertice_final = ""

def creaGrafo():

    while(True):
        try:
            print()
            tipo_grafo= int(input("Seleccione la opcion del tipo de grafo:\n 1) Grafo/Multi-grafo\n 2) Digrafo/multi-digrafo.\n Ingrese nº  de opcion:"))
            num_aristas = int(input("\n Ingrese numero de Aristas: "))
            aristas_grafo = [Arista() for i in range(num_aristas)]
            if (tipo_grafo==1 or tipo_grafo==2):
                for i in range(0, num_aristas):
                    aristas_grafo[i].peso=int(input("\tPeso de arista " + str(i+1) +": "))
                    aristas_grafo[i].vertice_inicial=str(input("\tVertice inicial arista " + str(i+1) +": "))
                    aristas_grafo[i].vertice_final=str(input("\tVertice final arista " + str(i+1) +": "))
                break
            else:
                print('Datos de TIPO DE GRAFO mal ingresados, intente nuevamente.......')
        except ValueError:
            print('Datos mal ingresados, intente nuevamente.......')
    Limpiar()
    vertices=[]
    for i in range(0,len(aristas_grafo)):
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
            nodos_aislados=int(input("¿Desea agregar vertices aislados al grafo?\n 1) Si.\n 2) No.\n\nIngrese numero de opcion: "))
            if(int(nodos_aislados)==2):
                if (len(aristas_grafo)==0):
                    print("Debe ingresar nodos aislados, ya que no se agregaron aristas...")
                    nodos_aislados=0
                else:
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
                break
        except ValueError:
            print('Datos mal ingresados, intente nuevamente.......')


            
    Limpiar()
    print("Nombre de vertices crados:\n\n")
    for i in range(0,len(vertices)):
        print("Vertice: "+str(vertices[i]))
    print("\nProceso de creacion del grafo finalizado, presione una tecla para continuar...")
    msvcrt.getch()
    return (aristas_grafo,vertices,tipo_grafo)

def Grafo_conexo(aristas_grafo,vertices,tipo_grafo): ########################################## FUNCION NUEVA
    if(len(aristas_grafo)==0):
        return 0
    matriz = [[0 for i in range(0,len(vertices))] for j in range(0,len(vertices))]
    matriz_aux2 = [[0 for i in range(0,len(vertices))] for j in range(0,len(vertices))]
    matriz_aux1 = [[0 for i in range(0,len(vertices))] for j in range(0,len(vertices))]
    matriz_sumada = [[0 for i in range(0,len(vertices))] for j in range(0,len(vertices))]
    for i in range(0,len(aristas_grafo)):
        vertice1=aristas_grafo[i].vertice_inicial
        vertice2=aristas_grafo[i].vertice_final
        if (tipo_grafo==1):
            for j in range(0,len(vertices)):
                if(vertices[j]==vertice1):
                    for k in range(0,len(vertices)):
                        if(vertices[k]==vertice2):
                            matriz[j][k]=matriz[j][k]+1
                            matriz_aux1[j][k]=matriz_aux1[j][k]+1
                            matriz_sumada[j][k]=matriz_sumada[j][k]+1
        for j in range(0,len(vertices)):
            if(vertices[j]==vertice2):
                for k in range(0,len(vertices)):
                    if(vertices[k]==vertice1):
                        matriz[j][k]=matriz[j][k]+1
                        matriz_aux1[j][k]=matriz_aux1[j][k]+1
                        matriz_sumada[j][k]=matriz_sumada[j][k]+1
    contador=0
    for k in range(0,len(aristas_grafo)):
        for l in range(0,len(vertices)):
            for i in range(0,len(vertices)):
                suma=0
                contador1=0
                for j in range(0,len(vertices)):
                    suma=(matriz_aux1[l][j] * matriz[contador1][i])+suma
                    contador1=contador1+1
                    
                matriz_aux2[int(contador/len(vertices))][i]=suma
                matriz_sumada[int(contador/len(vertices))][i]=matriz_sumada[int(contador/len(vertices))][i]+suma
                contador=contador+1    
                if (contador==len(vertices)*len(vertices)):
                    contador=0
        for i in range(0,len(vertices)):
            for j in range(0,len(vertices)):
                matriz_aux1[i][j] = matriz_aux2[i][j]
    for a in range(0,len(vertices)):
        for b in range(0,len(vertices)):
            if(matriz_sumada[a][b]==0):
                return 0
    return 1
            
def Cantidad_caminos(aristas_grafo,vertices,tipo_grafo,largo): ########################################## FUNCION NUEVA
    if(len(aristas_grafo)==0):
        return 0
    matriz = [[0 for i in range(0,len(vertices))] for j in range(0,len(vertices))]
    matriz_aux2 = [[0 for i in range(0,len(vertices))] for j in range(0,len(vertices))]
    matriz_aux1 = [[0 for i in range(0,len(vertices))] for j in range(0,len(vertices))]
    for i in range(0,len(aristas_grafo)):
        vertice1=aristas_grafo[i].vertice_inicial
        vertice2=aristas_grafo[i].vertice_final
        if (tipo_grafo==1):
            for j in range(0,len(vertices)):
                if(vertices[j]==vertice1):
                    for k in range(0,len(vertices)):
                        if(vertices[k]==vertice2):
                            matriz[j][k]=matriz[j][k]+1
                            matriz_aux1[j][k]=matriz_aux1[j][k]+1
        for j in range(0,len(vertices)):
            if(vertices[j]==vertice2):
                for k in range(0,len(vertices)):
                    if(vertices[k]==vertice1):
                        matriz[j][k]=matriz[j][k]+1
                        matriz_aux1[j][k]=matriz_aux1[j][k]+1
    caminos=0
    if(largo==1):
        for a in range(0,len(vertices)):
            for b in range(0,len(vertices)):
                caminos=caminos+matriz[a][b]   
        return caminos
        
    contador=0
    
    for k in range(0,largo-1):
        for l in range(0,len(vertices)):
            for i in range(0,len(vertices)):
                suma=0
                contador1=0
                for j in range(0,len(vertices)):
                    suma=(matriz_aux1[l][j] * matriz[contador1][i])+suma
                    contador1=contador1+1
                matriz_aux2[int(contador/len(vertices))][i]=suma
                contador=contador+1    
                if (contador==len(vertices)*len(vertices)):
                    contador=0
        for i in range(0,len(vertices)):
            for j in range(0,len(vertices)):
                matriz_aux1[i][j] = matriz_aux2[i][j]
    for a in range(0,len(vertices)):
        for b in range(0,len(vertices)):
            caminos=caminos+matriz_aux2[a][b]   
    return caminos
              