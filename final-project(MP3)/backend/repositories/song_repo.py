"""Defines the repository class for managing song data.

This module is part of the MP3AVLtree project and includes the
SongRepository class for interacting with songs stored in JSON format.

Author: Juan Esteban Bedoya <jebedoyal@udistrital.edu.co>

This file is part of the MP3AVLtree project.

MP3AVLtree is free software: you can redistribute it and/or modify it under 
the terms of the GNU General Public License as published by the Free Software 
Foundation, either version 3 of the License, or (at your option) any later version.

MP3AVLtree is distributed in the hope that it will be useful, but WITHOUT ANY 
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR 
A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with 
MP3AVLtree. If not, see <https://www.gnu.org/licenses/>.
"""

from typing import Optional
from pydantic import BaseModel  # pylint: disable=no-name-in-module
from backend.repositories.json_repo import JsonRepository as BaseRepository  # pylint: disable=import-error


class SongDAO(BaseModel):
    """Represents the data structure for a song.

    Attributes:
        id (int): Unique identifier for the song.
        title (str): Title of the song.
        artist (str): Artist name.
        album (str): Album name.
        year (int): Year the song was released.
        duration (int): Duration of the song in seconds.
    """
    id: int
    title: str
    artist: str
    album: str
    year: int
    duration: int


class SongRepository(BaseRepository):
    """Repository for managing song data using SongDAO."""

    def __init__(self):
        """Initializes the repository with the songs JSON file path."""
        super().__init__("backend/repositories/data/songs.json")

    def _extract_data(self, data: list[dict]) -> list[dict]:
        """(Optional override) Extracts song data from raw JSON list.

        Args:
            data (list[dict]): Raw list of dictionaries from JSON.

        Returns:
            list[dict]: Cleaned or validated song entries.
        """
        return data

    def get_all_songs(self) -> list[SongDAO]:
        """Retrieves all songs from the repository.

        Returns:
            list[SongDAO]: List of all songs as DAO objects.
        """
        data = self.load_data()
        return [SongDAO(**song) for song in data]

    def get_song_by_id(self, song_id: int) -> Optional[SongDAO]:
        """Retrieves a song by its ID.

        Args:
            song_id (int): ID of the song to search.

        Returns:
            Optional[SongDAO]: The matching song or None.
        """
        data = self.load_data()
        for song in data:
            if song.get("id") == song_id:
                return SongDAO(**song)
        return None

    def get_song_by_title(self, title: str) -> Optional[SongDAO]:
        """Retrieves a song by its title (case-insensitive).

        Args:
            title (str): Title of the song to search.

        Returns:
            Optional[SongDAO]: The matching song or None.
        """
        data = self.load_data()
        for song in data:
            if song.get("title", "").lower() == title.lower():
                return SongDAO(**song)
        return None

    def add_song(self, song: dict) -> None:
        """Adds a new song to the repository.

        Args:
            song (dict): Song data. Should not include an ID.

        Raises:
            TypeError: If the provided song is not a dictionary.
            ValueError: If the song already includes an ID.
        """
        data = self.load_data()
        if not isinstance(song, dict):
            raise TypeError("Song must be a dictionary.")
        if "id" in song:
            raise ValueError("Song must not include an ID. It is auto-assigned.")

        last_id = max((s["id"] for s in data), default=0)
        song["id"] = last_id + 1
        data.append(song)
        self.save_data(data)

    def update_song(self, song_id: int, new_data: dict) -> None:
        """Updates an existing song.

        Args:
            song_id (int): ID of the song to update.
            new_data (dict): Fields to update.

        Raises:
            ValueError: If the song is not found.
        """
        data = self.load_data()
        for i, song in enumerate(data):
            if song["id"] == song_id:
                data[i].update(new_data)
                self.save_data(data)
                return
        raise ValueError(f"Song with ID {song_id} not found.")

    def delete_song(self, song_id: int) -> None:
        """Deletes a song from the repository.

        Args:
            song_id (int): ID of the song to delete.

        Raises:
            ValueError: If the song does not exist.
        """
        data = self.load_data()
        initial_len = len(data)
        data = [song for song in data if song["id"] != song_id]
        if len(data) == initial_len:
            raise ValueError(f"Song with ID {song_id} not found.")
        self.save_data(data)
