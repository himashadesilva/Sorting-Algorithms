from unittest import TestCase
from MergeSort import mergeSort


class TestmergeSort(TestCase):
    def test_mergeSort(self):
        a = [10, 5, -4, 25]
        self.assertEqual(mergeSort(a, 0, len(a) - 1), [-4, 5, 10, 25])
        a = [22, 4, 1, 4]
        self.assertEqual(mergeSort(a, 0, len(a) - 1), [1, 4, 4, 22])
        a = [100, -100, 1, 0]
        self.assertEqual(mergeSort(a, 0, len(a) - 1), [-100, 0, 1, 100])
        a = [0, 4, 0, -5, 1, 4]
        self.assertEqual(mergeSort(a, 0, len(a) - 1), [-5, 0, 0, 1, 4, 4])
        a = [0, 0, 0];
        self.assertEqual(mergeSort(a, 0, len(a) - 1), [0, 0, 0])
        a = [12314, 235987, -54621]
        self.assertEqual(mergeSort(a, 0, len(a) - 1), [-54621, 12314, 235987])
