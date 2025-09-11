from collections import deque
def bfs(graph, start):
    queue=deque([start])
    while queue:
        node=queue.popleft()
        print(node, end='')
        queue.extend(graph[node])
# Example
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')