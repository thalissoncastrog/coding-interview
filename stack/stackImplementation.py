from typing import Optional

class Node:
    
    def __init__(self, data, next: Optional['Node'] = None):
        self.data = data
        self.next = next
    
class Stack:
    
    def __init__(self, top: Optional['Node'] = None):
        self.top = top

    def IsEmpty(self):
        
        if self.top is None:
            return True
    
        return False
    
    
    def Push(self, data):
        newNode = Node(data)

        if self.top is None:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        
    def Peek(self):

        if self.top is None:
            print("Stack Empty")
            return

        return self.top.data
    
    def Pop(self):
        
        if self.top is None:
            print("It is not possivel to apply this action!\nStack Empty!!")
            return

        item = self.top.data
        self.top = self.top.next

        return item    
    


