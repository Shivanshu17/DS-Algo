t = int(input())


while t>0:
    t-=1
    n, m = map(int(input().split()))
    N = {}
    for i in range(n):
        p, i = map(int(input().split()))
        if i in N:
            N[i] += p
        else:
            N[i] = p
    for i in range(m):
        p, i = map(int(input().split()))
        N[i] -= p
    ans = 0
    for k in N:
        if N[k]<0:
            ans-=N[k]
            
    print (ans)
    
