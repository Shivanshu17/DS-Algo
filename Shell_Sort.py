def shellsort(a):
    l = len(a)
    d = 1
    t = []
    while(d<l):
        t = t + [d]
        d = 3*d+1
    for k in range(0, len(t)):
        for i in range(t[k],l):
            x = k
            j = i
            key = a[i]
            while(j>=t[k] and key<a[j-t[k]]):
                a[j] = a[j-t[k]]
                j = j-t[x]
            
            a[j] = key

a = [3,5,1,6,3,8,2,9]
shellsort(a)
for k in a:
    print(k)