# 🤖 AI Multi-Agent Productivity Assistant

## 🚀 Overview

This project is a **Multi-Agent AI System** designed to manage tasks, schedules, and notes through intelligent automation.
It uses a coordinated set of agents that collaborate to understand user intent and execute real-world workflows.

The system is deployed on the cloud and provides a **chat-based interface** for seamless user interaction.

---

## 🧠 Key Features

* 🤖 Multi-agent architecture (Orchestrator + Specialized Agents)
* 🧠 Intelligent task understanding
* 🔄 Multi-step workflow execution
* 🛠 Tool-based execution (MCP-style integration)
* 🗂 Cloud database integration (MongoDB Atlas)
* 💬 Chat-based user interface
* ⚡ Real-time responses
* ☁️ Deployed on Google Cloud Run
* 🔗 API-based and scalable system

---

## 🏗️ Architecture
```
User → FastAPI → Orchestrator Agent
        ↓
    Task | Calendar | Notes Agents
        ↓
      Tool Layer (MCP)
        ↓
    MongoDB Atlas (Cloud DB)
        ↓
    Google Cloud Run (Deployment)

---
```
## ⚙️ Tech Stack

* **Backend:** FastAPI (Python)
* **Database:** MongoDB Atlas
* **Deployment:** Google Cloud Run
* **Architecture:** Multi-Agent System
* **UI:** Chat-based frontend (HTML + JS)

---

## 🌐 Live Demo

👉 https://ai-agent-494571364009.asia-south1.run.app

---

## 🧪 Example Queries

* `create task finish project`
* `schedule meeting tomorrow`
* `save note important idea`
* `plan my day`

---

## 🔄 Workflow

1. User inputs query via chat UI
2. Orchestrator agent analyzes intent
3. Task is broken into steps
4. Relevant agents are invoked
5. Tools execute operations
6. Data is stored in database
7. Response is returned to user

---

## 🎯 Problem Solved

Modern productivity tools are fragmented and require manual effort.
This system provides a **unified AI assistant** that automates workflows and reduces cognitive load.

---

## 💡 Unique Selling Point (USP)

* Multi-agent coordination instead of single AI model
* Tool-based execution for real-world actions
* Scalable cloud deployment
* End-to-end automation of workflows

---

## 🚀 Future Improvements

* LLM-based decision making
* Voice interaction
* Chat history persistence (database-level)
* Integration with real calendar APIs
* Frontend dashboard

---

## 🏁 Conclusion

This project demonstrates how **multi-agent AI systems** can be used to automate real-world workflows by combining intelligent decision-making, tool execution, and scalable cloud infrastructure.

---

## 👨‍💻 Author

Developed as part of a hackathon project to demonstrate **Agentic AI + Generative AI systems**.
