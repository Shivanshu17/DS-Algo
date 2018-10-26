from isanez import DS
t = int(input())

while t>0:
    t-=1
    A = input().split()
    
    x = DS.Stack()
    l = len(A)
    count = 0
    for i in range(l):
        if A[i] == '<':
            x.push(A[i])
        elif A[i]=='>' and x.isEmpty()!= True:
            count+=2
            x.pop()
        else:
            continue
    
    print(count)

