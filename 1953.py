from collections import deque

N = int(input())

graph = [[]]
for i in range(N):
    temp = list(map(int,input().split()))
    graph.append(temp[1:])

visited = [0 for _ in range(N + 1)]
def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        now = q.popleft()

        for next in graph[now]:
            if visited[next] == 0:
                visited[next] = visited[now] * -1
                q.append(next)



for i in range(1,N+1):
    if visited[i] == 0:
        bfs(i)

Cnt1 = 0
Cnt2 = 0

for i in range(1,N+1):
    if visited[i] == 1:
        Cnt1 +=1
    elif visited[i] == -1:
        Cnt2 +=1
print(Cnt1)
for i in range(1,N+1):
    if visited[i] == 1:
        print(i,end = " ")
print()
print(Cnt2)
for i in range(1,N+1):
    if visited[i] == -1:
        print(i,end = " ")