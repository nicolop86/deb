#!/usr/bin/python
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
queue.popleft()                 # The first to arrive now leaves

queue.popleft()                 # The second to arrive now leaves

print(queue)                           # Remaining queue in order of arrival

combs=[(x, y) for x in [1,2,3] for y in [10,3,1,4] if x != y]
print(combs)

