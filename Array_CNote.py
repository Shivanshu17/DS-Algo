t = int(input('Enter the number of test cases \n'))
b = []
for i in range(t):
    temp = list((input().split(" ")))
    X = int(temp[0])
    Y = int(temp[1])
    K = int(temp[2])
    N = int(temp[3])
    r = X-Y
    a = 0
    pc = []
    for j in range(N):
        pc.append(list((input().split(" "))))
    
    for j in range(N):
        if(int(pc[j][0]) >= r and int(pc[j][1]) <=K):
            a = 1
            break
        
    if (a==0):
        b = b+['No']
        
    if (a == 1):
        b = b+['Yes']
        

for i in b:
    print(i)

    