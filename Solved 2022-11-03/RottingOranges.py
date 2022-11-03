def orangesRotting(self, grid):
        rotten = MyQueue()
        nrUnrotten = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    nrUnrotten += 1

                elif grid[i][j] == 2:
                    rotten.push((i,j))

        time = 0

        while not rotten.empty():
            i, j= rotten.pop()

            if grid[i][j] == 2 + time and nrUnrotten != 0: # We have reached a new time step.
                time += 1

            if i > 0:
                if grid[i-1][j] == 1:
                    grid[i-1][j] = 2 + time # Indicates at which time step the orange rotted.
                    rotten.push((i-1, j))
                    nrUnrotten -= 1


            if i < len(grid) - 1:
                if grid[i+1][j] == 1:
                    grid[i+1][j] = 2 + time
                    rotten.push((i+1, j))
                    nrUnrotten -= 1

            if j > 0:
                if grid[i][j-1] == 1:
                    grid[i][j-1] = 2 + time
                    rotten.push((i, j-1))
                    nrUnrotten -= 1

            if j < len(grid[0]) - 1:
                if grid[i][j+1] == 1:
                    grid[i][j+1] = 2 + time
                    rotten.push((i, j+1))
                    nrUnrotten -= 1

        if nrUnrotten != 0:
            return -1

        return time

#Implementation of Queue (see Solved 2022-11-02)
class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self.peek()
        return self.out_stack.pop()
        

    def peek(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) != 0:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self):
        
        return len(self.in_stack) == 0 and len(self.out_stack) == 0
