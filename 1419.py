from math import *
l = int(input())
r = int(input())
k = int(input())

#나올 수 있는 값은 k*(2*x + (k-1)*d)//2

if k == 2:
    print(max(0, r - max(l, 3) + 1))
elif k == 3:
    l = ceil(l/3)
    r = floor(r/3)
    print(max(0, r - max(l, 2) + 1))
elif k == 4:
    l = ceil(l / 2)
    r = floor(r / 2)
    tmp = r - l + 1
    if l <= 1 <= r:
        tmp -= 1
    if l <= 2 <= r:
        tmp -= 1
    if l <= 3 <= r:
        tmp -= 1
    if l <= 4 <= r:
        tmp -= 1
    if l <= 6 <= r:
        tmp -= 1
    print(max(0, tmp))
else:
    l = ceil(l / 5)
    r = floor(r / 5)
    print(max(0, r - max(l, 3) + 1))