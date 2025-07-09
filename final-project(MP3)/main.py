"""Entry point for the MP3 Song Management API using FastAPI.

This file initializes the FastAPI application and registers the routes
defined in the song controller.

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

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.controllers import song_router  # pylint: disable=import-error


app: FastAPI = FastAPI(
    title="MP3 Song Management API",
    description="API for managing MP3 songs with features like search, insert, delete, and update.",
    version="0.0.1"
)

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8001",
    "http://127.0.0.1",
    "http://127.0.0.1:8001",
    "http://127.0.0.1:8000",
    "null",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(song_router)
