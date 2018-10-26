
t = int(input())

while t>0:
    t-=1
    tmass = 0
    C, O, H = 12, 16, 1
    A = input()
    i = 0
    
    while True:
        n = 1
        if A[i].isdigit():
            n = int(A[i])
        
        if A[i] == 'C':
            tmass += C
            mass= C
        elif A[i] == 'O':
            tmass += O
            mass = O
        elif A[i] == 'H':
            tmass += H
            mass = H
        elif A[i] == '(':
            mass = 0
            while A[i]!= ')':
                i+=1
                n = 1
                if A[i].isdigit():
                    n = int(A[i])
                    
                if A[i] == 'C':
                    tmass += C
                    z = C
                elif A[i] == 'O':
                    tmass += O
                    z = O
                elif A[i] == 'H':
                    tmass += H
                    z = H
            tmass += mass
            n = 1
        tmass = tmass + (n-1)*mass
        i += 1
        if i== len(A):
            break
    
    print(tmass)
