from typing import Optional

from more_itertools import first

class Node:

    def __init__(self, data, next: Optional['Node'] = None):
        self.data = data
        self.next = next

class Queue:

    def __init__(self, first: Optional['None'] = None, 
                 last: Optional['Node'] = None):
        
        self.first = first
        self.last = last

    def Add(self, item):

        newNode = Node(item)

        if self.last is not None:
            self.last.next = newNode
        
        self.last = newNode

        if self.first is None:
            self.first = self.last
        
    def Remove(self):

        if self.first is None:
            print("Impossibly apply this action\nQueue is Empty!!")
            return
    
        data = self.first.data
        self.first = first.next

        if self.first is None:
           self.last = None 
        
        return data
    
    def Peek(self):

        if self.first is None:
            print("Queue Empty!!")
            return
        
        return self.first.data
    
    def IsEmpty(self):
        
        return self.first is None