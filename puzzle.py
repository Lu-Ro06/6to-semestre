# Puzzle Lineal con busqueda en amplitud
from arbol import Nodo

def buscar_solucion_BFS(estado_inicial, solucion):
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    
    while len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop(0)
        nodos_visitados.append(nodo)
        
        if nodo.get_datos() == solucion:
            return nodo  
        # Expandir los nodos hijo
        dato_nodo = nodo.get_datos()

        # Operador Izquierdo
        hijo_izquierdo = Nodo([dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]])
        hijo_izquierdo.padre = nodo
        if not hijo_izquierdo.en_lista(nodos_visitados) and not hijo_izquierdo.en_lista(nodos_frontera):
            nodos_frontera.append(hijo_izquierdo)

        # Operador Central
        hijo_central = Nodo([dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]])
        hijo_central.padre = nodo
        if not hijo_central.en_lista(nodos_visitados) and not hijo_central.en_lista(nodos_frontera):
            nodos_frontera.append(hijo_central)

        # Operador Derecho
        hijo_derecho = Nodo([dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]])
        hijo_derecho.padre = nodo
        if not hijo_derecho.en_lista(nodos_visitados) and not hijo_derecho.en_lista(nodos_frontera):
            nodos_frontera.append(hijo_derecho)

if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]
    nodo_solucion = buscar_solucion_BFS(estado_inicial, solucion)

    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo.padre is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.padre
        resultado.append(estado_inicial)

        print("solución encontrado:")
        print(resultado[::-1])
        
        #[4,2,3,1], [2,4,3,1], [2,3,4,1], [2,1,3,4], [1,2,3,4]]  