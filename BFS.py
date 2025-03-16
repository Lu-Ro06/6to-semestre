class Nodo:
    def __init__(self, datos, padre=None):
        self.datos = datos
        self.padre = padre
        self.hijos = []

    def get_datos(self):
        return self.datos

    def get_padre(self):
        return self.padre

    def set_hijos(self, hijos):
        self.hijos = hijos

    def en_lista(self, lista_nodos):
        return any(nodo.get_datos() == self.datos for nodo in lista_nodos)


def buscar_solucion_BFS(conexiones, estado_inicial, solucion):
    nodos_visitados = []
    nodos_frontera = []

    nodoInicial = Nodo(estado_inicial)
    nodos_frontera.append(nodoInicial)

    while nodos_frontera:
        nodo = nodos_frontera.pop(0)  
        nodos_visitados.append(nodo)

        if nodo.get_datos() == solucion:
            return nodo 

        # Expandir nodos hijos
        dato_nodo = nodo.get_datos()
        lista_hijos = []

        for un_hijo in conexiones.get(dato_nodo, []):  
            hijo = Nodo(un_hijo, nodo) 
            if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                nodos_frontera.append(hijo)
                lista_hijos.append(hijo)

        nodo.set_hijos(lista_hijos)  
    return None 


if __name__ == "__main__":
    conexiones = {
        'CDMX': {'SLP', 'MEXICALI', 'CHIHUAHUA'},
        'SAPOPAN': {'ZACATECAS', 'MEXICALI'},
        'GUADALAJARA': {'CHIAPAS'},
        'CHIAPAS': {'CHIHUAHUA'},
        'MEXICALI': {'SLP', 'SAPOPAN', 'CDMX', 'CHIHUAHUA', 'SONORA'},
        'SLP': {'CDMX', 'MEXICALI'},
        'ZACATECAS': {'SAPOPAN', 'SONORA', 'CHIHUAHUA'},
        'SONORA': {'ZACATECAS', 'MEXICALI'},
        'MICHOACAN': {'CHIHUAHUA'},
        'CHIHUAHUA': {'MICHOACAN', 'ZACATECAS', 'MEXICALI', 'CDMX', 'CHIAPAS'}
    }

    estado_inicial = 'CDMX'
    solucion = 'ZACATECAS'
    nodo_solucion = buscar_solucion_BFS(conexiones, estado_inicial, solucion)

    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo is not None:     
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()

        resultado.reverse()  
        print("Solucion encontrada:", resultado)
