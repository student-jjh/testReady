N, C = map(int,input().split())

lst =list(map(int,input().split()))

S = N // 2

lst_1 = lst[:S]
lst_2 = lst[S:]

Set_1 = set()
Set_2 = set()

def get_sub_sums(arr):
    sums = []
    n = len(arr)
    for mask in range(1 << n):
        total = 0
        for i in range(n):
            if mask & (1 << i):
                total += arr[i]
        sums.append(total)
    return sums
    
lst_1 = get_sub_sums(lst_1)
lst_2 = sorted(get_sub_sums(lst_2))

def upper_bound(arr, target):
    left = 0
    right = len(arr)  # 주의: len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left  # target 이하 원소 개수

answer = 0
for item in lst_1:
    temp = C - item

    answer += upper_bound(lst_2,temp)

print(answer)

