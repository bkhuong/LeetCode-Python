class Stack:
    
    def __init__(self):
        self.items = []
        self.length = 0 
    
    def push(self, item):
        self.items.append(item)
        self.length +=1
    
    def pop(self):
        self.items.pop(-1)
        self.length -=1
    
    def peek(self):
        return self.items[-1]
    
    def isEmpty(self):
        return self.length == 0 
    
    def size(self):
        return self.length


