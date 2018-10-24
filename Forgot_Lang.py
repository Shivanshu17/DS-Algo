t = int(input())

while t>0:
    t-=1
    
    N, K = input().split(" ")
    N = int(N)
    K = int(K)
    Dict = [input().split(" ")]
    
    Check = [0]*N
    
    for i in range(K):
        C = input().split(" ")
        L = int(C[0])
        del C[0]
        
        for k in C:
            for z in Dict:
                if k == z:
                    Check[Dict.index(z)] = 1
        
        
    for p in len(Check):
        if Check[p] == 0:
            Check[p] = "NO"
        else:
            Check[p] = "YES"
    print(*Check)
    
