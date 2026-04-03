from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

# -------- AGENT LOGIC -------- #
def run_agent(query: str):
    q = query.lower()

    if "plan" in q:
        return {
            "type": "plan",
            "message": "✅ Your day has been planned",
            "time": "09:00",
            "task": "Task planned"
        }

    elif "meeting" in q:
        return {
            "type": "meeting",
            "message": "📆 Meeting scheduled at 11:00 AM",
            "time": "11:00",
            "task": "Meeting scheduled"
        }

    elif "note" in q or "write" in q or "remember" in q:
        return {
            "type": "note",
            "message": "📝 Note saved",
            "content": query
        }

    else:
        return {
            "type": "unknown",
            "message": "🤖 Try: Plan my day / Schedule meeting / Take notes"
        }


# -------- HOME PAGE -------- #
@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>AI Productivity OS</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

<style>
:root {
    --bg: #020617;
    --card: rgba(15,23,42,0.7);
    --border: rgba(255,255,255,0.08);
    --accent: #3b82f6;
    --text: #e2e8f0;
    --muted: #94a3b8;
}

/* GLOBAL */
body {
    margin:0;
    font-family:'Inter',sans-serif;
    background: radial-gradient(circle at top, #0f172a, #020617);
    color:var(--text);
}

/* HEADER */
.header {
    height:60px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:0 20px;
    backdrop-filter: blur(12px);
    border-bottom:1px solid var(--border);
}

.status {
    font-size:0.8rem;
    color:#22c55e;
}

/* LAYOUT */
.app {
    display:grid;
    grid-template-columns: 2.5fr 1fr;
    height:calc(100vh - 60px);
}

/* CHAT */
.chat {
    display:flex;
    flex-direction:column;
}

#chat {
    flex:1;
    padding:20px;
    overflow-y:auto;
    display:flex;
    flex-direction:column;
    gap:12px;
}

/* BUBBLES */
.msg {
    padding:14px;
    border-radius:14px;
    max-width:70%;
    animation:fade 0.3s ease;
}

.user {
    align-self:flex-end;
    background:linear-gradient(135deg,#3b82f6,#2563eb);
}

.bot {
    align-self:flex-start;
    background:var(--card);
    border:1px solid var(--border);
}

/* INPUT */
.input {
    padding:15px;
    display:flex;
    gap:10px;
    border-top:1px solid var(--border);
}

input {
    flex:1;
    padding:14px;
    border-radius:12px;
    border:1px solid var(--border);
    background:rgba(2,6,23,0.8);
    color:white;
}

button {
    padding:12px 16px;
    border-radius:10px;
    border:none;
    background:var(--accent);
    color:white;
    cursor:pointer;
    transition:0.2s;
}

button:hover {
    transform:scale(1.05);
}

/* QUICK */
.quick {
    padding:15px;
    display:flex;
    gap:10px;
}

.quick button {
    background:rgba(59,130,246,0.1);
    border:1px solid rgba(59,130,246,0.3);
}

/* SIDE */
.side {
    padding:15px;
    display:flex;
    flex-direction:column;
    gap:15px;
}

/* CARD */
.card {
    background:var(--card);
    backdrop-filter: blur(12px);
    border-radius:14px;
    padding:15px;
    border:1px solid var(--border);
}

/* CALENDAR */
.slot {
    display:flex;
    justify-content:space-between;
    padding:8px;
    background:#1e293b;
    border-radius:8px;
    margin-bottom:6px;
}

/* NOTES */
.note {
    padding:8px;
    background:#1e293b;
    border-radius:8px;
    margin-bottom:6px;
}

/* AGENTS */
.node {
    padding:8px;
    border-radius:8px;
    background:#1e293b;
}

.active {
    background:var(--accent);
    animation:pulse 1s infinite;
}

/* DASHBOARD */
.stat {
    display:flex;
    justify-content:space-between;
}

/* ANIMATIONS */
@keyframes pulse {
    0%{opacity:1}
    50%{opacity:0.6}
    100%{opacity:1}
}

@keyframes fade {
    from{opacity:0;transform:translateY(10px)}
    to{opacity:1}
}
</style>
</head>

<body>

<div class="header">
    🚀 AI Productivity OS
    <div class="status">● Agents Active</div>
</div>

<div class="app">

<!-- CHAT -->
<div class="chat">

<div class="quick">
<button onclick="quick('Plan my day')">📅 Plan</button>
<button onclick="quick('Schedule a meeting')">📆 Meeting</button>
<button onclick="quick('Take notes buy groceries')">📝 Notes</button>
</div>

<div id="chat"></div>

<div class="input">
<input id="q" placeholder="Ask your AI assistant..." />
<button onclick="send()">Send</button>
</div>

</div>

<!-- SIDE -->
<div class="side">

<div class="card">
<h3>📊 Dashboard</h3>
<div class="stat">Tasks <span id="tasks">0</span></div>
<div class="stat">Meetings <span id="meetings">0</span></div>
<div class="stat">Notes <span id="notesCount">0</span></div>
</div>

<div class="card">
<h3>📅 Calendar</h3>
<div id="calendar"></div>
</div>

<div class="card">
<h3>📝 Notes</h3>
<div id="notes"></div>
</div>

<div class="card">
<h3>🤖 Agents</h3>
<div id="planner" class="node">Planner</div>
<div id="scheduler" class="node">Scheduler</div>
<div id="notesAgent" class="node">Notes</div>
</div>

</div>

</div>

<script>
let tasks=0, meetings=0, notes=0;

function addMsg(text,type){
    const d=document.createElement("div");
    d.className="msg "+type;
    d.innerText=text;
    document.getElementById("chat").appendChild(d);
}

function activate(id){
    ["planner","scheduler","notesAgent"].forEach(i=>{
        document.getElementById(i).classList.remove("active");
    });
    document.getElementById(id).classList.add("active");
}

function addCalendar(time,text){
    const d=document.createElement("div");
    d.className="slot";
    d.innerHTML="<span>"+time+"</span><span>"+text+"</span>";
    document.getElementById("calendar").appendChild(d);
}

function addNote(text){
    const d=document.createElement("div");
    d.className="note";
    d.innerText=text;
    document.getElementById("notes").appendChild(d);
}

function updateDashboard(){
    document.getElementById("tasks").innerText=tasks;
    document.getElementById("meetings").innerText=meetings;
    document.getElementById("notesCount").innerText=notes;
}

function quick(q){
    document.getElementById("q").value=q;
    send();
}

async function send(){
    const q=document.getElementById("q").value.trim();
    if(!q) return;

    addMsg(q,"user");

    // typing effect
    const typing=document.createElement("div");
    typing.className="msg bot";
    typing.innerText="...";
    document.getElementById("chat").appendChild(typing);

    const res = await fetch("/run", {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({query:q})
    });

    const data = await res.json();

    typing.remove();
    addMsg(data.message || "No response","bot");

    if(data.type==="plan"){
        activate("planner");
        tasks++;
        addCalendar(data.time,data.task);
    }

    if(data.type==="meeting"){
        activate("scheduler");
        meetings++;
        addCalendar(data.time,data.task);
    }

    if(data.type==="note"){
        activate("notesAgent");
        notes++;
        addNote(data.content);
    }

    updateDashboard();
    document.getElementById("q").value="";
}
</script>

</body>
</html>
"""

# -------- API -------- #
@app.post("/run")
async def run(request: Request):
    data = await request.json()
    query = data.get("query", "")

    return run_agent(query)
