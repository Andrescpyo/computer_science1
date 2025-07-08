"""Service layer for managing songs using AVL tree and a JSON-based repository.

This module provides logic for inserting, deleting, searching, and updating
songs in both a persistent repository and an in-memory AVL tree, ensuring fast
lookups and ordered traversals.

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

from typing import Optional, List
from backend.services.avl_tree import AVLTree  # pylint: disable=import-error
from backend.repositories.song_repo import SongRepository, SongDAO  # pylint: disable=import-error


class SongService:
    """Service layer for managing song operations using AVL Tree and JSON repository."""

    def __init__(self):
        """Initializes the song service, loading songs into the AVL tree."""
        self._repo = SongRepository()
        self._tree = AVLTree()
        self._load_songs_to_tree()

    def _generate_key(self, song: SongDAO) -> str:
        """Generates a unique AVL key for a song using title, artist, and album.

        Args:
            song (SongDAO): Song object.

        Returns:
            str: Concatenated and normalized key.
        """
        return f"{song.title.lower()} - {song.artist.lower()} - {song.album.lower()}"

    def _load_songs_to_tree(self) -> None:
        """Loads all songs from the repository into the AVL tree."""
        songs = self._repo.get_all_songs()
        for song in songs:
            key = self._generate_key(song)
            self._tree.insert(key, song)

    def search_exact(self, title: str, artist: str, album: str) -> Optional[SongDAO]:
        """Searches for an exact match by title, artist, and album (case-insensitive).

        Args:
            title (str): Song title.
            artist (str): Artist name.
            album (str): Album name.

        Returns:
            Optional[SongDAO]: The matched song, or None if not found.
        """
        key = f"{title.lower()} - {artist.lower()} - {album.lower()}"
        return self._tree.search(key)

    def search_by_title_partial(self, title: str) -> List[SongDAO]:
        """Searches the AVL tree for songs with the given title substring.

        Args:
            title (str): Title substring (case-insensitive).

        Returns:
            List[SongDAO]: Songs that partially match the title.
        """
        matches = self._tree.search_partial(title.lower())
        return matches

    def get_all_sorted_by_title(self) -> List[SongDAO]:
        """Retrieves all songs sorted by title (including duplicates).

        Returns:
            List[SongDAO]: All songs in in-order AVL traversal.
        """
        return self._tree.get_all()

    def insert_song(self, song: dict) -> None:
        """Adds a song to both the repository and the AVL tree.

        Args:
            song (dict): Dictionary containing song fields.

        Raises:
            ValueError: If a song with the same ID already exists.
        """
        self._repo.add_song(song)
        dao = self._repo.get_song_by_id(song["id"])
        if dao:
            key = self._generate_key(dao)
            self._tree.insert(key, dao)

    def update_song(self, song_id: int, new_data: dict) -> None:
        """Updates an existing song and reloads the AVL tree.

        Args:
            song_id (int): ID of the song to update.
            new_data (dict): Dictionary with updated fields.

        Raises:
            ValueError: If the song with the given ID is not found.
        """
        self._repo.update_song(song_id, new_data)
        self._tree = AVLTree()
        self._load_songs_to_tree()

    def delete_song_by_id(self, song_id: int) -> None:
        """Deletes a song from the repository and updates the AVL tree.

        Args:
            song_id (int): ID of the song to delete.

        Raises:
            ValueError: If the song does not exist.
        """
        self._repo.delete_song(song_id)
        self._tree = AVLTree()
        self._load_songs_to_tree()
