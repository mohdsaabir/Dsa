# Time complexity O(V+E) where V is no of vetices and E is the no of edges

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': []
}

visited = set()

def dfs(node):
    # IF is needed in case of grpahs with cycle not needed in case of trees
    if node in visited:
        return
    
    print(node, end=" ")

    visited.add(node)

    for neighbor in graph[node]:
        dfs(neighbor)


dfs('A')