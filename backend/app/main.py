from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.agents.orchestrator import run_agent

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Productivity Chat</title>
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                background: #0f172a;
                margin: 0;
                color: white;
            }

            h1 {
                text-align: center;
                padding: 20px;
            }

            .chat-container {
                max-width: 700px;
                margin: auto;
                height: 65vh;
                overflow-y: auto;
                padding: 20px;
                border-radius: 10px;
                background: #1e293b;
                box-shadow: 0 0 20px rgba(0,0,0,0.4);
            }

            .message {
                padding: 12px;
                margin: 10px 0;
                border-radius: 12px;
                max-width: 75%;
                animation: fadeIn 0.3s ease-in;
            }

            .user {
                background: #3b82f6;
                margin-left: auto;
                text-align: right;
            }

            .bot {
                background: #334155;
                margin-right: auto;
            }

            .input-box {
                display: flex;
                justify-content: center;
                padding: 15px;
                background: #0f172a;
            }

            input {
                width: 60%;
                padding: 12px;
                border-radius: 8px;
                border: none;
                font-size: 16px;
            }

            button {
                padding: 12px 20px;
                margin-left: 10px;
                border-radius: 8px;
                border: none;
                background: #22c55e;
                color: white;
                cursor: pointer;
            }

            button:hover {
                background: #16a34a;
            }

            .typing {
                font-style: italic;
                opacity: 0.7;
            }

            @keyframes fadeIn {
                from { opacity: 0; transform: translateY(5px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
    </head>
    <body>

        <h1>🤖 AI Productivity Chat</h1>

        <div class="chat-container" id="chat"></div>

        <div class="input-box">
            <input id="query" type="text" placeholder="Type your message..." />
            <button onclick="sendMessage()">Send</button>
        </div>

        <script>
            const chat = document.getElementById("chat");

            function addMessage(text, className) {
                const div = document.createElement("div");
                div.className = "message " + className;
                div.innerText = text;
                chat.appendChild(div);
                chat.scrollTop = chat.scrollHeight;
            }

            async function sendMessage() {
                const input = document.getElementById("query");
                const query = input.value.trim();

                if (!query) return;

                addMessage(query, "user");
                input.value = "";

                // Typing animation
                const typing = document.createElement("div");
                typing.className = "message bot typing";
                typing.innerText = "AI is typing...";
                chat.appendChild(typing);
                chat.scrollTop = chat.scrollHeight;

                try {
                    const response = await fetch("/run?query=" + encodeURIComponent(query), {
                        method: "POST"
                    });

                    const data = await response.json();

                    chat.removeChild(typing);
                    addMessage(data.response, "bot");

                } catch (error) {
                    chat.removeChild(typing);
                    addMessage("❌ Error connecting to server", "bot");
                }
            }

            // ENTER KEY SUPPORT
            document.getElementById("query").addEventListener("keypress", function(event) {
                if (event.key === "Enter") {
                    sendMessage();
                }
            });
        </script>

    </body>
    </html>
    """


@app.post("/run")
def run(query: str):
    result = run_agent(query)
    return {"response": result}
