
from typing import List, Optional
from repositories.json_repo import JsonRepository

class SongRepository(JsonRepository):
    """Repository for managing song data stored in a JSON file."""

    def __init__(self):
        """Initializes the repository with the path to songs.json."""
        super().__init__("repositories/data/songs.json")

    def get_all_songs(self) -> List[dict]:
        """Returns all songs from the JSON file.

        Returns:
            List[dict]: A list of all song records.
        """
        return self.load_data()

    def get_song_by_id(self, song_id: int) -> Optional[dict]:
        """Returns a song by its unique ID.

        Args:
            song_id (int): ID of the song to retrieve.

        Returns:
            Optional[dict]: The song with the given ID, or None if not found.
        """
        for song in self.load_data():
            if song.get("id") == song_id:
                return song
        return None

    def add_song(self, song: dict) -> None:
        """Adds a new song to the repository.

        Args:
            song (dict): The song data to add. Must contain a unique "id" key.

        Raises:
            ValueError: If a song with the same ID already exists.
        """
        data = self.load_data()
        if any(existing.get("id") == song["id"] for existing in data):
            raise ValueError(f"Song with id {song['id']} already exists.")
        data.append(song)
        self.save_data(data)

    def delete_song(self, song_id: int) -> None:
        """Deletes a song by its ID.

        Args:
            song_id (int): ID of the song to delete.
        """
        data = self.load_data()
        new_data = [song for song in data if song.get("id") != song_id]
        self.save_data(new_data)

    def update_song(self, song_id: int, new_data: dict) -> None:
        """Updates an existing song with new data.

        Args:
            song_id (int): ID of the song to update.
            new_data (dict): Dictionary containing the updated fields.

        Raises:
            ValueError: If the song with the given ID is not found.
        """
        data = self.load_data()
        for index, song in enumerate(data):
            if song.get("id") == song_id:
                data[index].update(new_data)
                self.save_data(data)
                return
        raise ValueError(f"Song with id {song_id} not found.")
