# 1. Lista de Adjacência em Python
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E']
}

# Exemplo de consulta de vizinhos
for cidade, vizinhos in grafo.items():
    print(f"{cidade} => {vizinhos}")
