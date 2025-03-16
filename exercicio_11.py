# Grafo não direcionado
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'A'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C']
}

def dfs(grafo, vertice, visitados=None, ordem=None):
    if visitados is None:
        visitados = set()
    if ordem is None:
        ordem = []

    visitados.add(vertice)
    ordem.append(vertice)

    for vizinho in grafo[vertice]:
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados, ordem)
    
    return ordem

# Exemplo de uso
ordem_visita = dfs(grafo, 'A')
print("Ordem de visitação:", ordem_visita)
# Possível saída: ['A', 'B', 'D', 'C', 'E']
