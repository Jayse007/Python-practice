

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None #-> link to next node
        self.prev = None  #-> link to previous node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node= node.next

    
    
    
    # This adds a node changes the tail and points to the previous tail and None 
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        
        if not self.head:
            self.head = node
            self.tail = node
            return
        
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.tail.next = None
        
    
    
    #This removes the value parameter from the DoublyLinkedList
    def remove(self, value):
        if self.head == None:
            return False
        
        if self.head.value == value:
            if self.head.value == self.tail.value:
                self.head = None
                self.tail = None
                return
            
            self.head = self.head.next
            self.head.prev = None
        
        node = self.head

        while node  and node.value != value:
            node = node.next

        if node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
            return 
        
        elif node:
            node.prev.next = node.next
            node.next.prev = node.prev
            return True
        

        
        

        
           





doublyLL = DoublyLinkedList()
doublyLL.createDLL(4)
doublyLL.createDLL(10)
doublyLL.createDLL(15)
doublyLL.createDLL(32)
doublyLL.createDLL(15)



print([node.value for node in doublyLL])


#If you have any questions, please feel free to contact me on github or at shawonjames002@gmail.com