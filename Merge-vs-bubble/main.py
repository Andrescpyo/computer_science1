
from controllers.random_number import RandomNumberController # pylint: disable=import-error
from controllers.sort import BubbleSortController, MergeSortController # pylint: disable=import-error

if __name__ == "__main__":
    # TODO: Add a counter to count the number of comparisons and swaps for each algorithm.
    RandomNumberController.generate_and_save()
    BubbleSortController.sort_and_save()
    MergeSortController.sort_and_save()
    