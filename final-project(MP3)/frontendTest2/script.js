// script.js

// --- 1. Implementación del Árbol AVL ---

/**
 * Clase para representar una canción con sus propiedades.
 */
class Song {
    constructor(id, title, artist, album, year, duration) {
        this.id = id; // Clave única para el árbol AVL
        this.title = title;
        this.artist = artist;
        this.album = album;
        this.year = year;
        this.duration = duration; // duración en segundos
    }
}

/**
 * Clase para representar un nodo en el árbol AVL.
 */
class AVLNode {
    constructor(song) {
        this.song = song;
        this.left = null;
        this.right = null;
        this.height = 1; // Altura del nodo, inicializada en 1 al crear un nuevo nodo
    }
}

/**
 * Implementación del Árbol de Búsqueda Binaria Auto-Balanceado (AVL).
 * Las operaciones de inserción y eliminación mantienen el árbol balanceado
 * para asegurar un rendimiento logarítmico O(log n) para la búsqueda, inserción y eliminación.
 * La clave de ordenación para este AVL es el 'id' de la canción.
 */
class AVLTree {
    constructor() {
        this.root = null;
        this.nextId = 1; // Para generar IDs únicos para nuevas canciones
    }

    /**
     * Calcula la altura de un nodo. Si el nodo es nulo, la altura es 0.
     * @param {AVLNode} node El nodo para el que se quiere calcular la altura.
     * @returns {number} La altura del nodo.
     */
    height(node) {
        if (!node) return 0;
        return node.height;
    }

    /**
     * Calcula el factor de balance de un nodo (altura del subárbol izquierdo - altura del subárbol derecho).
     * @param {AVLNode} node El nodo para el que se quiere calcular el factor de balance.
     * @returns {number} El factor de balance.
     */
    getBalance(node) {
        if (!node) return 0;
        return this.height(node.left) - this.height(node.right);
    }

    /**
     * Actualiza la altura de un nodo basándose en la altura de sus hijos.
     * @param {AVLNode} node El nodo cuya altura se quiere actualizar.
     */
    updateHeight(node) {
        node.height = 1 + Math.max(this.height(node.left), this.height(node.right));
    }

    /**
     * Realiza una rotación a la derecha en el subárbol con raíz 'y'.
     * Usada para casos de desequilibrio Izquierda-Izquierda (LL) o Izquierda-Derecha (LR).
     * @param {AVLNode} y La raíz del subárbol a rotar.
     * @returns {AVLNode} La nueva raíz del subárbol después de la rotación.
     */
    rightRotate(y) {
        const x = y.left;
        const T2 = x.right;

        // Realizar rotación
        x.right = y;
        y.left = T2;

        // Actualizar alturas de los nodos afectados
        this.updateHeight(y);
        this.updateHeight(x);

        return x; // Retorna la nueva raíz del subárbol rotado
    }

    /**
     * Realiza una rotación a la izquierda en el subárbol con raíz 'x'.
     * Usada para casos de desequilibrio Derecha-Derecha (RR) o Derecha-Izquierda (RL).
     * @param {AVLNode} x La raíz del subárbol a rotar.
     * @returns {AVLNode} La nueva raíz del subárbol después de la rotación.
     */
    leftRotate(x) {
        const y = x.right;
        const T2 = y.left;

        // Realizar rotación
        y.left = x;
        x.right = T2;

        // Actualizar alturas de los nodos afectados
        this.updateHeight(x);
        this.updateHeight(y);

        return y; // Retorna la nueva raíz del subárbol rotado
    }

