#Note that this implementation utilizes my implementation of MaxHeap in the previous exercise.
import math
def kClosest(points, k):
    h = MaxHeap()
    for p in points:
        x, y = p[0], p[1]
        distance = math.sqrt(x**2 + y**2)
        if h.size() < k:
            h.push((distance,x,y)) # Tuples are compared position by position.
        else:
            h.push((distance,x,y))
            h.extractMax()
    return [(x,y) for (distance,x,y) in h.getHeap()]
