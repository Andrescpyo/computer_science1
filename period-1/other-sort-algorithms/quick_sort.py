
import time
from typing import List, Tuple

class QuickSort:
    """
    Implements the QuickSort algorithm with timing and step counting.
    """

    def __init__(self):
        self.steps = 0

    def _partition(self, arr: List[int], low: int, high: int) -> int:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            self.steps += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                self.steps += 1
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        self.steps += 1
        return i + 1

    def sort(self, arr: List[int]) -> List[int]:
        """
        Sorts an array using QuickSort.

        Args:
            arr: List of integers to sort.

        Returns:
            Sorted list of integers.
        """
        self.steps = 0
        self._quicksort(arr, 0, len(arr) - 1)
        return arr

    def _quicksort(self, arr: List[int], low: int, high: int) -> None:
        if low < high:
            pi = self._partition(arr, low, high)
            self._quicksort(arr, low, pi - 1)
            self._quicksort(arr, pi + 1, high)

    def measure(self, arr: List[int]) -> Tuple[List[int], float, int]:
        """
        Measures sorting time and steps for QuickSort.

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
