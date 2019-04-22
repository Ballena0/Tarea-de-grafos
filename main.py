from menu import menu
from grafo import creaGrafo

def main():

    (aristas_grafo,vertices) = creaGrafo()
    menu(aristas_grafo,vertices)
    
main()
