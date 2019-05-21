ss Queue2Stacks():
    def __init__(self):
        self.in_stack = []
        self.out_stack = [] 
        
    def enqueue(self,element): 
        self.in_stack.append(element)
        
    def dequeue(self): 
        if len(self.out_stack) == 0:
            for i in range(len(self.in_stack)):
                self.out_stack.append(self.in_stack.pop(-1))
            return self.out_stack.pop(-1)
        else:
            return(self.out_stack.pop(-1))
        

