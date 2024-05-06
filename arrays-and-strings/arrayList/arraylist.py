class ArrayList:
    def __init__(self, size=10): 
        self.size = size
        self.count = 0
        self.items = []
    
    def IsEmpty(self):
        return self.count == 0
    
    def IsFull(self):
        return self.count == self.size
    
    def Add(self, item):
        
        if self.IsFull():
            raise Exception("List is full")
        
        self.items.append(item)
        self.count += 1

    def AddAt(self, index, item):
        
        if index < 0 or index >= self.size:
            raise Exception("Index out of range")
        
        self.items.insert(index, item)
        self.count += 1

    def Remove(self):
        self.RemoveAt(self.count - 1)

    def RemoveAt(self, index):
        
        if index < 0 or index >= self.size:
            raise Exception("Index out of Range")

        del self.items[index]
        self.count -= 1

    def Set(self, index, item):
        
        if index < 0 or index >= self.size:
            raise Exception("Index out of Range")
        
        if index >= self.count:
            self.count = index + 1

        self.items.insert(index, item)

    def Size(self):
        return self.count

    def Clear(self):
        self.items = []
        self.count = 0

    def ToString(self):
        return str(self.items)
    
    def Get(self, index):
        
        if index < 0 or index >= self.size:
            raise Exception("Index out of Range")
        
        return self.items[index]
        
