def detect_cycle_dfs(graph):
    visited = set()
    recStack = set()

    def dfs(u):
        visited.add(u)
        recStack.add(u)
        for v in graph[u]:
            if v not in visited:
                if dfs(v):
                    return True
            elif v in recStack:
                # Encontramos um vértice que já estava na pilha de recursão
                return True
        recStack.remove(u)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

# Exemplo de uso
transactions = {
    'A': ['B'],
    'B': ['C'],
    'C': ['D'],
    'D': ['A']  # A -> B -> C -> D -> A forma um ciclo
}
existe_ciclo = detect_cycle_dfs(transactions)
print("Há ciclo suspeito?" , existe_ciclo)  # True
