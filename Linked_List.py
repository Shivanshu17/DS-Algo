class node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAfter(self, prev_node, new_data):
        if (prev_node is None):
            print('Previous Node must be a part of the linked list')
            return
        new_node = node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        
    def append(self, new_data):
        new_node = node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = new_node
    
    def deleteNode(self, key):
        if self.head is None:
            print('The list is already empty')
            return
        temp = self.head
        if(temp.data == key):
            self.head = temp.next
            temp = None
            return
        temp1 = self.head
        while (temp.next):
            temp =  temp.next
            if(temp.data == key):
                temp1.next = temp.next
                temp = None
                return
            temp1 = temp1.next
        print('Key is not in the list')
        
    def getCountRec(self, node):
        if(not node):
            return 0
        else:
            return 1+self.getCountRec(node.next)
    
    def getCount(self):
        return(self.getCountRec(self.head))
        
    def printList(self):
        if self.head is None:
            print('The list is empty')
            return
        temp = self.head
        while(temp.next):
            print(temp.data)
            temp = temp.next
        
if __name__ == '__main__':
    llist = LinkedList()
    llist.append(6)
    
    llist.push(5)
    llist.insertAfter(llist.head.next, 8)
    llist.append(11)
    llist.deleteNode(6)
    llist.push(17)
    llist.push(32)
    print(llist.getCount())
    llist.printList()

        
        
        