    /**
     * Inserta una nueva canción en el árbol AVL.
     * Este método es recursivo y maneja el rebalanceo después de la inserción.
     * @param {AVLNode} node La raíz del subárbol actual.
     * @param {Song} song La canción a insertar.
     * @returns {AVLNode} La raíz actualizada del subárbol.
     */
    insert(node, song) {
        // 1. Realizar la inserción normal de un Árbol de Búsqueda Binaria (BST)
        if (!node) {
            return new AVLNode(song);
        }

        if (song.id < node.song.id) {
            node.left = this.insert(node.left, song);
        } else if (song.id > node.song.id) {
            node.right = this.insert(node.right, song);
        } else {
            // ID duplicado: en este ejemplo, no permitimos IDs duplicados.
            // Podrías lanzar un error o actualizar la canción existente si fuera el caso.
            console.warn(`Attempted to insert duplicate song ID: ${song.id}`);
            return node;
        }

        // 2. Actualizar la altura del nodo ancestro actual
        this.updateHeight(node);

        // 3. Obtener el factor de balance de este nodo
        const balance = this.getBalance(node);

        // 4. Si el nodo está desequilibrado (balance > 1 o balance < -1),
        //    realizar las rotaciones apropiadas para rebalancear el árbol.

        // Caso Izquierda-Izquierda (LL)
        if (balance > 1 && song.id < node.left.song.id) {
            return this.rightRotate(node);
        }

        // Caso Derecha-Derecha (RR)
        if (balance < -1 && song.id > node.right.song.id) {
            return this.leftRotate(node);
        }

        // Caso Izquierda-Derecha (LR)
        if (balance > 1 && song.id > node.left.song.id) {
            node.left = this.leftRotate(node.left); // Rotación izquierda en el hijo izquierdo
            return this.rightRotate(node);           // Rotación derecha en el nodo actual
        }

        // Caso Derecha-Izquierda (RL)
        if (balance < -1 && song.id < node.right.song.id) {
            node.right = this.rightRotate(node.right); // Rotación derecha en el hijo derecho
            return this.leftRotate(node);             // Rotación izquierda en el nodo actual
        }

        // Si el nodo ya está balanceado, retornar el nodo sin cambios
        return node;
    }

    /**
     * Agrega una nueva canción al árbol AVL.
     * Actualiza la raíz del árbol si es necesario.
     * @param {Song} song La canción a agregar.
     */
    addSong(song) {
        if (!song.id) {
            // Asignar un nuevo ID si la canción no tiene uno (ej. para canciones añadidas por el usuario)
            // Esto es importante para la clave del AVL
            song.id = this.nextId++;
        } else {
             // Si la canción ya tiene ID, asegurar que nextId sea mayor que cualquier ID existente
             if (song.id >= this.nextId) {
                this.nextId = song.id + 1;
             }
        }

        this.root = this.insert(this.root, song);
        console.log(`Canción añadida al AVL: ID:${song.id} - ${song.title}`);
        this.inOrderTraverse(); // Para depuración
    }

    /**
     * Busca una canción por su ID en el árbol AVL.
     * @param {AVLNode} node La raíz del subárbol actual para la búsqueda.
     * @param {number} id El ID de la canción a buscar.
     * @returns {Song | null} La canción si es encontrada, de lo contrario null.
     */
    search(node, id) {
        if (!node) {
            return null; // No encontrado
        }

        if (id === node.song.id) {
            return node.song; // Encontrado
        }

        if (id < node.song.id) {
            return this.search(node.left, id);
        } else {
            return this.search(node.right, id);
        }
    }

    /**
     * Método público para buscar una canción por su ID.
     * @param {number} id El ID de la canción a buscar.
     * @returns {Song | null} La canción si es encontrada, de lo contrario null.
     */
    findSongById(id) {
        return this.search(this.root, id);
    }

    /**
     * Encuentra el nodo con el valor mínimo (la canción con el ID más pequeño)
     * en un subárbol dado. Usado en la operación de eliminación.
     * @param {AVLNode} node La raíz del subárbol.
     * @returns {AVLNode} El nodo con el valor mínimo.
     */
    minValueNode(node) {
        let current = node;
        while (current.left !== null) {
            current = current.left;
        }
        return current;
    }

