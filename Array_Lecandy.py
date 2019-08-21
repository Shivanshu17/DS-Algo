
t = int(input('Enter the number of test cases'))
o = []
for i in range(t):
    nc = list(input().split(" "))
    a = list(input().split(" "))
    
    s = 0
    
    for l in a:
        l= int(l)
        s = s+l
    
    if s<int(nc[1]):
        o = o + ['Yes']
    else:
        o = o + ['No']
        

for a in o:
   print(a)


        
