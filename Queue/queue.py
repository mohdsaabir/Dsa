# Deque is used as list.pop(0) is O(n) while deque.popleft() is O(1)
from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3) 

print(queue)

queue.popleft()

print(queue)