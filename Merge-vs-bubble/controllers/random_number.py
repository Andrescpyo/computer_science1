
from services.random_number import RandomNumberService # pylint: disable=import-error
from repositories.file_repository import FileRepository # pylint: disable=import-error

class RandomNumberController:
    """Controller to generate and save random numbers."""

    @staticmethod
    def generate_and_save():
        """Generates and saves random numbers in three different files."""
        sizes = [50, 100, 500, 1000, 5000, 10000]
        filenames = ["numbers_50.txt", "numbers_100.txt", "numbers_500.txt", "numbers_1000.txt","numbers_5000.txt", "numbers_10000.txt"]

        for size, filename in zip(sizes, filenames):
            numbers = RandomNumberService.generate_numbers(size)
            FileRepository.save_numbers(filename, numbers)
