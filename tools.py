import os

def Limpiar():
    if (os.name=='nt'): ## limpia la pantalla dependiendo del sistema operativo
        var = 'cls'
    else:
        var = 'clear'
    return os.system(var)