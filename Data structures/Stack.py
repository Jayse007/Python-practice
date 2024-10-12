class Stack:
    def __init__(self):
        self.item = []

    def push(self, item):
        self.item.insert(0, item)

    def pop(self):
        self.item.pop(0)

    def is_empty(self):
        print(self.item == [])
    
    def show(self):
        print(self.item)


thirty = Stack()
thirty.push(23)
thirty.push(39)
thirty.push(40)
thirty.pop()
thirty.show()
thirty.is_empty()