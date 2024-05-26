document.addEventListener("DOMContentLoaded", function() {
    const appID = YOUR_APP_ID; // Replace with your actual App ID
    const serverSecret = "YOUR_SERVER_SECRET"; // Replace with your actual Server Secret
    const roomId = "demoRoom"; // Hardcoded room ID for demonstration
    const userName = "User" + Date.now(); // Simple unique username based on timestamp

    const chatContainer = document.getElementById('chat-messages');
    const chatInput = document.getElementById('chat-input');
    const sendButton = document.getElementById('send-button');

    const appendMessage = (message, isBot = false) => {
        const messageElem = document.createElement('div');
        messageElem.textContent = message;
        messageElem.className = isBot ? 'bot-message' : 'user-message';
        chatContainer.appendChild(messageElem);
        chatContainer.scrollTop = chatContainer.scrollHeight;
    };

    sendButton.addEventListener('click', () => {
        const message = chatInput.value.trim();
        if (message) {
            appendMessage(message);
            chatInput.value = '';
            // Simulate bot response
            setTimeout(() => {
                appendMessage("Bot response to: " + message, true);
            }, 1000);
        }
    });

    const kitToken = ZegoUIKitPrebuilt.generateKitTokenForTest(
        appID,
        serverSecret,
        roomId,
        Date.now().toString(),
        userName
    );

    const zp = ZegoUIKitPrebuilt.create(kitToken);
    zp.joinRoom({
        container: document.getElementById('video-container'),
        scenario: {
            mode: ZegoUIKitPrebuilt.VideoConference,
        },
    });
});
