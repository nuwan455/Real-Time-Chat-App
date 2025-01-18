# 📱 Real-Time Chat App

A simple and responsive real-time chat application built with **Flask** and **Socket.IO**. Users can join the chat by entering a username and send messages that are broadcasted to all connected users instantly.

---

## 🚀 Features

- 🔥 **Real-Time Messaging** using WebSockets with Socket.IO  
- 👤 **Username Identification** to differentiate users  
- 🌐 **Broadcast Messages** to all connected clients  
- 🎨 **Clean & Responsive UI** for seamless user experience  

---

## 🛠️ Tech Stack

- **Backend:** Flask, Flask-SocketIO  
- **Frontend:** HTML, CSS, JavaScript  
- **WebSocket:** Socket.IO  

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/nuwan455/Real-Time-Chat-App.git
cd Real-Time-Chat-App
```

### 2️⃣ Create and Activate a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install flask flask-socketio
```

###  ️4️⃣ Run the Application
```bash
python app.py
```

### 5️⃣ Open in Browser
Visit 👉 http://127.0.0.1:5000 in your browser.

### 📂 Project Structure

```bash
Real-Time-Chat-App/
├── app.py
├── templates/
│   └── index.html
├── venv/ (virtual environment)
└── README.md
```

### ✨ Usage
1. Enter your username and click Start Chat.
2. Type your message and press Send or hit Enter.
3. All connected users will see messages in real-time.

### ⚡ Troubleshooting
- <b>Port Conflict:</b> If port 5000 is already in use, run the app on a different port:
```bash
python app.py --port 5001
```
- <b>Socket.IO Version Compatibility:</b> Ensure the Socket.IO client and server versions are compatible.

### 🛠️ Customization
- <b>UI Styling:</b> Modify <code>index.html</code> for layout and styling.
- <b>Feature Expansion:</b> Add more features (e.g., private chat, user list) in <code>app.py</code>.