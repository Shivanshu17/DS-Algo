t = int(input("Enter the number of test cases  "))
n = []
e = []

for i in range(t):
    n = n+[(input())]
    for j in range(len(n)):
        n[j] = int(n[j])
    k = list(input().split(" "))
    for j in range(len(k)):
        k[j] = int(k[j])
    e = e+[k]



for i in range(t):
    w = e[i]
    w.sort()
    s = 0
    for j in range(len(w)):
        s = s + (w[j] - w[0])
    print(s)
s



