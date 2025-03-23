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
        start_time = time.time()
        steps = 0
        iterations = 0
        n = len(data)
        for i in range(n):
            steps += 1  # Increment at the beginning of the outer loop
            iterations += 1  # Increment at the beginning of the outer loop
            for j in range(n - i - 1):
                steps += 1  # Increment for the comparison
                iterations += 1  # Increment for the comparison
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
                    steps += 1  # Increment for the swap
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
        steps = 0
        iterations = 0
        sorted_data, steps, iterations = MergeSort._merge_sort(data, steps, iterations)
        return sorted_data

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
        steps = 0
        iterations = 0
        sorted_data, steps, iterations = MergeSort._merge_sort(data, steps, iterations)
        print(f"Merge sort took {steps} comparison steps and {iterations} iterations.")
        return sorted_data

    @staticmethod
    def _merge_sort(data: list[int], steps: int, iterations: int) -> tuple[list[int], int, int]:
        """Recursive helper function for merge sort."""
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]
            steps += 1  # Increment for the assignment to mid            

            left_half, steps, iterations = MergeSort._merge_sort(left_half, steps, iterations)
            right_half, steps, iterations = MergeSort._merge_sort(right_half, steps, iterations)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                iterations += 1  # Increment for each evaluation of the while condition
                steps += 1      # Increment for the comparison
                if left_half[i] < right_half[j]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
                k += 1
                steps += 1  # Increment for the assignment to data[k]

            # Handle remaining elements in left_half
            while i < len(left_half):
                iterations += 1  # Increment for each evaluation of the while condition
                data[k] = left_half[i]
                i += 1
                k += 1
                steps += 1  # Increment for the assignment to data[k]

            # Handle remaining elements in right_half
            while j < len(right_half):
                iterations += 1  # Increment for each evaluation of the while condition
                data[k] = right_half[j]
                j += 1
                k += 1
                steps += 1  # Increment for the assignment to data[k]

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
        sorted_data, steps, iterations = MergeSort._merge_sort(data.copy(), 0, 0)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Merge sort took {elapsed_time:.20f} seconds.")
        print(f"Merge sort took {steps} comparison steps and {iterations} iterations.")
        return sorted_data