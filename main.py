class Datos:
    def __init__(self, Vertice, Arista, Peso):
        self.Vertice = Vertice
        self.Arista = Arista
        self.Peso = Peso
    def show(self):
        print(' Vertice = ',self.Vertice,'\n Arista = ',self.Arista,'\n Peso = ',self.Peso)

def IngresoDatos():
    print ('Ingrese los siguientes valores por pantalla')
    v=0
    a=0
    p=0
    while (v==0 or a==0 or p==0):
        try:
            v = int(input('Vertices: '))
            a = int(input('Aristas: '))
            p = int(input('Peso: '))
            break
        except ValueError: 
            print('Datos mal ingresados, intente nuevamente.......')
    DatosNuevos = Datos(v,a,p)
    return DatosNuevos
def 
def main ():
    datosNuevos = IngresoDatos()
    
    return 0

main()