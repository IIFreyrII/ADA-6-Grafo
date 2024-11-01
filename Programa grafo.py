import networkx as nx
import matplotlib.pyplot as plt

grafo = {
    'Aguascalientes': [('Zacatecas', 100), ('San Luis Potosí', 150)],
    'Zacatecas': [('Aguascalientes', 100), ('San Luis Potosí', 200), ('Durango', 250)],
    'San Luis Potosí': [('Aguascalientes', 150), ('Zacatecas', 200), ('Querétaro', 300)],
    'Durango': [('Zacatecas', 250), ('Chihuahua', 350)],
    'Chihuahua': [('Durango', 350), ('Coahuila', 400)],
    'Coahuila': [('Chihuahua', 400), ('Nuevo León', 450)],
    'Nuevo León': [('Coahuila', 450), ('San Luis Potosí', 500)]
}

# Función para recorrer todos los estados sin repetir ninguno
def recorrer_sin_repetir(grafo, inicio):
    visitados = set()
    recorrido = []
    costo_total = 0

    def dfs(estado):
        nonlocal costo_total
        visitados.add(estado)
        recorrido.append(estado)
        if estado not in grafo or not grafo[estado]:  # Si no tiene conexiones, omitirlo
            return
        for vecino, costo in grafo[estado]:
            if vecino not in visitados:
                costo_total += costo
                dfs(vecino)

    dfs(inicio)
    return recorrido, costo_total

# Función para recorrer los estados repitiendo al menos uno
def recorrer_con_repetir(grafo, inicio):
    recorrido = []
    costo_total = 0
    visitados = set()

    def dfs(estado):
        nonlocal costo_total
        recorrido.append(estado)
        visitados.add(estado)
        if estado not in grafo or not grafo[estado]:  # Si no tiene conexiones, omitirlo
            return
        
        for vecino, costo in grafo[estado]:
            if vecino not in visitados:
                costo_total += costo
                dfs(vecino)
                visitados.remove(vecino)  # Permite reexplorar el vecino en otro contexto

            if len(recorrido) > len(grafo):
                return

    dfs(inicio)
    return recorrido, costo_total

# Función para dibujar el grafo
def dibujar_grafo(grafo):
    G = nx.Graph()
    for estado, conexiones in grafo.items():
        for vecino, costo in conexiones:
            G.add_edge(estado, vecino, weight=costo)
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=10, font_weight='bold')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Mostrar los estados y sus relaciones
def mostrar_relaciones(grafo):
    for estado, conexiones in grafo.items():
        print(f"{estado}:")
        for vecino, costo in conexiones:
            print(f"  -> {vecino} (Costo: {costo})")

# Ejecución del programa
inicio = 'Aguascalientes'
recorrido_sin_repetir, costo_sin_repetir = recorrer_sin_repetir(grafo, inicio)
recorrido_con_repetir, costo_con_repetir = recorrer_con_repetir(grafo, inicio)

print("Recorrido sin repetir:", recorrido_sin_repetir)
print("Costo total sin repetir:", costo_sin_repetir)
print("Recorrido con repetir:", recorrido_con_repetir)
print("Costo total con repetir:", costo_con_repetir)

dibujar_grafo(grafo)
mostrar_relaciones(grafo)