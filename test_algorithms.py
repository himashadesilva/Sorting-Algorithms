from unittest import TestCase

from algorithms import bubbleSort, selectionSort, insertionSort


class TestBubbleSort(TestCase):
    def test_bubbleSort(self):
        self.assertEqual(bubbleSort([10, 5, -4, 25]), [-4, 5, 10, 25])
        self.assertEqual(bubbleSort([22, 4, 1, 4]), [1, 4, 4, 22])
        self.assertEqual(bubbleSort([100, -100, 1, 0]), [-100, 0, 1, 100])
        self.assertEqual(bubbleSort([0, 4, 0, -5, 1, 4]), [-5, 0, 0, 1, 4, 4])
        self.assertEqual(bubbleSort([]), [])
        self.assertEqual(bubbleSort([0,0,0]), [0,0,0])
        self.assertEqual(bubbleSort([12314, 235987, -54621]), [-54621, 12314, 235987])


class TestSelectionSort(TestCase):
    def test_selectionSort(self):
        self.assertEqual(selectionSort([10, 5, -4, 25]), [-4, 5, 10, 25])
        self.assertEqual(selectionSort([22, 4, 1, 4]), [1, 4, 4, 22])
        self.assertEqual(selectionSort([100, -100, 1, 0]), [-100, 0, 1, 100])
        self.assertEqual(selectionSort([0, 4, 0, -5, 1, 4]), [-5, 0, 0, 1, 4, 4])
        self.assertEqual(selectionSort([]), [])
        self.assertEqual(selectionSort([0,0,0]), [0,0,0])
        self.assertEqual(selectionSort([12314, 235987, -54621]), [-54621, 12314, 235987])



class TestInsertionSort(TestCase):
    def test_insertionSort(self):
        self.assertEqual(insertionSort([10, 5, -4, 25]), [-4, 5, 10, 25])
        self.assertEqual(insertionSort([22, 4, 1, 4]), [1, 4, 4, 22])
        self.assertEqual(insertionSort([100, -100, 1, 0]), [-100, 0, 1, 100])
        self.assertEqual(insertionSort([0, 4, 0, -5, 1, 4]), [-5, 0, 0, 1, 4, 4])
        self.assertEqual(insertionSort([]), [])
        self.assertEqual(insertionSort([0,0,0]), [0,0,0])
        self.assertEqual(insertionSort([12314, 235987, -54621]), [-54621, 12314, 235987])
