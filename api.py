from flask import Flask, request, render_template, jsonify
from arbol import Nodo

def buscar_solucion_BFS_rec(nodo_inicial, solucion, visitados):
    visitados.append(nodo_inicial.get_datos())
    if nodo_inicial.get_datos() == solucion:
        return nodo_inicial

    # Expandir nodos hijos
    dato_nodo = nodo_inicial.get_datos()
    hijos = [
        [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]],
        [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]],
        [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
    ]
    nodos_hijos = [Nodo(hijo, nodo_inicial) for hijo in hijos]
    nodo_inicial.set_hijos(nodos_hijos)

    for nodo_hijo in nodo_inicial.get_hijos():
        if nodo_hijo.get_datos() not in visitados:
            resultado = buscar_solucion_BFS_rec(nodo_hijo, solucion, visitados)
            if resultado is not None:
                return resultado
    return None

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    estado_inicial = request.form.get("estado_inicial")
    solucion = request.form.get("solucion")

    # Convertir las entradas de los nodos a listas
    try:
        estado_inicial = [int(x) for x in estado_inicial.split(",")]
        solucion = [int(x) for x in solucion.split(",")]
    except ValueError:
        return jsonify({"error": "Los nodos deben estar en formato de lista de enteros separados por comas."}), 400

    if not estado_inicial or not solucion:
        return jsonify({"error": "Debe enviar el nodo inicial y la solución"}), 400
    
    nodo_inicial = Nodo(estado_inicial)
    visitados = []
    nodo_solucion = buscar_solucion_BFS_rec(nodo_inicial, solucion, visitados)

    if nodo_solucion:
        resultado = []
        nodo = nodo_solucion
        while nodo is not None:
            resultado.append(nodo.get_datos())
            nodo = nodo.get_padre()
        resultado.reverse()
        return jsonify({"resultado": resultado})
    else:
        return jsonify({"mensaje": "No se encontró solución"}), 404

if __name__ == '__main__':
    app.run(debug=True)