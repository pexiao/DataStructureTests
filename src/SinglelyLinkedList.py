from typing import TypeVar, Generic, List, Optional

T = TypeVar('T')

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

    def Delete(self, value) -> None : 
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

    def Contains(self, value) -> bool : 
        currentNode : Node = self.head 
        while(currentNode) : 
            if (value == currentNode.data) : 
                return True
            currentNode = currentNode.next
        return False 
    
    def Change(self, originalValue, newValue) -> None : 
        currentNode : Node = self.head
        while(currentNode) : 
            if (originalValue == currentNode.data) : 
                currentNode.data = newValue
            currentNode = currentNode.next 

    def Size(self) -> int:
        return self.size 
