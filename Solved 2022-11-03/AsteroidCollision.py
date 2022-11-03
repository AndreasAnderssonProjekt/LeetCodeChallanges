def asteroidCollision(asteroids):
    remaining_asteroids = Stack()

    for asteroid in asteroids:
        add_last_asteroid = False
        if remaining_asteroids.empty():
            remaining_asteroids.push(asteroid)
        else:

            while not remaining_asteroids.empty():

                other_asteroid = remaining_asteroids.peek()
                
                #Asteroids do not collide.
                if asteroid >= 0 or other_asteroid <= 0 or other_asteroid * asteroid >= 0:
                    remaining_asteroids.push(asteroid)
                    add_last_asteroid = False
                    break
                
                #Collision where the new asteroid is larger.
                if abs(other_asteroid) < abs(asteroid):
                    remaining_asteroids.pop()
                    add_last_asteroid = True
                    continue
                
                #Collision where the asteroids are the same size.
                elif abs(other_asteroid) == abs(asteroid):
                    remaining_asteroids.pop()
                    add_last_asteroid = False
                    break
               #Collision where the new asteroid is smaller.
                else:
                    add_last_asteroid = False
                    break

            if add_last_asteroid:
                remaining_asteroids.push(asteroid)
    return remaining_asteroids.getStack()


# Implementation of stack
class Stack():
    def __init__(self):
        self.s = []

    def peek(self):
        if not self.empty():
            return self.s[-1]

    def pop(self):
        return self.s.pop()

    def push(self, value):
        self.s.append(value)

    def empty(self):
        return len(self.s) == 0

    def getStack(self):
        return self.s
