
import json
from typing import List


class JsonRepository:
    """Handles loading and saving JSON data from and to a file.

    Attributes:
        filepath (str): Path to the JSON file.
    """

    def __init__(self, filepath: str):
        """Initializes the repository with the path to the JSON file.

        Args:
            filepath (str): Full path to the JSON file.
        """
        self.filepath = filepath

    def load_data(self) -> List[dict]:
        """Loads and returns data from the JSON file.

        Returns:
            List[dict]: List of dictionary entries loaded from the file.
        
        Raises:
            ValueError: If the file exists but contains invalid JSON.
        """
        try:
            with open(self.filepath, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as exc:
            raise ValueError(f"Invalid JSON format in {self.filepath}.") from exc
    
    def save_data(self, data: List[dict]) -> None:
        """Saves the provided data to the JSON file.

        Args:
            data (List[dict]): List of dictionary entries to save.
        """
        with open(self.filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
