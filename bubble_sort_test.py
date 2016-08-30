import unittest
import bubble_sort

class bubbleSortTestMethods(unittest.TestCase):

    bubble_sort Bubble = new bubble_sort()
    def setUp(self):
        self.unsortedArray = [3,2,1,4,5]


    def test_default(self):
     #   self.assertCountEqual(Bubble.bu,[1,2,3,4,5], 'Wrong after sorting')