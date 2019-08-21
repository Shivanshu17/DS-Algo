from heap import *

    
h = heap()
def heapify():
    n = len(h.arr)
    n = n//2
    while(n>1):
        h.sink(h.arr[n])
        n = n-1
        
def printMax():
    n = len(h.arr)
    while(n>1):
        h.arr[1], h.arr[n-1] = h.arr[n-1], h.arr[1]
        h.sink(h.arr[1])
        n = n-1
        
    print(h.arr)
t = list(input().split(' '))
for i in t:
    h.insert(i)
    
heapify()
printMax()
    