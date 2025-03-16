from arbol import Nodo

def buscar_solucion_BFS_rec(nodo_inicial, solucion, visitados):
    visitados.append(nodo_inicial.get_datos())

    if nodo_inicial.get_datos() == solucion:
        return nodo_inicial

    # Expandir los nodos sucesores (hijos)
    dato_nodo = nodo_inicial.get_datos()
    
    hijos = [
        [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]],  # Izquierdo
        [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]],  # Central
        [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]   # Derecho
    ]

    nodos_hijos = [Nodo(hijo, nodo_inicial) for hijo in hijos]  # Se establece el padre correctamente

    nodo_inicial.set_hijos(nodos_hijos)

    for nodo_hijo in nodo_inicial.get_hijos():
        if nodo_hijo.get_datos() not in visitados:
            # Llamada recursiva
            resultado = buscar_solucion_BFS_rec(nodo_hijo, solucion, visitados)
            if resultado is not None:
                return resultado

    return None

if __name__ == "__main__":
    estado_inicial = [4, 2, 3, 1]
    solucion = [1, 2, 3, 4]
    visitados = []
    
    nodo_inicial = Nodo(estado_inicial)
    nodo_solucion = buscar_solucion_BFS_rec(nodo_inicial, solucion, visitados)

    # Mostrar resultado
    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        
        resultado.reverse()
        print("Solución encontrada:", resultado)
    else:
        print("No se encontró una solución.")