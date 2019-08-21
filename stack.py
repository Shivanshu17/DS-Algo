class stack:
    def __init__(self):
        self.stack = []
    
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    
    def push(self, item):
        self.stack.append(item)
    
    def size(self):
        return len(self.stack)
    
    def peek(self):
        if len(self.stack) == 0:
            return None
        t = self.stack.pop()
        self.stack.push(t)
        return(t)
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False
    
    