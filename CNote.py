t = int(input('Enter the number of test cases'))
X1 = []
Y1 = []



for i in range(t):
    X = list(input().split(" "))
    for k in range(len(X)):
        X[k] = int(X[k])
    
    for j in range(X[3]):
        N = list(input().split(" "))
        for k in range(len(N)):
            N[k] = int(N[k])
        
        Y1.append(N)
    X1.append(X)

print(X1)
print(Y1)


for i in range(t):
    l = 0
    for j in range(X1[i][3]):
        if X1[i][1] <= Y1[i*j+j][0] and X1[i][2] >= Y1[i*j+j][1]:
            l = 1
      
    if l==1:
        print("LuckyChef")
    else:
        print("UnluckyChef")
    

