# Bairros: A = Centro, B, C, D, E, F = Bairro Industrial
cidade = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['B', 'C', 'F'],
    'F': ['D', 'E']
}

from collections import deque

def bfs_caminho_curto(grafo, inicio, alvo):
    visitados = set()
    fila = deque([inicio])
    visitados.add(inicio)
    
    # Dicionário para guardar de onde cada vértice foi alcançado
    pai = {inicio: None}

    while fila:
        atual = fila.popleft()
        
        if atual == alvo:
            # Reconstruir caminho a partir do alvo
            caminho = []
            while atual is not None:
                caminho.append(atual)
                atual = pai[atual]
            caminho.reverse()
            return caminho  # Retorna o caminho do início até o alvo
        
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                pai[vizinho] = atual
                fila.append(vizinho)
    
    return None  # Se não houver rota

# Exemplo de uso:
caminho_minimo = bfs_caminho_curto(cidade, 'A', 'F')
print("Menor caminho de A até F:", caminho_minimo)
