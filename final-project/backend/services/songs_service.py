from typing import Optional, List
from services.avl_tree import AVLTree
from repositories.song_repo import SongRepository


class SongService:
    """Service layer for managing song operations using AVL Tree and JSON repository."""

    def __init__(self):
        """Initializes the service with a song repository and AVL tree."""
        self._repo = SongRepository()
        self._tree = AVLTree()
        self._load_songs_to_tree()

    def _load_songs_to_tree(self) -> None:
        """Loads all songs from the repository into the AVL tree using the lowercase title as key."""
        songs = self._repo.get_all_songs()
        for song in songs:
            title_key = song["title"].lower()
            self._tree.insert(title_key, song)

    def search_by_title(self, title: str) -> Optional[dict]:
        """Searches for a song by its title (case-insensitive).

        Args:
            title (str): Title of the song to search for.

        Returns:
            Optional[dict]: The song if found, or None otherwise.
        """
        return self._tree.search(title.lower())

    def get_all_sorted_by_title(self) -> List[dict]:
        """Returns all songs sorted alphabetically by title.

        Returns:
            List[dict]: A list of all songs in alphabetical order by title.
        """
        return self._tree.get_all()

    def insert_song(self, song: dict) -> None:
        """Inserts a new song into both the repository and the AVL tree.

        Args:
            song (dict): Song data. Must contain a unique 'id' and a 'title'.

        Raises:
            ValueError: If the song's ID already exists in the repository.
        """
        self._repo.add_song(song)
        self._tree.insert(song["title"].lower(), song)

    def delete_song_by_title(self, title: str) -> None:
        """Deletes a song by title from both the AVL tree and the JSON repository.

        Args:
            title (str): Title of the song to delete (case-insensitive).
        """
        song = self._tree.search(title.lower())
        if song:
            self._tree.delete(title.lower())
            self._repo.delete_song(song["id"])

    def update_song(self, song_id: int, new_data: dict) -> None:
        """Updates a song in the repository and reloads the AVL tree.

        Args:
            song_id (int): ID of the song to update.
            new_data (dict): Dictionary with updated song data.

        Raises:
            ValueError: If the song with the given ID is not found.
        """
        self._repo.update_song(song_id, new_data)
        self._tree = AVLTree()
        self._load_songs_to_tree()
