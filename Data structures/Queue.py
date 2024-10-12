class Queue():
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        length = len(self.items)
        self.items.insert(length, item)

    def dequeue(self):
        self.items.pop(0)

    def print_queue(self):
        print(self.items)


African_countries = Queue()
A_c = African_countries.enqueue
print_queue = African_countries.print_queue

A_c("Nigeria")
A_c("Ghana")
A_c("Rwanda")
A_c("Egypt")
A_c("Cote d' ivoire")



print_queue()
