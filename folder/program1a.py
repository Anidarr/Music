from  collections import deque
def bfs (graph,root):
    visited = set()
    q = deque([root])
    while q:
        vertex = q.popleft()
        print(vertex)
        visited.add(vertex)
        for i in graph[vertex]:
            if i not in visited:
                q.append(i)
    # print (visited)
graph = {0:[1,2,3] , 1:[0,1] , 2:[0,1,4,6] , 3:[0] , 4:[2] , 6:[2,5] , 5:[6]}
bfs(graph,0)