    /**
     * Elimina una canción del árbol AVL por su ID.
     * Este método es recursivo y maneja el rebalanceo después de la eliminación.
     * @param {AVLNode} root La raíz del subárbol actual.
     * @param {number} id El ID de la canción a eliminar.
     * @returns {AVLNode | null} La raíz actualizada del subárbol después de la eliminación.
     */
    deleteNode(root, id) {
        // 1. Realizar la eliminación normal de BST
        if (!root) {
            return root; // La canción no se encontró en el subárbol
        }

        // Navegar por el árbol para encontrar el nodo a eliminar
        if (id < root.song.id) {
            root.left = this.deleteNode(root.left, id);
        } else if (id > root.song.id) {
            root.right = this.deleteNode(root.right, id);
        } else {
            // Nodo con la canción a eliminar encontrado
            // Caso 1: Nodo con un hijo o sin hijos
            if (root.left === null || root.right === null) {
                const temp = root.left ? root.left : root.right;

                // No tiene hijos
                if (temp === null) {
                    return null; // El nodo es nulo después de la eliminación
                } else {
                    // Un hijo: reemplazar el nodo actual con su hijo
                    return temp;
                }
            } else {
                // Caso 2: Nodo con dos hijos: encontrar el sucesor in-order (el más pequeño en el subárbol derecho)
                const temp = this.minValueNode(root.right);

                // Copiar el contenido (canción) del sucesor in-order a este nodo
                root.song = temp.song;

                // Eliminar el sucesor in-order (ya que su contenido fue copiado)
                root.right = this.deleteNode(root.right, temp.song.id);
            }
        }

        // Si el árbol solo tenía un nodo, entonces retorna nulo
        if (root === null) {
            return root;
        }

        // 2. Actualizar la altura del nodo actual
        this.updateHeight(root);

        // 3. Obtener el factor de balance de este nodo (para verificar si está desequilibrado)
        const balance = this.getBalance(root);

        // 4. Si el nodo está desequilibrado, realizar las rotaciones apropiadas.

        // Caso Izquierda-Izquierda (LL)
        if (balance > 1 && this.getBalance(root.left) >= 0) {
            return this.rightRotate(root);
        }

        // Caso Izquierda-Derecha (LR)
        if (balance > 1 && this.getBalance(root.left) < 0) {
            root.left = this.leftRotate(root.left);
            return this.rightRotate(root);
        }

        // Caso Derecha-Derecha (RR)
        if (balance < -1 && this.getBalance(root.right) <= 0) {
            return this.leftRotate(root);
        }

        // Caso Derecha-Izquierda (RL)
        if (balance < -1 && this.getBalance(root.right) > 0) {
            root.right = this.rightRotate(root.right);
            return this.leftRotate(root);
        }

        return root; // Retorna el nodo (balanceado o después de rotación)
    }

    /**
     * Elimina una canción del árbol por su ID.
     * @param {number} id El ID de la canción a eliminar.
     * @returns {boolean} True si la canción fue eliminada, false si no se encontró.
     */
    removeSong(id) {
        const songToDelete = this.findSongById(id);
        if (songToDelete) {
            this.root = this.deleteNode(this.root, id);
            console.log(`Canción eliminada del AVL: ID:${id} - ${songToDelete.title}`);
            this.inOrderTraverse(); // Para depuración
            return true;
        }
        console.log(`Canción con ID ${id} no encontrada para eliminar.`);
        return false;
    }

    /**
     * Realiza un recorrido in-order del árbol para obtener todas las canciones ordenadas por ID.
     * @param {AVLNode} node El nodo actual en el recorrido.
     * @param {Array<Song>} arr El array donde se acumularán las canciones.
     */
    inOrder(node, arr) {
        if (node) {
            this.inOrder(node.left, arr);
            arr.push(node.song);
            this.inOrder(node.right, arr);
        }
    }

