class Datos:
    def __init__(self, Vertice, Arista, Peso, Vertices):
        self.Vertice = Vertice
        self.Arista = Arista
        self.Peso = Peso
        self.Vertices = Vertices
    def show(self):
        print(' Valores',' \n Vertices = ',self.Vertice, '\n Nombres = ',self.Vertices,'\n Aristas = ',self.Arista,'\n Peso = ',self.Peso)


def IngresoDatos():
    print ('Ingrese los siguientes valores por pantalla')
    v=0
    vN= []
    a=0
    p=[]
    while (a==0):
        try:
            v = int(input('Vertices: '))
            for i in range(0, v):
                vN.append(str(input("Nombre vertice: ")))
            a = int(input('Aristas: '))
            for i in range(0, a):
                p.append(int(input("Peso arista: ")))
            break
        except ValueError: 
            print('Datos mal ingresados, intente nuevamente.......')
    DatosNuevos = Datos(v,a,p, vN)
    return DatosNuevos.show()

#def sonAdyacentes(Datos):
#falta confirmar adyacencia




def main ():
    datosNuevos = IngresoDatos()
    ##return datosNuevos.show()
    ##Se esta retornando desde la funcion "IngresoDatos"
    #sonAdyacentes(datosNuevos)
main()