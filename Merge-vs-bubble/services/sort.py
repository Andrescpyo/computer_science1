
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
        n = len(data)
        for i in range(n):
            for j in range(n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
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
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            MergeSort.sort(left_half)
            MergeSort.sort(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                data[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                data[k] = right_half[j]
                j += 1
                k += 1

        return data
