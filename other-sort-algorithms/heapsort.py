
import time
from typing import List, Tuple

class HeapSort:
    """
    Implements Heap Sort with timing and step counting.
    """

    def __init__(self):
        self.steps = 0

    def _heapify(self, arr: List[int], n: int, i: int) -> None:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n:
            self.steps += 1
            if arr[left] > arr[largest]:
                largest = left
        if right < n:
            self.steps += 1
            if arr[right] > arr[largest]:
                largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.steps += 1
            self._heapify(arr, n, largest)

    def sort(self, arr: List[int]) -> List[int]:
        """
        Sorts an array using Heap Sort.

        Args:
            arr: List of integers to sort.

        Returns:
            Sorted list of integers.
        """
        self.steps = 0
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self._heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.steps += 1
            self._heapify(arr, i, 0)
        return arr

    def measure(self, arr: List[int]) -> Tuple[List[int], float, int]:
        """
        Measures sorting time and steps for Heap Sort.

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
