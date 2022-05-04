import unittest
import src.SinglelyLinkedList as LinkedList
import unittest

class TestLinkedList(unittest.TestCase) : 
    def testEmpty(self) :
        linkedList = LinkedList.LinkedList()
        self.assertEqual(linkedList.Size(), 0)

    def testLinkedAddDelete(self) : 
        linkedList = LinkedList.LinkedList()
        linkedList.Add(1)
        self.assertEqual(linkedList.Size(), 1)
        linkedList.Delete(1)
        self.assertFalse(linkedList.Contains(1))
        self.assertEqual(linkedList.Size(), 0)
    
    def testLinkedDeletionTwo(self) : 
        linkedList = LinkedList.LinkedList()
        for i in range(5) : 
            linkedList.Add(i)
        linkedList.Delete(3)
        self.assertFalse(linkedList.Contains(3))
    
    def testChange(self) : 
        linkedList = LinkedList.LinkedList()
        for i in range(5) : 
            linkedList.Add(i)
        linkedList.Change(3, 6)
        self.assertFalse(linkedList.Contains(3))
        self.assertTrue(linkedList.Contains(6))
        
    