
from threading import currentThread


class Node : 
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList : 
    
    def __init__(self) -> None:
        self.head = None
        self.size = 0 
    
    def Add(self, value) -> None : 
        newNode : Node = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.size = self.size + 1 

    def Delete(self, value) : 
        currentNode : Node = self.head 
        prevNode : Node = None 
        while(currentNode) :
            if (value == currentNode.data) : 
                if (prevNode) : 
                    prevNode.next = currentNode.next 
                currentNode.next = None 
                currentNode.data = None 
                self.size = self.size - 1
                return 
            prevNode = currentNode
            currentNode = currentNode.next 

    def RemoveAt(self, index : int) : 
        if (index >= self.size or index < 0) : 
            print("Cannot be removed due to index out of bounds")
            return 

        currentNode : Node = self.head 
        prevNode : Node = None

        i = 0
        while (index > i) : 
            prevNode = currentNode
            currentNode = currentNode.next
        
        if (prevNode) :
            prevNode.next = currentNode.next
        currentNode.next = None 
        currentNode.data = None 

    def Size(self) -> int:
        return self.size 
