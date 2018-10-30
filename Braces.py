from isanez import DS
t = int(input())
while t>0:
    t-=1
    x = DS.Stack()
    A = input().split()
    moves, count = 0, 0
    for i in range(len(A)):
        if A[i] == '}' and x.isEmpty():
            moves = moves + 1
        elif A[i]== '{':
            x.push(A[i])
        else:
            x.pop()
            moves = moves + 1
    
    while x.isEmpty()!= True:
        count = count+1
        x.pop()
    
    if count % 2 == 0:
        moves = moves + count/2
    else:
        moves = moves + int(count/2) +1
    
print(moves)