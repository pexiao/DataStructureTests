from typing import TypeVar, Generic, List, Optional

T = TypeVar('T')

class Stack(Generic[T]) : 
    
    def __init__(self) -> None :
        self.list : List[T] = []
        self.top = T 
        self.size = 0

    def Top(self) -> T : 
        return self.top
    
    def Push(self, value: T) -> None : 
        # Append the value to the list 
        # Update values for top and size 

        self.list.append(value)
        self.top = value
        self.size = self.size + 1 
    
    def Pop(self) -> Optional[T] : 
        # Remove from the top of the list 
        # Update values for top and size 

        if self.Size() == 0 :
            return None
        returnValue : T = self.list.pop()
        self.size = self.size - 1
        
        # Edge case to take care of indexing 
        if self.size == 0 : 
            self.top = None
        else : 
            self.top = self.list[self.size - 1]

        return returnValue
    
    def Size(self) -> int : 
        return self.size