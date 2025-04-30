
import time
from typing import List, Tuple

class InsertionSort:
    """
    Implements Insertion Sort with timing and step counting.
    """

    def __init__(self):
        self.steps = 0

    def sort(self, arr: List[int]) -> List[int]:
        """
        Sorts an array using Insertion Sort.

        Args:
            arr: List of integers to sort.

        Returns:
            Sorted list of integers.
        """
        self.steps = 0
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0:
                self.steps += 1
                if arr[j] > key:
                    arr[j + 1] = arr[j]
                    self.steps += 1
                    j -= 1
                else:
                    break
            arr[j + 1] = key
        return arr

    def measure(self, arr: List[int]) -> Tuple[List[int], float, int]:
        """
        Measures sorting time and steps for Insertion Sort.

        Args:
            arr: List of integers to sort.

        Returns:
            A tuple of (sorted list, elapsed time in seconds, step count).
        """
        data = arr.copy()
        start = time.perf_counter()
        sorted_list = self.sort(data)
        end = time.perf_counter()
        return sorted_list, end - start, self.steps
