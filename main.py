from menu import menu
from grafo import creaGrafo

def main():

    (aristas_grafo,vertices,tipo_grafo) = creaGrafo()
    menu(aristas_grafo,vertices,tipo_grafo)
    
main()
