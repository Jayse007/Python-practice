class Heap:
    def __init__(self):
        self.heap = []
        self.count = len(self.heap)

    def __str__(self):
        return f"{self.heap}"


    def add(self, value):
        self.heap.append(value)
        self.count += 1
        self.MinHeapify()

    def MinHeapify(self):
        i =  self.count - 1
        while i > 0 and self.heap[i] < self.heap[(i-1)// 2]:
            self.heap[i], self.heap[(i-1) // 2] = self.heap[(i-1) // 2], self.heap[i]
            i = (i-1)//2

    def delete(self, value):
        index = self.heap.index(value)
        left = (2 * index) + 1
        right = (2 * index) + 2
        if index < 0:
            return False
        
        count = len(self.heap)
        count = count - 1

        self.heap[index] = self.heap[count]

        while left < count and self.heap[index] > self.heap[left] or self.heap[index] > self.heap[right]:
            if self.heap[left] < self.heap[right]:
                self.heap[index] = self.heap[left]

            else:
                self.heap[index] = self.heap[right]
            



heap = Heap()
heap.add(3)
heap.add(7)
heap.add(18)
heap.add(12)
heap.add(25)
heap.add(11)
heap.delete(25)