S = input()

answer = set()

for i in range(0,len(S),1):
    for j in range(1,len(S)-i+1,1):
        answer.add(S[i:i+j])

print(len(answer))