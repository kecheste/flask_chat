# Flask Group Chat Application

This is a simple group chat application built using Python's Flask framework. The application implements the Observer design pattern to manage and notify users in a chat room.

## Features

- Real-time group chat functionality.
- User notifications when someone joins or leaves the chat.
- UI built with basic HTML and CSS for a clean and user-friendly interface.
- Dockerized for easy deployment.

## Design Pattern: Observer

This application uses the Observer design pattern to manage the interactions between users in the chat room. The Observer pattern is a behavioral design pattern that defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

For more detailed information on the Observer pattern, you can visit [this resource](https://refactoring.guru/design-patterns/observer).

## How It Works

- **ChatRoom (Subject)**: The `ChatRoom` class maintains a list of clients (observers) and notifies them of any state changes (e.g., when a user joins or leaves the chat).
- **Client (Observer)**: The `Client` class represents a user in the chat room. When a user sends a message, the `ChatRoom` notifies all clients of the new message.
- Users are prompted to enter their name when they join the chat. If they leave the chat, all remaining users are notified.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Docker (optional, for containerized deployment)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kecheste/flask_chat.git
   cd flask-chat-app
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python app.py
   ```

5. Open your web browser and navigate to `http://127.0.0.1:5000` to access the chat application.

### Docker Deployment

1. Build the Docker image:

   ```bash
   docker build -t flask-chat .
   ```

   or

   ```bash
   docker pull kecheste/flask-chat:v1.0
   ```

2. Run the Docker container:

   ```bash
   docker run -d -p 5000:5000 flask-chat-app
   ```

3. Access the application at `http://localhost:5000`.

## File Structure

```plaintext
.
├── app.py               # Main application file
├── requirements.txt     # Python dependencies
├── Dockerfile           # Dockerfile for containerizing the app
├── .dockerignore        # Files and directories to ignore in Docker build
└── templates
    └── index.html       # HTML template for the chat interface
```