    /**
     * Obtiene todas las canciones del árbol en un array ordenado por ID.
     * @returns {Array<Song>} Un array de objetos Song.
     */
    getAllSongs() {
        const songs = [];
        this.inOrder(this.root, songs);
        return songs;
    }

    /**
     * Realiza un recorrido in-order para imprimir las canciones en la consola (para depuración).
     */
    inOrderTraverse() {
        const songs = this.getAllSongs();
        console.log("Árbol AVL (In-Order):", songs.map(s => `ID:${s.id} - ${s.title}`));
    }

    /**
     * Busca canciones por título o artista (no usa la estructura de árbol directamente
     * para la búsqueda por texto, sino que recorre todos los nodos).
     * @param {string} query La cadena de búsqueda.
     * @returns {Array<Song>} Un array de canciones que coinciden con la consulta.
     */
    searchByTitleOrArtist(query) {
        const results = [];
        const lowerCaseQuery = query.toLowerCase();

        function traverseAndSearch(node) {
            if (!node) return;

            // Comprobar si el título o el artista de la canción actual contienen la consulta
            if (node.song.title.toLowerCase().includes(lowerCaseQuery) ||
                node.song.artist.toLowerCase().includes(lowerCaseQuery)) {
                results.push(node.song);
            }

            // Continuar el recorrido en ambos subárboles
            traverseAndSearch(node.left);
            traverseAndSearch(node.right);
        }

        traverseAndSearch(this.root);
        return results;
    }
}

// --- 2. Instancia del Árbol AVL y Carga de Datos Iniciales ---
const musicLibrary = new AVLTree();

/**
 * Carga las canciones desde el archivo JSON y las inserta en el árbol AVL.
 */
async function loadSongs() {
    try {
        const response = await fetch('./data/songs.json');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const songsData = await response.json();
        songsData.forEach(s => {
            const song = new Song(s.id, s.title, s.artist, s.album, s.year, s.duration);
            musicLibrary.addSong(song);
        });
        console.log("Canciones cargadas en el AVL desde songs.json.");
        renderLibrarySongs(); // Renderizar las canciones iniciales en la interfaz
    } catch (error) {
        console.error("Error al cargar las canciones:", error);
        // Mostrar un mensaje al usuario si hay un error en la carga
        libraryGrid.innerHTML = '<p style="color: var(--text-color-dark); text-align: center;">Error al cargar las canciones. Asegúrate de que el archivo `songs.json` existe y estás ejecutando un servidor local.</p>';
    }
}


// --- 3. Referencias a Elementos del DOM ---

const exploreScreen = document.getElementById('exploreScreen');
const playerScreen = document.getElementById('playerScreen');
const playlistScreen = document.getElementById('playlistScreen');

const searchInput = document.getElementById('searchInput');
const searchButton = document.getElementById('searchButton');
const libraryGrid = document.getElementById('libraryGrid');
const searchResultsContainer = document.getElementById('searchResults');
const noResultsText = document.getElementById('noResultsText');
const addSongButton = document.getElementById('addSongButton');

const addSongModal = document.getElementById('addSongModal');
const closeModalButton = addSongModal.querySelector('.close-button');
const addSongForm = document.getElementById('addSongForm');

const playerSongTitle = document.getElementById('playerSongTitle');
const playerArtistAlbum = document.getElementById('playerArtistAlbum');
const playerAlbumArt = document.getElementById('playerAlbumArt');
const playerDuration = document.getElementById('playerDuration');
const playPauseButton = document.getElementById('playPauseButton');

const playlistTitle = document.getElementById('playlistTitle');
const playlistArtist = document.getElementById('playlistArtist');
const playlistAlbum = document.getElementById('playlistAlbum');
const playlistAlbumArt = document.getElementById('playlistAlbumArt');
const playlistTrackList = document.getElementById('playlistTrackList');
const playlistPlays = document.getElementById('playlistPlays');


// --- 4. Funciones Auxiliares de UI ---

