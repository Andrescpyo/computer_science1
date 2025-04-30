
import random
import os

class RandomGenerator:
    """
    Generates a text file containing random integers separated by commas.
    """

    def __init__(self, count: int, lower: int, upper: int):
        """
        Args:
            count: Number of random integers to generate.
            lower: Minimum integer value (inclusive).
            upper: Maximum integer value (inclusive).
        """
        self.count = count
        self.lower = lower
        self.upper = upper

    def generate(self, filename: str) -> None:
        """
        Writes `count` random integers to `filename`, separated by commas.

        Args:
            filename: Relative path to output text file.
        """
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        numbers = [str(random.randint(self.lower, self.upper)) for _ in range(self.count)]
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(','.join(numbers))

    def read_numbers(self, filename: str):
        """
        Reads integers from a comma-separated file.

        Args:
            filename: Path to input file.

        Returns:
            List of integers.
        """
        with open(filename, 'r', encoding="utf-8") as f:
            content = f.read().strip()
        return [int(x) for x in content.split(',') if x]


    def write_numbers(self, filename: str, arr: list):
        """
        Writes integers to a file separated by commas.

        Args:
            filename: Path to output file.
            arr: List of integers to write.
        """
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(','.join(str(x) for x in arr))
