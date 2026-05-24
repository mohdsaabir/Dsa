# Default priority queue in python is a min heap
# To implement a max heap we can negate the priority value while pushing and popping
# This is heap based priority queue implementation and not the classical array of structure based implementation
# Time complexity of push and pop is O(log n) where n is the number of elements in the priority queue
import heapq

pq = []

heapq.heappush(pq, (3, 'task1'))
heapq.heappush(pq, (1, 'task2'))
heapq.heappush(pq, (2, 'task3'))

print(pq)

heapq.heappop(pq)
print(pq)

heapq.heappop(pq)
print(pq)
