from collections import deque

K = int(input())

def bfs(start):
    q = deque()
    q.append(start)
    color[start] = 1

    while q:
        now = q.popleft()
        color_now = color[now]
        for next in graph[now]:
            next_color = color[next]
            if next_color == color_now:
                return False
            elif next_color == 0:
                if color_now == 1:
                    next_color = 2
                else:
                    next_color = 1
                color[next] = next_color
                q.append(next)
    return True
    

for i in range(K):
    V,E = map(int,input().split())

    graph = [[] for _ in range(V + 1)]
    color = [0 for _ in range(V+1)]

    for j in range(E):
        s,e = map(int,input().split())
        graph[s].append(e)
        graph[e].append(s)
    result = True
    for i in range(1, V + 1):
        if(color[i] == 0):
            result = bfs(i)
        if result == False:
            break
            
    if result:
        print("YES")
    else:
        print("NO")
    