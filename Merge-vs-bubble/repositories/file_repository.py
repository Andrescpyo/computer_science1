
import os

class FileRepository:
    """Handles file operations for storing numbers."""

    DATA_PATH = os.path.join(os.path.dirname(__file__), "data")
    @staticmethod
    def save_numbers(filename: str, numbers: list[int]) -> None:
        """Saves a list of numbers to a text file.

        Args:
            filename (str): Name of the file.
            numbers (list[int]): List of numbers to save.
        """
        os.makedirs(FileRepository.DATA_PATH, exist_ok=True)
        file_path = os.path.join(FileRepository.DATA_PATH, filename)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write("\n".join(map(str, numbers)))

        print(f"File '{filename}' saved successfully.")
