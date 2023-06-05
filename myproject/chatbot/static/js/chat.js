// chat.js
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('user-input-form');
    const input = document.getElementById('user-input');
    const chatLog = document.getElementById('chat-log');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const message = input.value.trim();
        if (message !== '') {
            appendMessage('user', message);
            input.value = '';
            sendRequest(message);
        }
    });

    function appendMessage(sender, message) {
        const li = document.createElement('li');
        li.textContent = `${sender}: ${message}`;
        chatLog.appendChild(li);
    }

    function sendRequest(message) {
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/chat/', true);
        xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        xhr.onload = () => {
            if (xhr.status === 200) {
                const response = JSON.parse(xhr.responseText);
                appendMessage('chatbot', response.message);
            }
        };
        xhr.send(`message=${encodeURIComponent(message)}`);
    }
});
