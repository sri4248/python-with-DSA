from collections import deque
def bfs(graph,start):
    queue=dequeue([start])
    visited=set()
    visited.add(start)
    while queue:
        vertex=queue.popleft()
        print(vertex,end=' ')
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}
print("BFS traversal starting from vertex 'A':")
bfs(graph,'B')   
