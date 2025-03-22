import time

class BubbleSort:
    """Service for sorting a list of numbers using bubble sort algorithm."""

    @staticmethod
    def sort(data: list[int]) -> list[int]:
        """Sorts the list of numbers using bubble sort algorithm.
        
        Args:
            data (list[int]): List of numbers to sort.

        Returns:
            list[int]: Sorted list of numbers.
        """

        start_time = time.time() #measure the time
        steps = 0                #count the number of steps
        iterations = 0           #count the number of iterations

        n = len(data)
        for i in range(n):
            iterations += 1
            for j in range(n-i-1):
                steps += 1
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
                    steps += 1  #count the swaps as a step
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Bubble sort took {elapsed_time:.20f} seconds.")
        print(f"Bubble sort took {steps} steps and {iterations} iterations.")
        return data

class MergeSort:
    """Service for sorting a list of numbers using merge sort algorithm."""

    @staticmethod
    def sort(data: list[int]) -> list[int]:
        """Sorts the list of numbers using merge sort algorithm.
        
        Args:
            data (list[int]): List of numbers to sort.

        Returns:
            list[int]: Sorted list of numbers.
        """

        steps = 0                #count the number of steps
        iterations = 0           #count the number of iterations
        return MergeSort._merge_sort(data, steps, iterations)[0]

    @staticmethod
    def _merge_sort(data: list[int], steps: int, iterations: int) -> tuple[list[int], int, int]:
        """Recursive helper function for merge sort."""
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            left_half, steps, iterations = MergeSort._merge_sort(left_half, steps, iterations)
            right_half, steps, iterations = MergeSort._merge_sort(right_half, steps, iterations)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                iterations += 1
                if left_half[i] < right_half[j]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
                k += 1
                steps += 1

            while i < len(left_half):
                data[k] = left_half[i]
                i += 1
                k += 1
                steps += 1
                iterations += 1

            while j < len(right_half):
                data[k] = right_half[j]
                j += 1
                k += 1
                steps += 1
                iterations += 1
        return data, steps, iterations
    
    @staticmethod
    def sort_time(data: list[int]) -> list[int]:
        """Sorts the list of numbers using merge sort algorithm and measures time.
        
        Args:
            data (list[int]): List of numbers to sort.

        Returns:
            list[int]: Sorted list of numbers.
        """
        start_time = time.time()
        sorted_data, steps, iterations = MergeSort._merge_sort(data.copy(), 0, 0) # Make a copy to avoid modifying original in place
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Merge sort took {elapsed_time:.20f} seconds.")
        print(f"Merge sort took {steps} steps and {iterations} iterations.")
        return sorted_data
