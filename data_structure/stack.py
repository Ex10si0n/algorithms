class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, elm):
        self.stack.append(elm)
    
    def pop(self):
        val = self.stack.pop()
        return val

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop())
    print(s.stack)
