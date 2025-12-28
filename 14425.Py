N,M = map(int,input().split())

dict = {}

for i in range(N):
    dict[input()] = 1

answer = 0

for _ in range(M):
    if input() in dict:
        answer +=1

print(answer)
