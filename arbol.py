class Nodo:
    def __init__(self, datos, padre=None):  
        self.datos = datos
        self.hijos = []  
        self.padre = padre  
        self.costo = None  

    def get_datos(self):  
        return self.datos

    def get_padre(self):  
        return self.padre

    def set_costo(self, costo):
        self.costo = costo

    def set_hijos(self, hijos):  # 🔹 Nuevo método para asignar hijos al nodo
        self.hijos = hijos  

    def get_hijos(self):  # 🔹 Método para obtener los hijos del nodo
        return self.hijos  

    def igual(self, nodo):
        return self.get_datos() == nodo.get_datos()

    def en_lista(self, lista_nodos):
        return any(self.igual(n) for n in lista_nodos)

    def __str__(self):
        return str(self.get_datos())