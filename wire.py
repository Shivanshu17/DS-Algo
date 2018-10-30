from isanez import DS

t = int(input())
while t>0:
    t-=1
    A = input().split()
    x = DS.Stack()
    for i in range(len(A)):
        if x.isEmpty():
            x.push(A[i])
        elif A[i] == x.peek():
            x.pop()
            continue
        else:
            x.push(A[i])
        
    if x.isEmpty():
        print('yes')
    else:
        print('no')
        

        