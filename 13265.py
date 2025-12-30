from collections import deque


def bfs(s):
    q = deque()
    q.append(s)
    visited[s] = 1

    while q:
        now = q.popleft()
        
        for end in graph[now]:
            if visited[end] == 0:
                visited[end] = -1 * visited[now]
                q.append(end)
            
            elif visited[end] == visited[now]:
                return False
    
    return True




T = int(input())

for i in range(T):
    N,M = map(int,input().split())

    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        s,e = map(int,input().split())

        graph[s].append(e)
        graph[e].append(s)

    visited = [0 for _ in range(N + 1)]

    b = True

    for i in range(1,N+1):
        if visited[i] == False:
            b = bfs(i)
        
        if b == False:
            break
    

    if b:
        print("possible")
    else:
        print("impossible")

