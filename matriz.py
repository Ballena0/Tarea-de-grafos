

def matriz_ady(aristas_grafo,vertices): ### Imprime la matriz de adyacencia del grafo, imprimira solo los numeros ordenados como matriz.
    rango=int(len(vertices))
    matriz = [[0 for i in range(0,rango)] for j in range(0,rango)]
    for i in range(0,len(aristas_grafo)):### Recorre el arreglo de aristas, selecciona los vertices de los extremos de cada arista y los compara en el arreglo de vertices para encontrar la posicion donde colocar un "1" en la matriz.
        vertice1=aristas_grafo[i].vertice_inicial
        vertice2=aristas_grafo[i].vertice_final
        for j in range(0,len(vertices)):### Coloca "unos" en la matriz segun adyacencia de nodos, en el primer sentido.
            if(vertices[j]==vertice1):
                for k in range(0,len(vertices)):
                    if(vertices[k]==vertice2):
                        matriz[j][k]=1
        for j in range(0,len(vertices)):### Coloca "unos" en la matriz segun adyacencia de nodos, en el segundo sentido.
            if(vertices[j]==vertice2):
                for k in range(0,len(vertices)):
                    if(vertices[k]==vertice1):
                        matriz[j][k]=1
    for i in range(0,len(vertices)):### Imprime la matriz de adyacencia recorriendola slot a slot
        print(" ")
        for j in range(0,len(vertices)):
            print(str(matriz[i][j])+" ",end="")
    print("\n")
    pass
    