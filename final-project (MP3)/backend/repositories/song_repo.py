
from pydantic import BaseModel # Warning: This import is failed in the previous code snippet
from environmsent_variables import EnvironmentVariables
from repositories.base_repository import BaseRepository
from typing import Optional

class SongDAO(BaseModel):
    """Represents the data structure for a song.

    Attributes:
        id (int): Unique identifier for the song.
        title (str): Title of the song.
        artist (str): Artist name.
        album (str): Album name.
        year (int): Year of release.
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
        """Initializes the repository with the path to the songs data file."""
        env = EnvironmentVariables()
        super().__init__(env.path_songs_data)

    def _extract_data(self, data: list[dict]) -> list[dict]:
        """Extracts and returns the raw list of songs.

        This method allows for preprocessing or transformation
        of raw JSON data if needed.

        Args:
            data (list[dict]): Raw list of song dictionaries.

        Returns:
            list[dict]: Cleaned or validated list of song dictionaries.
        """
        return data

    def get_all_songs(self) -> list[SongDAO]:
        """Retrieves all songs in the repository as SongDAO objects.

        Returns:
            list[SongDAO]: List of all stored songs.
        """
        return [SongDAO(**song) for song in self.data]

    def get_song_by_id(self, song_id: int) -> Optional[SongDAO]:
        """Finds a song by its unique ID.

        Args:
            song_id (int): ID of the song to search.

        Returns:
            Optional[SongDAO]: The matching song, or None if not found.
        """
        for song in self.data:
            if song.get("id") == song_id:
                return SongDAO(**song)
        return None

    def get_song_by_title(self, title: str) -> Optional[SongDAO]:
        """Finds a song by its title, case-insensitive.

        Args:
            title (str): Title of the song to search.

        Returns:
            Optional[SongDAO]: The matching song, or None if not found.
        """
        for song in self.data:
            if song.get("title", "").lower() == title.lower():
                return SongDAO(**song)
        return None
