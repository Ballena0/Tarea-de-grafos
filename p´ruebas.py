graph = {   # ASI TIENE QUE QUEDAR EL GRAFO
        'a':{
            'b':10,
            'c':3
        },
        'b':{
            'c':1,
            'd':2
        },
        'h':{
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

print ("c" in graph.keys())