/**
 * Formatea una duración en segundos a un string "MM:SS".
 * @param {number} seconds La duración en segundos.
 * @returns {string} La duración formateada.
 */
function formatDuration(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
}

/**
 * Genera un degradado de color aleatorio de una lista predefinida.
 * @returns {string} Una cadena de CSS para un degradado lineal.
 */
function getRandomGradient() {
    const gradients = [
        'linear-gradient(135deg, #ff7e00, #ff007e)', // Naranja a morado
        'linear-gradient(135deg, #f72c72, #e75c2e)', // Rosa a naranja
        'linear-gradient(135deg, #7c3aff, #ff3a81)', // Morado a rosa
        'linear-gradient(135deg, #ff9900, #ff0077)'  // Naranja a rojo
    ];
    return gradients[Math.floor(Math.random() * gradients.length)];
}

/**
 * Aplica el efecto de marquesina (texto desplazable) si el contenido de un elemento
 * excede su ancho visible.
 * @param {HTMLElement} element El elemento HTML que contiene el texto.
 */
function applyMarqueeEffect(element) {
    // Es crucial que el elemento ya esté en el DOM y se haya renderizado
    // para que scrollWidth y clientWidth tengan valores correctos.
    setTimeout(() => { // Pequeño retraso para asegurar que el DOM ha sido renderizado
        if (element.scrollWidth > element.clientWidth) {
            element.classList.add('marquee');
            // Ajustar la duración de la animación según la longitud del texto
            // (opcional, para que los textos más largos se muevan más rápido)
            const textLength = element.scrollWidth;
            const containerWidth = element.clientWidth;
            const animationDuration = (textLength / 50) + 3; // Ajusta 50 para la velocidad base y 3s para el "extra"
            element.style.animationDuration = `${animationDuration}s`;
        } else {
            element.classList.remove('marquee');
            element.style.animationDuration = ''; // Limpiar si no se necesita
        }
    }, 50); // Un pequeño retraso puede ser necesario para mediciones precisas
}


// --- 5. Funciones de Renderizado de Contenido ---

/**
 * Renderiza todas las canciones de la biblioteca en la cuadrícula principal.
 */
function renderLibrarySongs() {
    libraryGrid.innerHTML = ''; // Limpiar la cuadrícula antes de renderizar
    const allSongs = musicLibrary.getAllSongs(); // Obtener todas las canciones del AVL

    if (allSongs.length === 0) {
        libraryGrid.innerHTML = '<p style="color: var(--text-color-dark); text-align: center; width: 100%;">No hay canciones en la biblioteca. ¡Añade una!</p>';
        return;
    }

    allSongs.forEach(song => {
        const card = document.createElement('div');
        card.classList.add('music-card');
        card.dataset.songId = song.id; // Guarda el ID para fácil acceso

        card.innerHTML = `
            <div class="album-cover" style="background: ${getRandomGradient()};"></div>
            <p class="album-name" title="${song.title}">${song.title}</p>
            <p class="artist">${song.artist}</p>
            <button class="delete-button" data-id="${song.id}"><span class="fas fa-trash"></span></button>
        `;
        libraryGrid.appendChild(card);

        // Aplicar marquesina a los títulos de los álbumes
        const albumNameElement = card.querySelector('.album-name');
        applyMarqueeEffect(albumNameElement);

        // Eventos para ver detalles de la canción/álbum
        card.querySelector('.album-cover').addEventListener('click', () => showPlaylistScreen(song));
        card.querySelector('.album-name').addEventListener('click', () => showPlaylistScreen(song));
        card.querySelector('.artist').addEventListener('click', () => showPlaylistScreen(song));

        // Evento para eliminar canción
        card.querySelector('.delete-button').addEventListener('click', (event) => {
            event.stopPropagation(); // Evita que el clic se propague al card padre
            const songId = parseInt(event.currentTarget.dataset.id);
            if (confirm(`¿Estás seguro de que quieres eliminar "${song.title}" (ID: ${songId})?`)) {
                if (musicLibrary.removeSong(songId)) {
                    renderLibrarySongs(); // Volver a renderizar la lista principal
                    // Si hay una búsqueda activa, también actualizar los resultados
                    if (searchInput.value.trim() !== '') {
                        renderSearchResults(musicLibrary.searchByTitleOrArtist(searchInput.value));
                    }
                } else {
                    alert('No se pudo eliminar la canción. Asegúrate de que el ID es correcto.');
                }
            }
        });
    });
}

