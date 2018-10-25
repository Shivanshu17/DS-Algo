from isanez import DS

t = int(input())

while t>0:
    t-=1
    
    n = int(input())
    A = [int(number) for number in input().split(" ")]
    x = DS.Stack()
    y = DS.Stack()
    p = 0
    count = 1
    i =0
    while i<n:
        if A[i] == count:
            count+=1
            y.push(A[i])
            i = i+1
            continue
        while x.peek() == count and x.isEmpty() != True:
            count+=1
            y.push(x.pop())
        
        if x.isEmpty() == True:
            x.push(A[i])
            i+=1
            continue
        elif A[i] < x.peek():
            x.push(A[i])
            i+=1
        else:
            p = 1
            break
    
    if p == 0:
        print("yes")
    else:
        print("no")


    