t = int(input())

while t>0:
    t-=1
    A = [int(number) for number in input().split()]
    A.sort()
    print(A[0]^A[1])
    