import unittest
from mergesort import MergeSort

class TestMergeSort(unittest.TestCase):
    
    def testBasicList(self):
        list = [12,5,3,9,7]

        MergeSort(list)

        # print(list)

        listSorted = [3, 5, 7, 9, 12]

        assert list == listSorted

    def testListAlreadySorted(self):
        list = [3, 5, 7, 9, 12]

        MergeSort(list)

        # print(list)

        listSorted = [3, 5, 7, 9, 12]

        assert list == listSorted
        
    def testListInverted(self):
        list = [12, 9, 7, 5, 3]

        MergeSort(list)

        # print(list)

        listSorted = [3, 5, 7, 9, 12]

        assert list == listSorted

    def testListRepeated(self):
        list = [12, 12, 7, 7, 3]

        MergeSort(list)

        # print(list)

        listSorted = [3, 7, 7, 12, 12]

        assert list == listSorted