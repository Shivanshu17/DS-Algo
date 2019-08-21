def insertionsort(arr):
    l = len(arr)
    for i in range(1,l):
        j= i-1
        key = arr[i]
        while(j>=0 and key<arr[j]):
            arr[j+1] =  arr[j]
            j = j-1
        
        arr[j+1] = key

arr = [3,5,1,6,3,8,2,9]
insertionsort(arr)
for k in arr:
    print(k)