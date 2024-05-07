class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:

    def __init__(self):
        self.head = None

    def AddFirst(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            return
        else:
            newNode.next = self.head # type: ignore
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




