class Deque:
    def __init__(self):
        self.items = []
        self.length = 0

    def addFront(self, item):
        self.items = [item] + self.items
        self.length +=1 

    def addRear(self, item):
        self.items.append(item)
        self.length +=1         
        
    def removeFront(self):
        self.length -=1         
        return self.items.pop(0)
    
    def removeRear(self):
        self.length -=1                 
        return self.items.pop(-1)
    
    def isEmpty(self):
        return self.length == 0 
    
    def size(self):
        return self.length

