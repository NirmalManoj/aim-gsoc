window.addEventListener('load', () => {
    const preloader = document.getElementById('preloader');
    preloader.style.display = 'none';
});

let changeBackgroundImage = clickedImage => {
    const mainSection = document.getElementById('main-section');
    const images = document.querySelectorAll('.images img');
    images.forEach(image => image.parentElement.classList.remove('active-image'));
    clickedImage.parentElement.classList.add('active-image');
    const imageSrc = clickedImage.src;
    mainSection.style.backgroundImage = `url(${imageSrc})`;
}

let changeBackgroundImageSeason = clickedImage => {
    const seasonsSection = document.getElementById('seasons-section');
    const images = document.querySelectorAll('.images img');
    images.forEach(image => image.parentElement.classList.remove('seasons-active-image'));
    clickedImage.parentElement.classList.add('seasons-active-image');
    const imageSrc = clickedImage.src;
    seasonsSection.style.backgroundImage = `url(${imageSrc})`;
}

let changeBackgroundImageSeries = clickedImage => {
    const tvSeriesSection = document.getElementById('tv-series-section');
    const images = document.querySelectorAll('.images img');
    images.forEach(image => image.parentElement.classList.remove('tv-series-active-image'));
    clickedImage.parentElement.classList.add('tv-series-active-image');
    const imageSrc = clickedImage.src;
    tvSeriesSection.style.backgroundImage = `url(${imageSrc})`;
}


window.onscroll = function () {
    $('.navbar-collapse').collapse('hide');
};
function sendMessage() {
    var messageInput = document.getElementById('message-input');
    var message = messageInput.value;

    var chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += '<div><strong>You:</strong> ' + message + '</div>';

    messageInput.value = '';
}
// Load the chat messages from local storage when the page is loaded
// Load the chat messages from local storage when the page is loaded
window.onload = function () {
    var savedMessages = localStorage.getItem('chatMessages');
    if (savedMessages) {
        document.getElementById('chat-box').innerHTML = savedMessages;
    }
};

function sendMessage() {
    var messageInput = document.getElementById('message-input');
    var message = messageInput.value;

    var chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += '<div style="text-align: right;"><strong>You:</strong> ' + message + '</div>';

    // Save the messages to local storage
    var currentMessages = chatBox.innerHTML;
    localStorage.setItem('chatMessages', currentMessages);

    messageInput.value = '';
}
//play btn
function playVideo() {
    var video = document.getElementById('myVideo');
    video.play();
}

function hideOverlay() {
    var overlay = document.getElementById('videoOverlay');
    overlay.style.display = 'none';
}

function showOverlay() {
    var overlay = document.getElementById('videoOverlay');
    overlay.style.display = 'flex';
}
const chatBox = document.getElementById('chatBox');
const messageInput = document.getElementById('messageInput');
const sendButton = document.getElementById('sendButton');

// Load messages from local storage
let messages = JSON.parse(localStorage.getItem('messages')) || [];

// Display messages from local storage
if (messages.length) {
    messages.forEach(message => {
        displayMessage(message);
    });
}

// Event listener for the send button
sendButton.addEventListener('click', function () {
    const message = messageInput.value;
    if (message) {
        messages.push(message);
        localStorage.setItem('messages', JSON.stringify(messages));
        displayMessage(message, true);
        messageInput.value = '';
    }
});

// Function to display messages
function displayMessage(message, isUser = false) {
    const p = document.createElement('p');
    p.textContent = message;
    const br = document.createElement("br");

    p.classList.add('userMessage');

    chatBox.appendChild(p);
    chatBox.appendChild(br);
}

function isMovieInPlaylist(movieData) {
    const playlist = localStorage.getItem('playlist');
    if (!playlist) return false;
    const storedPlaylist = JSON.parse(playlist);
    return storedPlaylist.includes(movieData);
}

function addToPlaylist(movieId) {
    const movieData = document.getElementById(movieId).innerHTML;
    if (isMovieInPlaylist(movieData)) {
        alert('This movie is already in your playlist.');
    } else {
        let playlist = localStorage.getItem('playlist');
        if (!playlist) {
            playlist = [];
        } else {
            playlist = JSON.parse(playlist);
        }
        playlist.push(movieData);
        localStorage.setItem('playlist', JSON.stringify(playlist));
        alert('Movie added to playlist.');
    }
}