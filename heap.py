class heap:
    def __init__(self):
        self.arr = ['\0']
        
    def greater(self, x, y):
        if x<=y:
            return(self.arr.index(y))
        else:
            return(self.arr.index(x))
    
    def less(self, x, y, z):
        if(x<y or x<z):
            return True
        return False
        
    def swim(self, k):
        j = self.arr.index(k)
        while(j>2 and self.arr[j]>self.arr[j//2]):
            self.arr[j], self.arr[j//2] = self.arr[j//2], self.arr[j]
            j = j//2
        
    def sink(self, k):
        j = self.arr.index(k)
        n = len(self.arr)
        while(j<n//2 and self.less(self.arr[j],self.arr[2*j],self.arr[2*j+1])):
            t = self.greater(self.arr[2*j], self.arr[2*j+1])
            self.arr[j], self.arr[t] = self.arr[t], self.arr[j]
            j = t
    def isEmpty(self):
        if len(self.arr == 1):
            return True
        return False
    
    def insert(self, k):
        self.arr.append(k)
        self.swim(k)
    
    def delMax(self):
        self.arr[1], self.arr[-1] = self.arr[-1], self.arr[1]
        return_value = self.arr.pop(-1)
        self.sink(self.arr[1])
    
    
        