# Time complexity O(V+E)
from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C' : [],
    'D' : [],
    'E' : []
}

visited = set()

queue = deque(['A'])
visited.add('A')

while queue:

    node = queue.popleft()
    print(node , end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

