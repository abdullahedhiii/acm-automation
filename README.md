# ACM Coders Cup Chatbot

A FastAPI-based chatbot powered by Google's Gemini API, designed to answer questions about ACM Coders Cup competitions, events, and modules.

## Features

- RESTful API built with FastAPI
- Powered by Google Gemini AI
- CORS enabled for easy frontend integration
- Conversation history support
- Health check endpoints
- Ready for deployment on multiple platforms

## Quick Start

### Prerequisites

- Python 3.11+
- Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))

### Installation

1. Clone or navigate to the project directory:
```bash
cd acm-chatbot
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
```

Edit `.env` and add your Gemini API key:
```
GEMINI_API_KEY=your_actual_api_key_here
PORT=8000
```

5. Run the server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Health Check

```bash
GET /
GET /health
```

Response:
```json
{
  "status": "online",
  "service": "ACM Coders Cup Chatbot",
  "version": "1.0.0"
}
```

### Simple Chat (Recommended for most use cases)

```bash
POST /chat/simple
Content-Type: application/json

{
  "message": "What is Coders Cup?"
}
```

Response:
```json
{
  "response": "Coders Cup is a batch-wise speed programming competition organized by ACM Tech Team..."
}
```

### Chat with History

```bash
POST /chat
Content-Type: application/json

{
  "message": "Tell me about the competitions",
  "conversation_history": [
    {
      "role": "user",
      "content": "Hi"
    },
    {
      "role": "assistant",
      "content": "Hello! How can I help you today?"
    }
  ]
}
```

Response:
```json
{
  "response": "ACM Coders Cup features several competitions...",
  "status": "success"
}
```

## Frontend Integration Example

### JavaScript/React Example

```javascript
async function sendMessage(userMessage) {
  const response = await fetch('https://your-deployment-url.com/chat/simple', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      message: userMessage
    })
  });

  const data = await response.json();
  return data.response;
}

// Usage
const botResponse = await sendMessage("What competitions are available?");
console.log(botResponse);
```

### HTML/Vanilla JS Example

```html
<!DOCTYPE html>
<html>
<head>
    <title>ACM Chatbot</title>
</head>
<body>
    <div id="chat-container">
        <div id="messages"></div>
        <input type="text" id="user-input" placeholder="Ask about ACM Coders Cup...">
        <button onclick="sendMessage()">Send</button>
    </div>

    <script>
        const API_URL = 'https://your-deployment-url.com/chat/simple';

        async function sendMessage() {
            const input = document.getElementById('user-input');
            const message = input.value;

            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message })
            });

            const data = await response.json();
            displayMessage('User', message);
            displayMessage('Bot', data.response);
            input.value = '';
        }

        function displayMessage(sender, text) {
            const messagesDiv = document.getElementById('messages');
            messagesDiv.innerHTML += `<p><strong>${sender}:</strong> ${text}</p>`;
        }
    </script>
</body>
</html>
```

## Deployment Options

### Option 1: Railway

1. Install Railway CLI:
```bash
npm i -g @railway/cli
```

2. Login and deploy:
```bash
railway login
railway init
railway add
```

3. Set environment variable in Railway dashboard:
   - `GEMINI_API_KEY`: Your Gemini API key

### Option 2: Render

1. Push your code to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com/)
3. Click "New +" → "Web Service"
4. Connect your repository
5. Render will auto-detect the `render.yaml` configuration
6. Add environment variable:
   - `GEMINI_API_KEY`: Your Gemini API key
7. Deploy

### Option 3: Vercel

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Deploy:
```bash
vercel
```

3. Add environment variable in Vercel dashboard:
   - `GEMINI_API_KEY`: Your Gemini API key

### Option 4: Docker

1. Build the image:
```bash
docker build -t acm-chatbot .
```

2. Run the container:
```bash
docker run -p 8000:8000 -e GEMINI_API_KEY=your_api_key acm-chatbot
```

### Option 5: Heroku

1. Create a `Procfile`:
```
web: python main.py
```

2. Deploy:
```bash
heroku create acm-chatbot
heroku config:set GEMINI_API_KEY=your_api_key
git push heroku main
```

## Testing the API

### Using cURL

```bash
# Health check
curl http://localhost:8000/health

# Simple chat
curl -X POST http://localhost:8000/chat/simple \
  -H "Content-Type: application/json" \
  -d '{"message": "What is Coders Cup?"}'
```

### Using Python

```python
import requests

response = requests.post(
    'http://localhost:8000/chat/simple',
    json={'message': 'Tell me about Speed Typing competition'}
)

print(response.json()['response'])
```

## Chatbot Knowledge Base

The chatbot is trained with information about:

- **Competitions**: Coders Cup, Speed Typing, Code Battle, Quiz, UI/UX, Hackathon, Query Quest, Data Dash, Speed Debugging
- **Module Heads**: Team leaders and organizers
- **DevDay Modules**: Prompt Engineering, Retarded Frenzy, Data Analytics
- **Website Pages**: Home, Coders Cup, Modules, About Us, Sponsors
- **Tech Operations**: Scoreboard, Tech Trivia, Registration System, Comic Game

## Customization

To update the chatbot's knowledge:

1. Edit the `load_context()` function in `main.py`
2. Update the system instruction text with new information
3. Restart the server

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Troubleshooting

### "Gemini API key not configured" error
- Make sure you've set the `GEMINI_API_KEY` environment variable
- Check that your `.env` file is in the project root
- Verify your API key is valid

### CORS errors
- The API allows all origins by default (`allow_origins=["*"]`)
- For production, update line 16 in `main.py` to specify your domain

### Port already in use
- Change the port in `.env` file
- Or specify a different port when running: `PORT=3000 python main.py`

## License

This project is created for ACM Coders Cup event.

## Support

For issues or questions, contact the ACM Tech Team.
