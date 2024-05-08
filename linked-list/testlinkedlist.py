import unittest
from linkedlist import LinkedList

class TestLinkedList(unittest.TestCase):

    def testAddFirst(self):
        linkList = LinkedList()

        linkList.AddFirst(5)

        result = linkList.GetNodeAtIndex(0)

        assert result == 5