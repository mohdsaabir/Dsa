# Issue is the if queue is full it removes the oldest elemnt and add the new element deviation from the classical circular queue implementation
from collections import deque

queue = deque(maxlen=3)

queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

queue.append(4)
print(queue)

