

def matriz_ady(aristas_grafo,vertices,tipo_grafo): 
    matriz = [[0 for i in range(0,len(vertices))] for j in range(0,len(vertices))]
    for i in range(0,len(aristas_grafo)):
        vertice1=aristas_grafo[i].vertice_inicial
        vertice2=aristas_grafo[i].vertice_final
        if (tipo_grafo==1):
            for j in range(0,len(vertices)):
                if(vertices[j]==vertice1):
                    for k in range(0,len(vertices)):
                        if(vertices[k]==vertice2):
                            matriz[j][k]=matriz[j][k]+1
        for j in range(0,len(vertices)):
            if(vertices[j]==vertice2):
                for k in range(0,len(vertices)):
                    if(vertices[k]==vertice1):
                        matriz[j][k]=matriz[j][k]+1
    for i in range(0,len(vertices)):
        print(" ")
        for j in range(0,len(vertices)):
            print(str(matriz[i][j])+" ",end="")
    print("\n")
    pass

    