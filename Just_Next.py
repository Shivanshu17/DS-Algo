
from isanez import DS
t = int(input())

while t>0:
    t-=1
    n = int(input())
    A = [int(number) for number in input().split(" ")]
    d = DS.Queue()
    p = 0
    l = len(A)
    for i in range(len(A)-1):
        if A[-(l-i)] <= A[(l-i-1)]:
            d.push(A[-(l-i)])
            del A[-(l-i)]
        elif A[-(l-i)] > A[(l-i-1)]:
            p = 1
            mini = A[(l-i-1)]
            del A[(l-i-1)]
    check = 0
    while d.isEmpty()!=True:
        f = d.pop()
        if mini <= f:
            A.append(mini)
            check = 1
            A.append(f)
        if check == 0:
            A.append(mini)
    
    if p == 0:
       print(-1)
    else:
        print(*A,"")
