import unittest

from selectionSort import selection_sort
#from mergeSort import mergeSort
#from bubbleSort import bubbleSort
from insertionSort import insertionSort
#import quickSort
#import heapSort

unsorted_positive_array = [5, 5, 7, 8, 2, 4, 1]

unsorted_negative_array = [-1, -3, -5, -7, -9, -5]

unsorted_integer_array = [-6, 0, -4, -5, 5, 5, 7, 8, 2, 4, 1]

empty_array = []

duplicate_number_array = [2, 2, 2, 2]

error_message = "The expected and achieved outcomes are not same"

class UnitTest(unittest.TestCase):
    def _test_sort(self, sort_func, input_list):
        expected_list = sorted(input_list)
        self.assertEqual(sort_func(input_list), expected_list, error_message)
    def test_selection_sort(self):
        print('\nTesting Selection Sort')
        print("For positive numbers")
        self._test_sort(selection_sort, unsorted_positive_array)
        print("For negative numbers")
        self._test_sort(selection_sort, unsorted_negative_array)
        print("For both positive and negative numvers")
        self._test_sort(selection_sort, unsorted_integer_array)
        print("For array with same numbers")
        self._test_sort(selection_sort, duplicate_number_array)
        print("For empty array")
        self._test_sort(bubbleSort, unsorted_positive_array)
        
    def test_insertion_sort(self):
        print("\nTesting Insertion Sort")
        print("For positive numbers")
        self._test_sort(insertionSort, unsorted_positive_array)
        print("For negative numbers")
        self._test_sort(insertionSort, unsorted_negative_array)
        print("For both positive and negative numvers")
        self._test_sort(insertionSort, unsorted_integer_array)
        print("For array with same numbers")
        self._test_sort(insertionSort, duplicate_number_array)
        print("For empty array")
        self._test_sort(insertionSort, unsorted_positive_array)
if __name__ == '__main__':
    unittest.main()
    