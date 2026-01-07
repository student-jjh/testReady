N = int(input())

answer = 0
dic = dict()

for i in range(N):
    temp = input()

    if temp == "ENTER":
        answer += len(dic)
        dic = dict()
    
    else:
        dic[temp] = 1
answer += len(dic)

print(answer)
        