from isanez import DS
t = int(input())
while t>0:
    t-=1
    
    A = [int(number) for number in input().split()]
    x = DS.Stack()
    l = len(A)
    count = 0
    maxarea = 0
    for i in range(l):
        marea = 0
        if x.isEmpty() or A[i]> x.peek():
            x.push(A[i])
            count = 0
        elif A[i]<= int(x.peek()):
            
            while x.isEmpty()!= True and A[i]< x.peek():
                area = (count+1)* x.pop()
                count+=1
                if marea<area:
                    marea = area
            if A[i] == x.peek():
                count+=2
                area = (count)*x.pop()
                if marea<area:
                    marea = area
        if maxarea<marea:
            maxarea = marea
    
    if x.isEmpty()!= True:
        count = 0
        marea = 0
        while x.isEmpty() != True:
            area = (count+1)* x.pop()
            count+=1
            if marea<area:
                marea = area
        maxarea = max(maxarea, marea)
    
    print(maxarea)
                
                
                
    