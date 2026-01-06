import sys
from collections import deque
m, n, o, p, q, r, s, t, u, v, w = map(int, sys.stdin.readline().split())
tomato = [[[[[[[[[[list(map(int, sys.stdin.readline().split())) for _ in range(n)]for _ in range(o)]for _ in range(p)]for _ in range(q)]for _ in range(r)]for _ in range(s)]for _ in range(t)]for _ in range(u)]for _ in range(v)]for _ in range(w)]

# 요구 조건 퍼지는 범위
room1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1]
room2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0]
room3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0]
room4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0]
room5 = [0,0,0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0]
room6 = [0,0,0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0]
room7 = [0,0,0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0]
room8 = [0,0,0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
room9 = [0,0,0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
room10 = [0,0,-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
room11 = [-1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# 토마토 존재하는 값 구성
queue = deque()
for a in range(w):
    for b in range(v):
        for c in range(u):
            for d in range(t):
                for e in range(s):
                    for f in range(r):
                        for g in range(q):
                            for h in range(p):
                                for i in range(o):
                                    for j in range(n):
                                        for k in range(m):
                                            if tomato[a][b][c][d][e][f][g][h][i][j][k] == 1:
                                                queue.append([a, b, c, d, e, f, g, h, i, j, k, 0])
# BFS 탐색                                              
while queue:
    n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, result = queue.popleft()
    for i in range(22):
        m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11 = n1+room1[i], n2+room2[i], n3+room3[i], n4+room4[i], n5+room5[i], n6+room6[i], n7+room7[i], n8+room8[i], n9+room9[i], n10+room10[i], n11+room11[i]
        if 0 <= m1 < w and 0 <= m2 < v and 0 <= m3 < u and 0 <= m4 < t and 0 <= m5 < s and 0 <= m6 < r and 0 <= m7 < q and 0 <= m8 < p and 0 <= m9 < o and 0 <= m10 < n and 0 <= m11 < m:
            if tomato[m1][m2][m3][m4][m5][m6][m7][m8][m9][m10][m11] == 0:
                tomato[m1][m2][m3][m4][m5][m6][m7][m8][m9][m10][m11] = 1
                queue.append([m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, result+1])

# 익지 않은 곳이 존재하는지 체크
for a in range(w):
    for b in range(v):
        for c in range(u):
            for d in range(t):
                for e in range(s):
                    for f in range(r):
                        for g in range(q):
                            for h in range(p):
                                for i in range(o):
                                    for j in range(n):
                                        for k in range(m):
                                            if tomato[a][b][c][d][e][f][g][h][i][j][k] == 0:
                                                result = -1
print(result)
