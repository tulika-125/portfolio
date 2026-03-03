document.addEventListener('DOMContentLoaded', () => {
    const chatWidget = document.createElement('div');
    chatWidget.id = 'chat-widget';
    chatWidget.innerHTML = `
        <div id="chat-button">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>
        </div>
        <div id="chat-window" class="hidden">
            <div class="chat-header">
                <span>Ask about Tulika</span>
                <button id="close-chat">&times;</button>
            </div>
            <div id="chat-messages"></div>
            <div class="chat-input-area">
                <input type="text" id="chat-input" placeholder="Type a message...">
                <button id="send-chat">Send</button>
            </div>
        </div>
    `;
    document.body.appendChild(chatWidget);

    const chatButton = document.getElementById('chat-button');
    const chatWindow = document.getElementById('chat-window');
    const closeChat = document.getElementById('close-chat');
    const chatInput = document.getElementById('chat-input');
    const sendChat = document.getElementById('send-chat');
    const chatMessages = document.getElementById('chat-messages');

    // Toggle Chat Window
    chatButton.addEventListener('click', () => {
        chatWindow.classList.toggle('hidden');
        chatWidget.classList.toggle('active');
        if (!chatWindow.classList.contains('hidden')) {
            chatInput.focus();
        }
    });

    closeChat.addEventListener('click', () => {
        chatWindow.classList.add('hidden');
        chatWidget.classList.remove('active');
    });

    // Send Message
    async function sendMessage() {
        const message = chatInput.value.trim();
        if (!message) return;

        // Add User Message
        appendMessage('user', message);
        chatInput.value = '';

        // Add Loading Indicator
        const loadingId = appendMessage('bot', 'Thinking...');

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            });
            const data = await response.json();

            // Remove Loading Indicator and Add Bot Message
            removeMessage(loadingId);
            if (data.error) {
                appendMessage('bot', 'Error: ' + data.error);
            } else {
                appendMessage('bot', data.response);
            }
        } catch (error) {
            removeMessage(loadingId);
            appendMessage('bot', 'Error: Could not connect to server.');
        }
    }

    sendChat.addEventListener('click', sendMessage);
    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage();
    });

    function appendMessage(sender, text) {
        const msgDiv = document.createElement('div');
        msgDiv.classList.add('message', sender);
        msgDiv.id = 'msg-' + Date.now();
        msgDiv.textContent = text;
        chatMessages.appendChild(msgDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight;
        return msgDiv.id;
    }

    function removeMessage(id) {
        const msg = document.getElementById(id);
        if (msg) msg.remove();
    }

    // Video Modal Logic
    const videoModal = document.getElementById('video-modal');
    const projectVideo = document.getElementById('project-video');
    const projectVideoSource = projectVideo.querySelector('source');
    const closeModal = document.getElementById('close-modal');
    const projectItems = document.querySelectorAll('.clickable-project');

    projectItems.forEach(item => {
        item.addEventListener('click', () => {
            const videoPath = item.getAttribute('data-video');
            if (videoPath) {
                projectVideoSource.src = videoPath;
                projectVideo.load();
                videoModal.classList.remove('hidden');
                projectVideo.play();
            }
        });
    });

    closeModal.addEventListener('click', () => {
        videoModal.classList.add('hidden');
        projectVideo.pause();
    });

    window.addEventListener('click', (e) => {
        if (e.target === videoModal) {
            videoModal.classList.add('hidden');
            projectVideo.pause();
        }
    });
});
