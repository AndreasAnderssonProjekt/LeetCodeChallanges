class MinHeap():
    def __init__(self):
        self.l = []

    def getMin(self):
        return self.l[0]

    def extractMin(self):
        return self.pop(0)

    def pop(self, i):
        self.swap(i,-1)
        val = self.l.pop()
        for j in range((len(self.l)//2) - 1,-1,-1):
            self.heapify(j)
        return val

    def push(self,value):
        self.l.append(value)
        for j in range((len(self.l) // 2) - 1, -1, -1):
            self.heapify(j)

    def heapify(self,i):
        smallest = i
        left_child = 2*i + 1
        right_child = 2*i + 2
        n = len(self.l)

        if left_child < n and self.l[left_child] < self.l[smallest]:
            smallest = left_child

        if right_child < n and self.l[right_child] < self.l[smallest]:
            smallest = right_child

        if i != smallest:
            self.swap(smallest, i)
            self.heapify(smallest)

    def swap(self, i, j):
        tmp = self.l[i]
        self.l[i] = self.l[j]
        self.l[j] = tmp

    def parent(self, i):
        return (i-1) // 2
