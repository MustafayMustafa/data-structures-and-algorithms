import unittest
from typing import Optional


def binary_search(search_list: list, search_value) -> Optional[int]:
    """
    Binary Search Algorithm
    Returns the position of an element in a sorted list.

    :param search_list - a sorted list of elements.
    :param search_value - the value to search for in the search_list.
    :returns - the position the element exists in the array else, returns None.

    Time Complexity - O(log(n))
    """
    low = 0
    high = len(search_list) - 1

    while low <= high:
        midpoint = (low+high)//2

        if search_list[midpoint] == search_value:
            return midpoint
        elif search_list[midpoint] < search_value:
            low = midpoint + 1
        elif search_list[midpoint] > search_value:
            high = midpoint - 1

    return None


class TestBinarySearch(unittest.TestCase):
    sorted_list = [1, 2, 3, 4, 5]

    def test_search(self):
        self.assertEqual(binary_search(self.sorted_list, 1), 0)
        self.assertEqual(binary_search(self.sorted_list, 2), 1)
        self.assertEqual(binary_search(self.sorted_list, 5), 4)

    def test_not_in_list(self):
        self.assertIsNone(binary_search(self.sorted_list, 100))


if __name__ == '__main__':
    unittest.main()
