import queue
import unittest
from queueImplementation import Queue

class TestQueue(unittest.TestCase):

    def testAdd(self):

        queue = Queue()

        queue.Add(5)
        queue.Add(6)

        result = queue.Peek()

        assert result == 5
    
    def testRemove(self):

        queue = Queue()

        queue.Add(5)
        queue.Add(6)

        item = queue.Remove()

        result = queue.Peek()

        assert result == 6

    def testIsEmpty(self):

        queue = Queue()

        queue.Add(5)
        queue.Add(7)

        item = queue.Remove()
        item = queue.Remove()

        result = queue.IsEmpty()

        assert result is True