/**
 * Renderiza los resultados de búsqueda en el contenedor de resultados.
 * @param {Array<Song>} results Un array de canciones que coinciden con la búsqueda.
 */
function renderSearchResults(results) {
    searchResultsContainer.innerHTML = ''; // Limpiar resultados anteriores
    noResultsText.style.display = 'none'; // Ocultar el mensaje de "no resultados" inicial

    if (results.length === 0) {
        searchResultsContainer.innerHTML = '<p style="color: var(--text-color-dark); text-align: center;">No se encontraron resultados para tu búsqueda.</p>';
        return;
    }

    results.forEach(song => {
        const listItem = document.createElement('div');
        listItem.classList.add('list-item');
        listItem.dataset.songId = song.id;

        listItem.innerHTML = `
            <div class="album-cover small" style="background: ${getRandomGradient()};"></div>
            <div class="info">
                <p class="album-name" title="${song.title}">${song.title}</p>
                <p class="artist">${song.artist}</p>
            </div>
            <span class="icon fas fa-heart"></span>
            <button class="delete-button-small" data-id="${song.id}"><span class="fas fa-trash"></span></button>
        `;
        searchResultsContainer.appendChild(listItem);

        // Aplicar marquesina a los títulos de los álbumes en los resultados
        const albumNameElement = listItem.querySelector('.album-name');
        applyMarqueeEffect(albumNameElement);

        // Evento para mostrar la pantalla del reproductor al hacer clic en el elemento
        listItem.addEventListener('click', () => showPlayerScreen(song));

        // Evento para eliminar canción desde los resultados de búsqueda
        listItem.querySelector('.delete-button-small').addEventListener('click', (event) => {
            event.stopPropagation(); // Evita que el clic se propague al listItem padre
            const songId = parseInt(event.currentTarget.dataset.id);
            if (confirm(`¿Estás seguro de que quieres eliminar "${song.title}" (ID: ${songId})?`)) {
                if (musicLibrary.removeSong(songId)) {
                    renderLibrarySongs(); // Actualizar la biblioteca principal
                    renderSearchResults(musicLibrary.searchByTitleOrArtist(searchInput.value)); // Volver a renderizar los resultados de búsqueda
                } else {
                    alert('No se pudo eliminar la canción.');
                }
            }
        });
    });
}


// --- 6. Gestión de Pantallas (Navegación) ---

/**
 * Oculta todas las pantallas y muestra la pantalla especificada.
 * @param {string} screenId El ID de la pantalla a mostrar (ej. 'exploreScreen').
 */
function showScreen(screenId) {
    exploreScreen.style.display = 'none';
    playerScreen.style.display = 'none';
    playlistScreen.style.display = 'none';

    document.getElementById(screenId).style.display = 'flex'; // Las pantallas son flex containers
}

/**
 * Muestra la pantalla de exploración principal.
 */
function showExploreScreen() {
    showScreen('exploreScreen');
}

/**
 * Muestra la pantalla del reproductor con los detalles de una canción.
 * @param {Song} song La canción a mostrar en el reproductor.
 */
