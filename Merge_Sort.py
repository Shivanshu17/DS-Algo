def mergesort(arr):
    if len(arr)>1:
        m = len(arr)//2
        
        L = arr[:m]
        R = arr[m:]
        
        mergesort(L)
        mergesort(R)
        
        i = j = k = 0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                arr[k]= L[i]
                k+=1
                i+=1
            else:
                arr[k] = R[j]
                k+=1
                j+=1
            
        while i<len(L):
            arr[k] = L[i]
            k+=1
            i+=1
            
        while j<len(R):
            arr[k] = R[j]
            k+=1
            j+=1
        


arr = [3,5,1,6,3,8,2,9]
mergesort(arr)
for i in arr:
        print(i)
            