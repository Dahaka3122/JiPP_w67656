from collections import deque

def bfs_Task(graph, start, end):
    queue = deque([[start]]) # kolekcja do przechowywania ścieżek
    visited = set() # wierzchołki odwiedzone

    while queue:
        path = queue.popleft()
        node = path[-1] # ostatni wierzchołek w ścieżce
        # jeżeli wierzchołek jest celem, zwróć ścieżkę
        if node == end: return path

        if node not in visited:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)

    return None # jeżeli nie znaleziono ścieżki

graph = {
    'A': ['B', 'C'],
}