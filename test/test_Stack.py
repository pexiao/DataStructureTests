import src.Stack as Stack 

import unittest

class TestStack(unittest.TestCase) :
    
    def testEmpty(self) : 
        stack = Stack.Stack()
        self.assertEqual(stack.Size(), 0)
    
