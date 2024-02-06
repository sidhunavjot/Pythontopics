#implementation using queue

from queue import LifoQueue

stack = LifoQueue(maxsize=6)
stack.put(2)
stack.put(4)
stack.put(7)
stack.put(3)
stack.put(8)
stack.put(10)

print(stack.qsize())
print(stack.full())
stack.get()
print(stack.full())
