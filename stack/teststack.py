import unittest
from stackImplementation import Stack

class TestStack(unittest.TestCase):

    def testIsEmpty(self):

        stack = Stack()

        result = stack.IsEmpty()

        assert result is True

    def testPush(self):

        stack = Stack()

        stack.Push(5)

        result = stack.Peek()

        assert result == 5
    
    def testPeek(self):

        stack = Stack()

        result = stack.Peek()

        assert result is None

    def testPop(self):

        stack = Stack()

        stack.Push(5)
        stack.Push(8)
        stack.Push(10)

        stack.Pop()
        result = stack.Peek()

        assert result == 8

    def testPopStackEmpty(self):

        stack = Stack()

        result = stack.Pop()

        assert result is None


        

