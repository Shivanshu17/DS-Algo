from stack import *
s = stack()

a = list(input().split())

def isOperand(self, ch):
    return ch.isalpha()

def notGreater(self, op):
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    a = precedence[op]
    b = s.peek()
    return True if a>=b else False

for i in a:
    if self.isOperand(i):
        print(i, end= '')
    
    elif i=='(':
        s.push(i)
        
    elif i == ')':
        while( not s.isEmpty() and s.peek!='('):
            print(s.pop(), end ='')
        if (s.isEmpty()):
            print('Braces unmatched')
        else:
            s.pop()
    
    else:
        while(not s.isEmpty() and self.notGreater(i)):
            print(s.pop(), end = '')
        
        s.push(i)

while(not s.isEmpty()):
    print(s.pop(), end ='')


    