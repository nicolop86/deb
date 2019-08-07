#!/usr/bin/python
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
print(queue)
queue.append("Graham")
print(queue)
queue.popleft()
print(queue)
queue.popleft()
print(queue)

