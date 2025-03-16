from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []

    while queue:
        current = queue.popleft()
        order.append(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order

# Exemplo com o grafo da questão 7:
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E']
}

resultado = bfs(grafo, 'A')
print("Ordem de visita da BFS:", resultado)
# Saída típica: ['A', 'B', 'C', 'D', 'E', 'F']

"""
Diferença fundamental: 
- A BFS utiliza uma fila (queue) para armazenar os nós temporários,
  enquanto a DFS costuma usar uma pilha (ou recursão com pilha implícita).
"""
