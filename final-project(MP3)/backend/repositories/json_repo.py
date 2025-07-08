"""Provides a base repository for working with JSON data files.

This module is part of the MP3AVLtree project and defines the JsonRepository
class, which handles loading and saving structured data in JSON format.

Author: Juan Esteban Bedoya <jebedoyal@udistrital.edu.co>

This file is part of the MP3AVLtree project.

MP3AVLtree is free software: you can redistribute it and/or modify it under the 
terms of the GNU General Public License as published by the Free Software 
Foundation, either version 3 of the License, or (at your option) any later version.

MP3AVLtree is distributed in the hope that it will be useful, but WITHOUT ANY 
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR 
A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with 
MP3AVLtree. If not, see <https://www.gnu.org/licenses/>.
"""

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
