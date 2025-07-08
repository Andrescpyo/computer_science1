"""Initializes the controllers package for the MP3AVLtree project.

This module registers all API routers from the controller layer, 
exposing them for inclusion in the FastAPI application.

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

from backend.controllers.song_controller import router as song_router  # pylint: disable=import-error
