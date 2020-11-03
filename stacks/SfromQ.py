from queue import Queue

class Stack:
    def __init__(self):
        self.isEmpty = True
        self.q = Queue()

    def push(self,ele):
        self.q.put(ele)
        #self.size +=1
        for _ in  range(self.q.qsize()-1):
            data = self.q.get()
            #print(data)
            self.q.put(data)

    def pop(self):
        return self.q.get()
    
    def peek(self):
        return self.q[0]



s = Stack()
s.push(3)
s.push(2)
s.push(1)

# print(s.pop())
# print(s.pop())
print(s.peek())