function showPlayerScreen(song) {
    if (!song) {
        alert('No se ha seleccionado ninguna canción para reproducir.');
        return;
    }
    playerSongTitle.textContent = song.title;
    playerArtistAlbum.textContent = `${song.artist} • ${song.album}`;
    playerDuration.textContent = formatDuration(song.duration);
    playerAlbumArt.style.background = getRandomGradient(); // Asigna un degradado aleatorio
    showScreen('playerScreen');
    console.log(`Reproduciendo: ${song.title}`);
    playPauseButton.classList.remove('fa-pause'); // Asegura que el botón de play esté visible al iniciar
    playPauseButton.classList.add('fa-play');
}

/**
 * Muestra la pantalla de la lista de reproducción/álbum con los detalles de un álbum
 * y sus canciones.
 * @param {Song} selectedSong La canción seleccionada que pertenece al álbum/playlist.
 */
function showPlaylistScreen(selectedSong) {
    if (!selectedSong) return;

    playlistTitle.textContent = selectedSong.album;
    playlistArtist.textContent = selectedSong.artist;
    // Podrías mostrar el título de la canción seleccionada aquí o simplemente el álbum
    playlistAlbum.textContent = `Álbum: ${selectedSong.album} (${selectedSong.year})`;
    playlistPlays.textContent = `${(Math.floor(Math.random() * 100) * 1000 + 420).toLocaleString()} Plays`; // Simular reproducciones grandes
    playlistAlbumArt.style.background = getRandomGradient();

    playlistTrackList.innerHTML = ''; // Limpiar lista anterior

    // Filtrar todas las canciones que pertenecen al mismo álbum y artista
    const albumSongs = musicLibrary.getAllSongs().filter(song =>
        song.artist === selectedSong.artist && song.album === selectedSong.album
    ).sort((a, b) => a.title.localeCompare(b.title)); // Ordenar por título para una lista coherente

    if (albumSongs.length === 0) {
        playlistTrackList.innerHTML = '<p style="color: var(--text-color-dark); text-align: center;">No hay canciones en este álbum.</p>';
    } else {
        albumSongs.forEach((song, index) => {
            const listItem = document.createElement('li');
            listItem.classList.add('track-item');
            listItem.dataset.songId = song.id;

            listItem.innerHTML = `
                <span class="track-number">${(index + 1).toString().padStart(2, '0')}</span>
                <div class="track-details">
                    <p class="track-name" title="${song.title}">${song.title}</p>
                    <p class="track-artist">${song.artist}</p>
                </div>
                ${song.title.toLowerCase().includes('explicit') ? '<span class="explicit-tag">explicit</span>' : ''}
                <span class="icon fas fa-heart"></span>
                <span class="icon fas fa-ellipsis-h"></span>
                <button class="delete-button-small" data-id="${song.id}"><span class="fas fa-trash"></span></button>
            `;
            playlistTrackList.appendChild(listItem);

            // Aplicar marquesina a los nombres de las canciones en la lista de reproducción
            const trackNameElement = listItem.querySelector('.track-name');
            applyMarqueeEffect(trackNameElement);

            // Evento para reproducir la canción al hacer clic en el elemento de la lista
            listItem.addEventListener('click', () => showPlayerScreen(song));

            // Evento para eliminar canción desde la lista de reproducción
            listItem.querySelector('.delete-button-small').addEventListener('click', (event) => {
                event.stopPropagation(); // Evita que el clic se propague al listItem padre
                const songId = parseInt(event.currentTarget.dataset.id);
                if (confirm(`¿Estás seguro de que quieres eliminar "${song.title}" (ID: ${songId})?`)) {
                    if (musicLibrary.removeSong(songId)) {
                        // Después de eliminar, volvemos a la pantalla principal y refrescamos todo
                        showExploreScreen();
                        renderLibrarySongs();
                        if (searchInput.value.trim() !== '') {
                            renderSearchResults(musicLibrary.searchByTitleOrArtist(searchInput.value));
                        }
                    } else {
                        alert('No se pudo eliminar la canción.');
                    }
                }
            });
        });
    }

    showScreen('playlistScreen');
}


// --- 7. Event Listeners Principales ---

