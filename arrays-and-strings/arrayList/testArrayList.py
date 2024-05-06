from tokenize import String
import unittest
from arraylist import ArrayList

class TestArrayList(unittest.TestCase):

    def testIsEmpty(self):
        arrayList = ArrayList(15)
        
        result = arrayList.IsEmpty()

        assert result is True

    def testIsFull(self):
        arrayList = ArrayList(2)

        arrayList.Add(1)
        arrayList.Add(2)

        result = arrayList.IsFull()

        assert result is True

    def testAdd(self):
        arrList = ArrayList(2)

        arrList.Add(3)

        result = arrList.count

        assert result == 1

    def testAddAt(self):
        arrList = ArrayList(2)

        arrList.AddAt(0, 5)
        arrList.AddAt(1, 6)

        result = arrList.Get(0)

        assert result == 5

    def testRemove(self):
        arrList = ArrayList(2)

        arrList.AddAt(0, 5)
        arrList.AddAt(1, 6)

        arrList.Remove()

        result = arrList.count

        assert result == 1

    def testRemoveAt(self):
        arrList = ArrayList(2)

        arrList.AddAt(0, 5)
        arrList.AddAt(1, 6)

        arrList.RemoveAt(1)

        result = arrList.count

        assert result == 1

    def testSet(self):
        arrList = ArrayList(2)

        arrList.Add(5)
        arrList.Add(6)

        arrList.Set(0, 1)

        result = arrList.Get(0)

        assert result == 1

    def testSize(self):
        arrList = ArrayList(2)

        arrList.Add(5)
        arrList.Add(6)

        result = arrList.count

        assert result == 2

    def testClear(self):
        arrList = ArrayList(2)

        arrList.Add(5)
        arrList.Add(6)

        arrList.Clear()

        resultCount = arrList.count

        assert resultCount == 0

    def testToString(self):
        arrList = ArrayList(2)

        arrList.Add(5)
        arrList.Add(6)

        assert type(arrList.ToString()) is str
