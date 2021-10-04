class Queue:
    def __init__(self):
        self.queue = []
    
    def push(self, elm):
        self.queue.append(elm)
    
    def pop(self):
        val = self.queue[0]
        del self.queue[0]
        return val

if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    print(q.pop())
    print(q.queue)
