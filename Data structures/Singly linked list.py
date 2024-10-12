class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
    def __str__(self):
        return f"{self.data}"


class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_head(self, data):#This changes the head of a linked-list
        self.head = Node(data, self.head)

    
    def add_at_tail(self, data):#This changes the tail of a linked-list
        if not self.head:
            self.head = Node(data, None)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(data, None)

    
    def get_tail(self):#This returns the tail in the linked-list
        n = self.head
        while n.next != None:
            n = n.next
        return n.data 
    
    def get_head(self):
        return self.head.data
    
    def is_empty(self):#This determines if a linked-list is empty 
        return self.head == None
    
    
    def print_list(self):#This prints the content of the linked list
        n = self.head
        while n != None:
            print(n.data, end= " => ")
            n = n.next
        print()

    
    def contains(self, value): #This searches the linked-list for "value"
        n = self.head
        
        while n != None and n.data != value:
            n = n.next
        
        if n:
            return True
        return False
            
    def remove(self, value):
        if self.head.data == value:
            self.head.data = "Deleted"
            return
        
        n = self.head
        while n != None and n.data != value:
            n = n.next

        if n.data:
             n.data = "Deleted"

    def traverse(self):
        n = self.head
        while n != None:
            print(n.data)
            n = n.next

    def reverse(self):
        curr = self.head
        reverse = None
        while curr.data: 
           if  not curr.next:
                reverse = Node(curr.data, reverse)
                self.print_list()
                return
           
           reverse = Node(curr.data, reverse)
           curr = curr.next
        
        self.head = reverse
        self.print_list()


            

        
    
    
            
        

       


        
            
            

            
            

        

s = LinkedList()
s.add_at_tail(18)
s.add_at_head(5)
s.add_at_head(8)
s.add_at_head(9)
s.add_at_head(12)

print(s.contains(12))


s.reverse()



