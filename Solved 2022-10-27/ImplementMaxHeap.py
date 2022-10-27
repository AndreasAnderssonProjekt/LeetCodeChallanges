class MaxHeap():
    def __init__(self):
        self.l = []

    def getHeap(self):
        return self.l

    def getMax(self):
        return self.l[0]

    def extractMax(self):
        return self.pop(0)

    def pop(self, i):
        self.swap(i,-1)
        val = self.l.pop()
        self.heapify(i)
        return val

    def push(self,value):
        self.l.append(value)
        curr = self.size() - 1
        while curr > 0 and self.l[(curr-1)//2] < self.l[curr]:
            temp = self.l[(curr-1)//2]
            self.l[(curr-1)//2] = self.l[curr]
            self.l[curr] = temp
            curr = (curr-1)//2

    def heapify(self,i):
        largest = i
        left_child = 2*i + 1
        right_child = 2*i + 2
        n = len(self.l)

        if left_child < n and self.l[left_child] > self.l[largest]:
            largest = left_child

        if right_child < n and self.l[right_child] > self.l[largest]:
            largest = right_child

        if i != largest:
            self.swap(largest, i)
            self.heapify(largest)

    def swap(self, i, j):
        tmp = self.l[i]
        self.l[i] = self.l[j]
        self.l[j] = tmp

    def parent(self, i):
        return (i-1) // 2

    def size(self):
        return len(self.l)
