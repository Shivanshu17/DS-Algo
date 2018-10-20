

t = int(input("Enter the size of test set"))
nc = []
A = []
nf = []
for i in range(int(t)):
    nc = list(input().split(" "))
    a = list(input().split(" "))
    nc1 = []
    a1 = []
    for t in nc:
        t = int(t)
        nc1 = nc1 + [t]
    for t in a:
        t = int(t)
        a1 = a1 +[t]
        
    nf.append(nc1)
    A.append(a1)
print (nf)
print(A)

p = 0
for i in range(t):
    for j in range(len(A[i])):
        p = p + A[i][j]
    if p < nf[i][1]:
        print ('Yes')
    else:
        print('No')


    


    