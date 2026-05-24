graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C' : [],
    'D' : [],
    'E' : []
}

visited = set()
stack = ['A']


while stack:

    node = stack.pop()

    if node not in visited:
        print(node, end=' ')
        visited.add(node)

        for neighbor in reversed(graph[node]):
            stack.append(neighbor)

