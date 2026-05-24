from collections import deque

queue = deque()
# Enqueue elements ie from rear
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)
# Dequeue elements ie from rear
queue.pop()
print(queue)


# Inject elements ie from front
queue.appendleft(0)
print(queue)

# Eject elements ie from front
queue.popleft()
print(queue)