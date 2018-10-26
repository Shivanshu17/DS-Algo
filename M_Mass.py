from isanez import DS
t = int(input())

while t>0:
    t-=1
    A = input()
    C, O, H = 12, 16, 1
    A = '(' + A + ')' + '1'
    x = DS.Stack()
    l = len(A)
    tmass, mass, hmass, n, i =  0, 0, 0, 1, 0
    while i<l:
        if A[i] != ')':
            x.push(A[i])
            i+=1
            continue
        elif A[i] == ')':
            z=1
            if A[i+1].isdigit():
                i = i+1
                try:
                    z = int(A[i])
                except IndexError:
                    break
            n =1
            mass = 0
            while x.peek()!= '(':
                k = x.pop()
                if k.isdigit():
                    n = int(k)
                    continue
                elif k == 'C':
                    mass+=(n)*C
                    n = 1
                elif k == 'O':
                    mass+=(n)*O
                    n = 1
                elif k == 'H':
                    mass+=(n)*H
                    n = 1
            
            tmass += (z)*mass
            
    
    print(tmass)
            