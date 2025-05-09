
import random

class RandomNumberService:
    """Service for generating random numbers."""

    @staticmethod
    def generate_numbers(count: int) -> list[int]:
        """Generates a list of random numbers.
        
        Args:
            count (int): Number of random numbers to generate.

        Returns:
            list[int]: List of random integers.
        """
        return [random.randint(1, 100000) for _ in range(count)]
