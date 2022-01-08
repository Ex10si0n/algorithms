# Linear Structure

## Queue

A Queue is a linear structure that follows a particular order in which the operations are performed. The order is First In First Out (FIFO). A good example of a queue is any queue of consumers for a resource where the consumer that came first is served first.

![Types of Queue in Data structure | Queue Data structure Introduction and  Operations](https://i1.faceprep.in/Companies-1/queue-operations.gif)

**Code to implement** [\[src code\]](../codes/data-structure/queue.py)

```python
class Queue:
    def __init__(self):
        self.queue = []
    
    def push(self, elm):
        self.queue.append(elm)
    
    def pop(self):
        val = self.queue[0]
        del self.queue[0]
        return val
```

## Stack

Stack is a linear data structure that follows a particular order in which the operations are performed. The order may be LIFO(Last In First Out) or FILO(First In Last Out).

![Stack Data Structure and Implementation in Python, Java and C/C++](https://cdn.programiz.com/sites/tutorial2program/files/stack.png)

\*\*Code to implement \*\*[\[src code\]](../codes/data-structure/stack.py)

```python
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, elm):
        self.stack.append(elm)
    
    def pop(self):
        val = self.stack.pop()
        return val
```
