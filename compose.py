import math
t = int(input())

while t>0:
    t-=1
    N = int(input())
    M = int(input())
    pm, pn = 0,0
    for i in range(2,M):
        if M%i == 0:
            pm =1
            break
    for i in range(2, N):
        if N%i == 0:
            pn = 1
            break
    count = 0
    if pm == 1 and pn == 1:
        while N!=M:
            for i in range(2, N):
                if N%i == 0:
                    t = N/i
                    if N+t<=M:
                        N = N+t
            
            count +=1
    print(count)    



    

