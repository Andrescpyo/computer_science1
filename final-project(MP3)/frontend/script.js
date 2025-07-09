document.addEventListener('DOMContentLoaded', () => {
    // Referencias a elementos del DOM
    const nowPlayingScreen = document.getElementById('nowPlayingScreen');
    const libraryScreen = document.getElementById('libraryScreen');
    const searchScreen = document.getElementById('searchScreen');
    const addSongModalMP3 = document.getElementById('addSongModalMP3');

    const menuButtonMP3 = document.getElementById('menuButtonMP3');
    const backToNowPlaying = document.getElementById('backToNowPlaying');
    const searchMenuButtonMP3 = document.getElementById('searchMenuButtonMP3');
    const searchButtonMP3 = document.getElementById('searchButtonMP3');
    const backToLibraryFromSearch = document.getElementById('backToLibraryFromSearch');
    const addSongMenuButtonMP3 = document.getElementById('addSongMenuButtonMP3');
    const closeAddModalMP3 = document.getElementById('closeAddModalMP3');
    const addSongFormMP3 = document.getElementById('addSongFormMP3');

    const mp3LibraryList = document.getElementById('mp3LibraryList');
    const searchInputMP3 = document.getElementById('searchInputMP3');
    const searchResultsList = document.getElementById('searchResultsList');

    // NUEVAS REFERENCIAS: Botones de navegación de la rueda
    const prevButtonMP3 = document.getElementById('prevButtonMP3');
    const nextButtonMP3 = document.getElementById('nextButtonMP3');
    // Si tienes un botón de Play/Pause, también lo necesitarás aquí
    // const playPauseButtonMP3 = document.getElementById('playPauseButtonMP3'); // Si lo vas a implementar más tarde

    // Estado global de la aplicación (simula un reproductor)
    let currentScreen = 'nowPlaying'; // 'nowPlaying', 'library', 'search'
    let allSongs = [];
    let currentPlayingSongIndex = -1; // Índice de la canción reproduciéndose

    // Base URL de tu API de FastAPI
    const API_BASE_URL = 'http://127.0.0.1:8000'; // Asegúrate de que coincida con el puerto de tu backend

    // Función para mostrar una pantalla específica
    function showScreen(screenName) {
        nowPlayingScreen.classList.remove('active-screen');
        libraryScreen.classList.remove('active-screen');
        searchScreen.classList.remove('active-screen');
        addSongModalMP3.style.display = 'none'; // Asegúrate de que el modal esté oculto

        switch (screenName) {
            case 'nowPlaying':
                nowPlayingScreen.classList.add('active-screen');
                currentScreen = 'nowPlaying';
                break;
            case 'library':
                libraryScreen.classList.add('active-screen');
                currentScreen = 'library';
                loadSongsIntoLibrary(); // Cargar canciones cada vez que entras a la biblioteca
                break;
            case 'search':
                searchScreen.classList.add('active-screen');
                currentScreen = 'search';
                searchResultsList.innerHTML = ''; // Limpiar resultados anteriores
                break;
            case 'addSong':
                addSongModalMP3.style.display = 'flex';
                // No cambiamos el currentScreen principal porque el modal es una superposición
                break;
        }
    }

    // --- Funciones de Interacción con el Backend ---

    async function fetchAllSongs() {
        try {
            const response = await fetch(`${API_BASE_URL}/songs/all`);
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Error al cargar las canciones');
            }
            const data = await response.json();
            allSongs = data; // Almacenar todas las canciones

            // Si es la primera carga y no hay canción reproduciéndose, reproduce la primera
            if (currentPlayingSongIndex === -1 && allSongs.length > 0) {
                currentPlayingSongIndex = 0;
                displaySong(allSongs[currentPlayingSongIndex]);
            }
            return data;
        } catch (error) {
            console.error('Error fetching all songs:', error);
            alert(`Error: ${error.message}. Por favor, verifica que el backend esté funcionando.`);
            return [];
        }
    }

    async function searchSongs(query) {
        try {
            const response = await fetch(`${API_BASE_URL}/songs/search/${encodeURIComponent(query)}`);
            if (!response.ok) {
                const errorData = await response.json();
                if (response.status === 404 && errorData.detail === "No matching songs found.") {
                    return [];
                }
                throw new Error(errorData.detail || 'Error al buscar canciones');
            }
            const data = await response.json();
            return data;
        } catch (error) {
            console.error('Error searching songs:', error);
            alert(`Error: ${error.message}`);
            return [];
        }
    }

    async function addSongToBackend(songData) {
        try {
            const response = await fetch(`${API_BASE_URL}/songs/add`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(songData)
            });
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Error al añadir la canción');
            }
            const result = await response.json();
            alert(result.message);
            await fetchAllSongs();
            loadSongsIntoLibrary();
            return true;
        } catch (error) {
            console.error('Error adding song:', error);
            alert(`Error al añadir canción: ${error.message}`);
            return false;
        }
    }

    async function deleteSongFromBackend(songId) {
        try {
            const response = await fetch(`${API_BASE_URL}/songs/delete/${songId}`, {
                method: 'DELETE'
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Error al eliminar la canción');
            }

            const result = await response.json();
            alert(result.message);

            // Recargar todas las canciones y la biblioteca después de eliminar
            await fetchAllSongs(); // Esto actualizará `allSongs`
            loadSongsIntoLibrary();

            // Lógica adicional para manejar la eliminación de la canción actualmente en reproducción
            if (currentPlayingSongIndex !== -1 && allSongs.length > 0) {
                // Si la canción eliminada era la que se estaba reproduciendo,
                // o si el índice actual ahora es inválido (ej. era la última y se eliminó)
                const deletedSongIndex = allSongs.findIndex(song => song.id === songId);
                if (deletedSongIndex === currentPlayingSongIndex) {
                    // Si se eliminó la canción actual, intentar reproducir la siguiente o la primera
                    if (allSongs.length > 0) {
                        currentPlayingSongIndex = Math.min(deletedSongIndex, allSongs.length - 1);
                        displaySong(allSongs[currentPlayingSongIndex]);
                    } else {
                        // No hay más canciones
                        displaySong({ title: 'No hay canciones', artist: '', album: '', year: '', duration: 0 });
                        currentPlayingSongIndex = -1;
                    }
                } else if (deletedSongIndex < currentPlayingSongIndex) {
                    // Si se eliminó una canción anterior a la actual, el índice de la actual se desplaza
                    currentPlayingSongIndex--;
                }
                // Si la canción actualmente en reproducción es válida después de la eliminación, simplemente se mantiene
                if (currentPlayingSongIndex !== -1 && allSongs.length > 0) {
                    displaySong(allSongs[currentPlayingSongIndex]);
                }
            } else if (allSongs.length === 0) {
                // Si no quedan canciones
                displaySong({ title: 'No hay canciones', artist: '', album: '', year: '', duration: 0 });
                currentPlayingSongIndex = -1;
            }

            return true;
        } catch (error) {
            console.error('Error deleting song:', error);
            alert(`Error al eliminar canción: ${error.message}`);
            return false;
        }
    }

    // --- Funciones de Renderizado y Lógica del MP3 Player ---

    function displaySong(song) {
        const playerSongTitle = document.getElementById('playerSongTitle');
        const playerArtistAlbum = document.getElementById('playerArtistAlbum');
        const durationElement = document.getElementById('playerDuration');

        if (song) {
            playerSongTitle.textContent = song.title;
            playerArtistAlbum.textContent = `${song.artist} - ${song.album} (${song.year})`;
            const minutes = Math.floor(song.duration / 60);
            const seconds = song.duration % 60;
            durationElement.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
        } else {
            playerSongTitle.textContent = 'No hay canción';
            playerArtistAlbum.textContent = 'N/A';
            durationElement.textContent = '00:00';
        }
        // Nota: la barra de progreso y el tiempo restante requerirían una API de audio real
        // o una simulación más compleja con setInterval.
    }

    function renderSongList(songs, targetListElement) {
        targetListElement.innerHTML = '';
        if (songs.length === 0) {
            const noResultsItem = document.createElement('li');
            noResultsItem.textContent = "No hay canciones para mostrar.";
            targetListElement.appendChild(noResultsItem);
            return;
        }

        songs.forEach((song, index) => { // Asegúrate de obtener el índice aquí
            const listItem = document.createElement('li');
            listItem.classList.add('song-item');

            const songInfo = document.createElement('span');
            songInfo.textContent = `${song.title} - ${song.artist}`;
            songInfo.dataset.songId = song.id;
            songInfo.style.cursor = 'pointer';
            songInfo.style.flexGrow = '1';
            songInfo.addEventListener('click', () => {
                // Cuando una canción de la lista es seleccionada, actualiza el índice de la canción actual
                currentPlayingSongIndex = allSongs.findIndex(s => s.id === song.id); // Encuentra el índice real de la canción seleccionada en `allSongs`
                displaySong(song);
                showScreen('nowPlaying');
            });

            const deleteButton = document.createElement('button');
            deleteButton.innerHTML = '<i class="fas fa-trash"></i>';
            deleteButton.classList.add('delete-song-button');
            deleteButton.style.marginLeft = '10px';
            deleteButton.style.backgroundColor = '#FF4444';
            deleteButton.style.color = 'white';
            deleteButton.style.border = 'none';
            deleteButton.style.padding = '5px 8px';
            deleteButton.style.cursor = 'pointer';
            deleteButton.style.borderRadius = '5px';
            deleteButton.style.fontSize = '1em';

            deleteButton.addEventListener('click', async (event) => {
                event.stopPropagation();
                if (confirm(`¿Estás seguro de que quieres eliminar "${song.title}"?`)) {
                    await deleteSongFromBackend(song.id); // Esta función ya maneja la recarga y actualización del UI
                }
            });

            listItem.style.display = 'flex';
            listItem.style.alignItems = 'center';
            listItem.style.justifyContent = 'space-between';

            listItem.appendChild(songInfo);
            listItem.appendChild(deleteButton);
            targetListElement.appendChild(listItem);
        });
    }

    async function loadSongsIntoLibrary() {
        const songs = await fetchAllSongs();
        renderSongList(songs, mp3LibraryList);
    }

    // --- NUEVAS FUNCIONES PARA CAMBIAR CANCIONES ---
    function playNextSong() {
        if (allSongs.length === 0) {
            console.log('No hay canciones para reproducir.');
            return;
        }
        currentPlayingSongIndex++;
        if (currentPlayingSongIndex >= allSongs.length) {
            currentPlayingSongIndex = 0; // Vuelve al principio si llega al final
        }
        displaySong(allSongs[currentPlayingSongIndex]);
        showScreen('nowPlaying'); // Asegúrate de que la pantalla de reproducción esté activa
    }

    function playPreviousSong() {
        if (allSongs.length === 0) {
            console.log('No hay canciones para reproducir.');
            return;
        }
        currentPlayingSongIndex--;
        if (currentPlayingSongIndex < 0) {
            currentPlayingSongIndex = allSongs.length - 1; // Vuelve al final si llega al principio
        }
        displaySong(allSongs[currentPlayingSongIndex]);
        showScreen('nowPlaying'); // Asegúrate de que la pantalla de reproducción esté activa
    }


    // --- Event Listeners ---

    menuButtonMP3.addEventListener('click', () => showScreen('library'));
    backToNowPlaying.addEventListener('click', () => showScreen('nowPlaying'));
    searchMenuButtonMP3.addEventListener('click', () => showScreen('search'));
    addSongMenuButtonMP3.addEventListener('click', () => showScreen('addSong'));
    closeAddModalMP3.addEventListener('click', () => addSongModalMP3.style.display = 'none');

    searchButtonMP3.addEventListener('click', async () => {
        const query = searchInputMP3.value.trim();
        if (query) {
            const results = await searchSongs(query);
            renderSongList(results, searchResultsList);
        } else {
            searchResultsList.innerHTML = '<li>Por favor, ingresa un término de búsqueda.</li>';
        }
    });

    backToLibraryFromSearch.addEventListener('click', () => {
        showScreen('library');
        searchInputMP3.value = '';
        searchResultsList.innerHTML = '';
    });

    addSongFormMP3.addEventListener('submit', async (event) => {
        event.preventDefault();

        const newSong = {
            title: document.getElementById('newTitleMP3').value,
            artist: document.getElementById('newArtistMP3').value,
            album: document.getElementById('newAlbumMP3').value,
            year: parseInt(document.getElementById('newYearMP3').value),
            duration: parseInt(document.getElementById('newDurationMP3').value)
        };

        const success = await addSongToBackend(newSong);
        if (success) {
            addSongFormMP3.reset();
            addSongModalMP3.style.display = 'none';
            showScreen('library');
        }
    });

    // NUEVOS EVENT LISTENERS PARA LOS BOTONES DE NAVEGACIÓN
    if (prevButtonMP3) {
        prevButtonMP3.addEventListener('click', playPreviousSong);
    }
    if (nextButtonMP3) {
        nextButtonMP3.addEventListener('click', playNextSong);
    }


    // Inicializar la aplicación al cargar
    showScreen('nowPlaying'); // Muestra la pantalla de "now playing" al inicio
    fetchAllSongs(); // Carga las canciones al inicio para tenerlas disponibles
});