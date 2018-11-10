import math
t = int(input())

while t>0:
    t-=1
    N = int(input())
    M = int(input())
    pm, pn = 0,0
    for i in range(2,int(M/2)):
        if M%i == 0:
            pm =1
            break
    for i in range(2, int(N/2)):
        if N%i == 0:
            pn = 1
            break
    count = 0
    if pm == 1 and pn == 1:
        while N!=M:
            N = divisee(N, M)
            count +=1
    print(count)    

def divisee(a,b):

    for i in range(2, a):
        if a%i == 0:
            t = a/i
            if a+t<=b:
                a = a+t
            
    return(a)
