
from services.sort import BubbleSort, MergeSort # pylint: disable=import-error
from repositories.file_repository import FileRepository # pylint: disable=import-error

class BubbleSortController:
    """Controller to sort a list of numbers using bubble sort algorithm and save it."""

    @staticmethod
    def sort_and_save():
        """Sorts a list of numbers using bubble sort algorithm and saves it in 
        three different files."""
        filenames = ["numbers_100.txt", "numbers_1000.txt", "numbers_10000.txt"]
        new_filenames = ["bubble_100.txt", "bubble_1000.txt", "bubble_10000.txt"]

        for filename, new_filename in zip(filenames, new_filenames):
            numbers = FileRepository.load_numbers(filename)
            sorted_numbers = BubbleSort.sort(numbers)
            FileRepository.save_numbers(new_filename, sorted_numbers)

class MergeSortController:
    """Controller to sort a list of numbers using merge sort algorithm and save it."""

    @staticmethod
    def sort_and_save():
        """Sorts a list of numbers using merge sort algorithm and saves it in 
        three different files."""
        filenames = ["numbers_100.txt", "numbers_1000.txt", "numbers_10000.txt"]
        new_filenames = ["merge_100.txt", "merge_1000.txt", "merge_10000.txt"]

        for filename, new_filename in zip(filenames, new_filenames):
            numbers = FileRepository.load_numbers(filename)
            sorted_numbers = MergeSort.sort_time(numbers)
            FileRepository.save_numbers(new_filename, sorted_numbers)
