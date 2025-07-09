"""This module defines the FastAPI endpoints for managing songs
in the MP3AVLtree project.

It provides routes for retrieving, searching, inserting, updating,
and deleting song records stored in a JSON file and organized 
internally using an AVL Tree for efficient access.

Author: Juan Esteban Bedoya <jebedoyal@udistrital.edu.co>

This file is part of the MP3AVLtree project.

MP3AVLtree is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

MP3AVLtree is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with MP3AVLtree. If not, see <https://www.gnu.org/licenses/>.
"""

from typing import List, Optional
from fastapi import APIRouter, HTTPException, Body
from backend.services.song_service import SongService  # pylint: disable=import-error
from backend.repositories.song_repo import SongDAO  # pylint: disable=import-error

router = APIRouter()
services = SongService()


@router.get("/songs/all", response_model=List[SongDAO], summary="Get All Songs sorted by title")
def get_all_songs() -> List[dict]:
    """Fetches all songs sorted alphabetically by title.

    Returns:
        List[SongDAO]: List of all song records.
    """
    return services.get_all_sorted_by_title()


@router.get("/songs/search/{title}", response_model=List[SongDAO], summary="Search songs by partial title match")
def search_song_by_title(title: str) -> List[dict]:
    """Searches for songs by partial title (case-insensitive).

    Args:
        title (str): Partial or full title of the song.

    Returns:
        List[SongDAO]: List of matching songs.

    Raises:
        HTTPException: If title is empty or no matches are found.
    """
    if not title:
        raise HTTPException(status_code=400, detail="Title cannot be empty.")
    matches = services.search_by_title_partial(title)
    if not matches:
        raise HTTPException(status_code=404, detail="No matching songs found.")
    return matches


@router.post("/songs/add", response_model=dict, status_code=201, summary="Add a new song to the repository")
def add_song(song: SongDAO):
    """Adds a new song to the repository.

    Args:
        song (SongDAO): Song data to be added.

    Returns:
        dict: Success message.

    Raises:
        HTTPException: If the song could not be added (e.g., duplicate ID).
    """
    try:
        services.insert_song(song.model_dump(exclude_none=True))
        return {"message": "Song added successfully."}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e


@router.put("/songs/{song_id}", response_model=dict, summary="Update an existing song by ID")
def update_song(song_id: int, new_data: dict = Body(...)):
    """Updates an existing song by ID.

    Args:
        song_id (int): ID of the song to update.
        new_data (SongDao): Song fields to update. 

    Returns:
        dict: Success message.

    Raises:
        HTTPException: If the song does not exist or update fails.
    """
    try:
        services.update_song(song_id, new_data.model_dump(exclude_unset=True))
        return {"message": f"Song with ID {song_id} updated successfully."}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e)) from e


@router.delete("/songs/delete/{song_id} ", response_model=dict, summary="Delete a song by its ID")
def delete_song_by_id(song_id: int):
    """Deletes a song by its ID.

    Args:
        song_id (int): ID of the song to delete.

    Returns:
        dict: Success message.

    Raises:
        HTTPException: If the song does not exist.
    """
    try:
        services.delete_song_by_id(song_id)
        return {"message": f"Song with ID {song_id} was deleted successfully."}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e)) from e
