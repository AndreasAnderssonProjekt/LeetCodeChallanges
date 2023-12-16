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
