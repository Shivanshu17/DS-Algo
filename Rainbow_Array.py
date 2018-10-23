t = int(input())

while t>0:
    t-=1
    
    N = int(input())
    
    if N<13:
        print("no")
        continue
    
    A = [int(number) for number in input().split(" ")]
    count = 1
    state = 0
 


    l = int(len(A)/2) +1
    for i in range(l):
        if A[i]== count and A[i]==A[-(i+1)]:
            continue
        
        elif A[i]== (count+1) and A[i]==A[-(i+1)]:
            count+=1
            continue
        
        else:
            state =1 
            break
        
    if state ==1:
        print("no")
    
    else:
        print("yes")
            