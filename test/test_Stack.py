import src.Stack as Stack 
import unittest

class TestStack(unittest.TestCase) :
    
    def testEmpty(self) : 
        # Simple test to test an empty stack 
        stack = Stack.Stack()
        self.assertEqual(stack.Size(), 0)

    def testStackOne(self) : 
        # Test to test push andd pop one value 
        stack = Stack.Stack()
        self.assertEqual(stack.Size(), 0)

        stack.Push(1)
        self.assertEqual(stack.Top(), 1)

        value = stack.Pop()
        self.assertEqual(value, 1)

    def testStackMany(self) : 
        stack = Stack.Stack()
        
        stack.Push(1)
        stack.Push(2)
        value = stack.Pop()
        self.assertEqual(value, 2)

        stack.Push(3)
        stack.Push(4)
        value = stack.Pop()
        self.assertEqual(value, 4)

        value = stack.Pop()
        self.assertEqual(value, 3)

        value = stack.Pop()
        self.assertEqual(value, 1)

        self.assertEqual(stack.Size(), 0)

    def testMultiple(self) : 
        stack = Stack.Stack()
        for i in range(10) :
            stack.Push(i)
        self.assertEqual(stack.Size(), 10)
        for i in range(10) : 
            value = stack.Pop()
            self.assertEqual(value, 9 - i )
    

