class Stack():
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self,n=None):
        if n==None:
             return self.items.pop()
        else:
             return self.items.pop(n)
    def peek(self,n=None):
        if n==None:
             return self.items[len(self.items)-1]
        else:
             return self.items[n]
    def size(self):
        return len(self.items)
