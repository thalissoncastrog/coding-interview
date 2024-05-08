from typing import Optional

class Node:

    def __init__(self, data, next: Optional['Node'] = None):
        self.data = data
        self.next = next
    

class LinkedList:

    def __init__(self, head: Optional['Node'] = None):
        self.head = head

    def AddFirst(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head
            self.head = newNode
    
    def AddAtIndex(self, data, index):
        newNode = Node(data)
        currentNode = self.head
        position = 0

        if(position == index):
            self.AddFirst(data)
        else:
            while(currentNode != None and position + 1 != index):
                position += 1
                currentNode = currentNode.next

                if currentNode != None:
                    newNode.next = currentNode.next
                    currentNode.next = newNode
                else: 
                    print("Index not present")

    def AddAtEnd(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return
        
        currentNode = self.head

        while(currentNode.next):
            currentNode = currentNode.next

        currentNode.next = newNode

    def UpdateNode(self, data, index):
        currentNode = self.head
        position = 0

        if position == index:
            currentNode.data = data # type: ignore
        else:
            while(currentNode != None and position != index):
                position += 1
                currentNode = currentNode.next

            if currentNode is not None:
                currentNode.data = data
            else:
                print("Index not present")

    def GetNodeAtIndex(self, index):

        currentNode = self.head

        if currentNode is None:
            return "Empty List"

        position = 0 

        if position == index:
            return currentNode.data
        
        while(currentNode != None and position != index):
            position += 1
            currentNode = currentNode.next
        
        if currentNode is not None:
            return currentNode.data
        
        return "Index not present"
                
            

    def RemoveFirstNode(self):
            
        if(self.head == None):
            return
        
        self.head = self.head.next
    
    def RemoveLastNode(self):

        if(self.head is None):
            return
        
        currentNode = self.head

        while(currentNode.next.next): # type: ignore
            currentNode = currentNode.next # type: ignore

        currentNode.next = None # type: ignore

    def RemoveAtIndex(self, index):
        
        if self.head is None:
            return
        
        currentNode = self.head
        position = 0

        if position == index:
            self.RemoveFirstNode()
        else:
            while(currentNode != None and position + 1 != index):
                position += 1
                currentNode = currentNode.next
            
            if currentNode is not None:
                currentNode.next = currentNode.next.next # type: ignore
            else:
                print("Index not present")

    def RemoveNode(self, data):
        currentNode = self.head

        if currentNode.data == data: # type: ignore
            self.RemoveFirstNode()
            return
    
        while(currentNode != None and currentNode.next.data != data): # type: ignore
            currentNode = currentNode.next

        if currentNode is not None:
            currentNode.next = currentNode.next.next # type: ignore

    def SizeOf(self):
        size = 0

        if self.head:
            currentNode = self.head
            while(currentNode):
                size += 1
                currentNode = currentNode.next
            
        return size
    
    def Print(self):
        currentNode = self.head

        while(currentNode):
            print(currentNode.data)
            currentNode = currentNode.next
            
