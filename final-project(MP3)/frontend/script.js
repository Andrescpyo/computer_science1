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
                // Manejar errores HTTP (ej. 404, 500)
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Error al cargar las canciones');
            }
            const data = await response.json();
            allSongs = data; // Almacenar todas las canciones
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
                // Si no se encuentran canciones, FastAPI devuelve 404 con un mensaje específico
                if (response.status === 404 && errorData.detail === "No matching songs found.") {
                    return []; // Retorna un array vacío si no hay coincidencias
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
            // Recargar todas las canciones y la biblioteca después de añadir
            await fetchAllSongs();
            loadSongsIntoLibrary();
            return true;
        } catch (error) {
            console.error('Error adding song:', error);
            alert(`Error al añadir canción: ${error.message}`);
            return false;
        }
    }

    // --- NUEVA FUNCIÓN: Eliminar canción del backend ---
    async function deleteSongFromBackend(songId) {
        try {
            const response = await fetch(`${API_BASE_URL}/songs/delete/${songId}`, {
                method: 'DELETE' // Método HTTP DELETE
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Error al eliminar la canción');
            }

            const result = await response.json();
            alert(result.message); // Muestra el mensaje de éxito del backend

            // Recargar todas las canciones y la biblioteca después de eliminar
            await fetchAllSongs();
            loadSongsIntoLibrary();
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
        // Actualizar otros elementos de la UI como la duración y la barra de progreso si es necesario
        playerSongTitle.textContent = song.title;
        playerArtistAlbum.textContent = `${song.artist} - ${song.album} (${song.year})`;
        // Simular duración (aquí solo mostramos el total)
        const durationElement = document.getElementById('playerDuration');
        const minutes = Math.floor(song.duration / 60);
        const seconds = song.duration % 60;
        durationElement.textContent = `${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
    }

    // --- FUNCIÓN MODIFICADA: renderSongList para incluir el botón de eliminar ---
    function renderSongList(songs, targetListElement) {
        targetListElement.innerHTML = ''; // Limpiar lista
        if (songs.length === 0) {
            const noResultsItem = document.createElement('li');
            noResultsItem.textContent = "No hay canciones para mostrar.";
            targetListElement.appendChild(noResultsItem);
            return;
        }

        songs.forEach(song => {
            const listItem = document.createElement('li');
            listItem.classList.add('song-item'); // Añade una clase para posibles estilos

            // Contenedor para el título/artista y el botón
            const songInfo = document.createElement('span');
            songInfo.textContent = `${song.title} - ${song.artist}`;
            songInfo.dataset.songId = song.id; // Guarda el ID para reproducir
            songInfo.style.cursor = 'pointer'; // Para indicar que es clickeable
            songInfo.style.flexGrow = '1'; // Para que ocupe el espacio disponible
            songInfo.addEventListener('click', () => {
                // Lógica para reproducir la canción seleccionada
                console.log('Reproduciendo:', song.title);
                displaySong(song);
                showScreen('nowPlaying');
            });

            const deleteButton = document.createElement('button');
            deleteButton.innerHTML = '<i class="fas fa-trash"></i>';
            deleteButton.classList.add('delete-song-button'); // Añade una clase para estilos
            deleteButton.style.marginLeft = '10px'; // Espacio entre el texto y el botón
            deleteButton.style.backgroundColor = '#FF4444'; // Rojo para eliminar
            deleteButton.style.color = 'white';
            deleteButton.style.border = 'none';
            deleteButton.style.padding = '5px 8px'; // Adjust padding
            deleteButton.style.cursor = 'pointer';
            deleteButton.style.borderRadius = '5px';
            deleteButton.style.fontSize = '1em'; // Adjust icon size using font-size 
                                
            deleteButton.addEventListener('click', async (event) => {
                event.stopPropagation(); // Evita que el clic en el botón active también el evento de 'songInfo' (reproducir)
                if (confirm(`¿Estás seguro de que quieres eliminar "${song.title}"?`)) {
                    const success = await deleteSongFromBackend(song.id);
                    if (success) {
                        // La función deleteSongFromBackend ya recarga la lista, no se necesita hacer nada más aquí
                        console.log(`Canción ${song.title} eliminada con éxito.`);
                    }
                }
            });

            listItem.style.display = 'flex'; // Usar flexbox para alinear el texto y el botón
            listItem.style.alignItems = 'center'; // Alinear verticalmente
            listItem.style.justifyContent = 'space-between'; // Espacio entre elementos

            listItem.appendChild(songInfo);
            listItem.appendChild(deleteButton);
            targetListElement.appendChild(listItem);
        });
    }

    async function loadSongsIntoLibrary() {
        const songs = await fetchAllSongs();
        renderSongList(songs, mp3LibraryList);
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
        showScreen('library'); // Volver a la biblioteca después de la búsqueda
        searchInputMP3.value = ''; // Limpiar el campo de búsqueda
        searchResultsList.innerHTML = ''; // Limpiar resultados
    });

    addSongFormMP3.addEventListener('submit', async (event) => {
        event.preventDefault(); // Prevenir el envío del formulario por defecto

        const newSong = {
            title: document.getElementById('newTitleMP3').value,
            artist: document.getElementById('newArtistMP3').value,
            album: document.getElementById('newAlbumMP3').value,
            year: parseInt(document.getElementById('newYearMP3').value),
            duration: parseInt(document.getElementById('newDurationMP3').value)
        };

        const success = await addSongToBackend(newSong);
        if (success) {
            addSongFormMP3.reset(); // Limpiar formulario
            addSongModalMP3.style.display = 'none'; // Cerrar modal
            showScreen('library'); // Mostrar la biblioteca actualizada
        }
    });

    // Inicializar la aplicación al cargar
    showScreen('nowPlaying'); // Muestra la pantalla de "now playing" al inicio
    fetchAllSongs(); // Carga las canciones al inicio para tenerlas disponibles
});