// Event listener para el botón de búsqueda
searchButton.addEventListener('click', () => {
    const query = searchInput.value.trim();
    if (query) {
        const results = musicLibrary.searchByTitleOrArtist(query);
        renderSearchResults(results);
    } else {
        // Si la búsqueda está vacía, limpiar los resultados y mostrar el mensaje por defecto
        searchResultsContainer.innerHTML = '';
        noResultsText.style.display = 'block';
    }
});

// Event listener para la tecla Enter en el input de búsqueda
searchInput.addEventListener('keyup', (event) => {
    if (event.key === 'Enter') {
        searchButton.click(); // Simula un clic en el botón de búsqueda
    }
});

// Event listener para abrir el modal de añadir canción
addSongButton.addEventListener('click', () => {
    addSongModal.style.display = 'flex'; // Mostrar el modal
    document.getElementById('newId').value = musicLibrary.nextId; // Pre-rellenar con el siguiente ID disponible
    document.getElementById('newId').focus(); // Poner el foco en el campo ID
});

// Event listener para cerrar el modal de añadir canción (botón X)
closeModalButton.addEventListener('click', () => {
    addSongModal.style.display = 'none';
    addSongForm.reset(); // Limpiar el formulario al cerrar
});

// Event listener para cerrar el modal si se hace clic fuera de su contenido
window.addEventListener('click', (event) => {
    if (event.target === addSongModal) {
        addSongModal.style.display = 'none';
        addSongForm.reset();
    }
});

// Event listener para el envío del formulario de añadir canción
addSongForm.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevenir el envío por defecto del formulario

    const newId = parseInt(document.getElementById('newId').value);
    const newTitle = document.getElementById('newTitle').value.trim();
    const newArtist = document.getElementById('newArtist').value.trim();
    const newAlbum = document.getElementById('newAlbum').value.trim();
    const newYear = parseInt(document.getElementById('newYear').value);
    const newDuration = parseInt(document.getElementById('newDuration').value);

    // Validaciones básicas
    if (!newTitle || !newArtist || !newAlbum || isNaN(newYear) || isNaN(newDuration) || newYear < 1900 || newDuration <= 0) {
        alert('Por favor, completa todos los campos y asegúrate de que Año y Duración son números válidos.');
        return;
    }

    // Verificar si el ID ya existe antes de añadir
    if (musicLibrary.findSongById(newId)) {
        alert(`Ya existe una canción con el ID ${newId}. Por favor, usa un ID único.`);
        return;
    }

    const newSong = new Song(newId, newTitle, newArtist, newAlbum, newYear, newDuration);

    musicLibrary.addSong(newSong); // Añadir la canción al árbol AVL
    renderLibrarySongs(); // Actualizar la vista de la biblioteca principal
    addSongModal.style.display = 'none'; // Ocultar el modal
    addSongForm.reset(); // Limpiar el formulario
    alert(`"${newSong.title}" añadida correctamente a la biblioteca.`);
});

// Event listeners para los botones de "volver" en las pantallas secundarias
document.getElementById('backToExplore').addEventListener('click', showExploreScreen);
document.getElementById('backToExploreFromPlaylist').addEventListener('click', showExploreScreen);

// Event listener para el botón de Play/Pause en el reproductor (simulado)
playPauseButton.addEventListener('click', () => {
    if (playPauseButton.classList.contains('fa-play')) {
        playPauseButton.classList.remove('fa-play');
        playPauseButton.classList.add('fa-pause');
        console.log('Reproduciendo...');
    } else {
        playPauseButton.classList.remove('fa-pause');
        playPauseButton.classList.add('fa-play');
        console.log('Pausa.');
    }
});


// --- 8. Inicialización de la Aplicación ---

// Cargar las canciones desde el JSON y renderizar la interfaz cuando el DOM esté completamente cargado.
document.addEventListener('DOMContentLoaded', loadSongs);