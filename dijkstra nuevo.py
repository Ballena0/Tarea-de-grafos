graph = {
        'a':{
            'b':10,
            'c':3
        },
        'b':{
            'c':1,
            'd':2
        },
        'c':{
            'b':4,
            'd':8,
            'e':2
        },
        'd':{
            'e':7
        },
        'e':{
            'd':9
        }
}
    
def dijkstra(graph,vertice_i,vertice_f):    
    dist_corta = {}
    predecesor = {}
    unseenV = graph
    infinity = 9999
    path = []

    for vertice in unseenV:
        dist_corta[vertice] = infinity
    dist_corta[vertice_i] = 0
    while unseenV:
        minVert = None
        for vertice in unseenV:
            if minVert is None:
                minVert = vertice
            elif dist_corta[vertice] < dist_corta[minVert]:
                minVert = vertice
        for Vady, peso in graph[minVert].items():
            if peso + dist_corta[minVert] < dist_corta[Vady]:
                dist_corta[Vady] = peso + dist_corta[minVert]
                predecesor[Vady] = minVert
        unseenV.pop(minVert)
    Vact = vertice_f
    while Vact!= vertice_i:
        try:
            path.insert(0,Vact)
            Vact = predecesor[Vact]
        except KeyError:
            print ('Ruta no accesible')
            break
    path.insert(0,vertice_i)
    if (dist_corta[vertice_f]!=infinity):
        print('La distancia mas corta es ' + str(dist_corta[vertice_f]))
        print('Y la ruta es ' + str(path))
dijkstra(graph,'e','a')