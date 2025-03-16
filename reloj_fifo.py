import time
from arbol import Nodo

def buscar_solucion_DFS(estado_inicial, solucion):
    nodos_visitados = []
    nodos_frontera = []
    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)
    
    while len(nodos_frontera) != 0:
        nodo = nodos_frontera.pop()
        nodos_visitados.append(nodo)
        
        if nodo.get_datos() == solucion:
            return nodo  
        
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
    
    inicio = time.perf_counter()  # Inicio de medición
    nodo_solucion = buscar_solucion_DFS(estado_inicial, solucion)
    fin = time.perf_counter()  # Fin de medición

    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo.padre is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.padre
        resultado.append(estado_inicial)

        print("Solución encontrada:")
        print(resultado[::-1])
    
    print(f"Tiempo de ejecución: {fin - inicio:.10f} segundos")