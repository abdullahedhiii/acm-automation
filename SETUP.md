# ACM NUCES Karachi Chatbot - Setup Guide

## Quick Start (5 minutes)

### Step 1: Get Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy your API key

### Step 2: Set Up Environment

```bash
# Navigate to the project directory
cd acm-chatbot

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
```

### Step 3: Configure API Key

Edit the `.env` file and add your Gemini API key:

```
GEMINI_API_KEY=your_actual_gemini_api_key_here
PORT=8000
```

### Step 4: Run the Server

```bash
python main.py
```

You should see:
```
INFO:     Started server process
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 5: Test the Chatbot

1. Open `chat.html` in your web browser (just double-click the file)
2. Click "Test Connection" - you should see "✓ Connected"
3. Try asking: "What is Coders Cup?"
4. Try introducing yourself: "Hi, my name is Ahmed and I'm from batch 23"
5. Then ask: "What competitions should I join?" - it should remember your name!

## Features Explained

### 1. Conversation Memory

The chatbot remembers context within a session:

```javascript
// First message
User: "Hi, my name is Sarah"
Bot: "Hello Sarah! Nice to meet you..."

// Later in the conversation
User: "What should I join?"
Bot: "Sarah, based on your interests..." // Remembers your name!
```

### 2. Session Management

- Each chat session has a unique ID
- Sessions expire after 1 hour of inactivity
- Click "New Chat" to start fresh

### 3. API Endpoints

#### `/chat` - Chat with memory (recommended)
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What is Coders Cup?",
    "session_id": "optional-session-id"
  }'
```

Response:
```json
{
  "response": "Coders Cup is a competitive programming competition...",
  "session_id": "abc-123-def-456",
  "status": "success"
}
```

#### `/chat/simple` - One-off questions (no memory)
```bash
curl -X POST http://localhost:8000/chat/simple \
  -H "Content-Type: application/json" \
  -d '{"message": "What is ACM?"}'
```

#### `/session/new` - Create new session
```bash
curl -X POST http://localhost:8000/session/new
```

#### `/health` - Check server status
```bash
curl http://localhost:8000/health
```

## Integration with Your Website

### Simple Integration (HTML/JS)

```html
<script>
const API_URL = 'https://your-deployed-url.com';
let sessionId = null;

async function sendMessage(userMessage) {
  const response = await fetch(`${API_URL}/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      message: userMessage,
      session_id: sessionId
    })
  });

  const data = await response.json();
  sessionId = data.session_id; // Store for next message
  return data.response;
}
</script>
```

### React Integration

```jsx
import { useState } from 'react';

function ChatBot() {
  const [sessionId, setSessionId] = useState(null);

  async function sendMessage(message) {
    const response = await fetch('https://your-api.com/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message, session_id: sessionId })
    });

    const data = await response.json();
    setSessionId(data.session_id);
    return data.response;
  }

  // Your chat UI here
}
```

## Deployment

### Option 1: Render (Recommended - Free)

1. Push code to GitHub
2. Go to [render.com](https://render.com)
3. Click "New +" → "Web Service"
4. Connect your GitHub repo
5. Render auto-detects `render.yaml`
6. Add environment variable:
   - Key: `GEMINI_API_KEY`
   - Value: Your Gemini API key
7. Click "Create Web Service"

You'll get a URL like: `https://acm-chatbot.onrender.com`

### Option 2: Railway

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Add environment variable
railway variables set GEMINI_API_KEY=your_key_here

# Deploy
railway up
```

### Option 3: Docker

```bash
# Build image
docker build -t acm-chatbot .

# Run container
docker run -p 8000:8000 \
  -e GEMINI_API_KEY=your_key_here \
  acm-chatbot
```

## Testing Conversation Memory

Try this sequence to test memory:

1. **User**: "Hi, my name is Ahmed and I'm from batch 23"
   **Bot**: Should greet you by name

2. **User**: "What competitions are there?"
   **Bot**: Should list competitions

3. **User**: "Which one is best for me?"
   **Bot**: Should remember your name (Ahmed) and reference previous conversation

4. **User**: "When is it?"
   **Bot**: Should understand "it" refers to the competition discussed

## Troubleshooting

### "Gemini API key not configured"
- Check `.env` file exists
- Verify API key is correct
- Make sure you activated the virtual environment

### "Cannot connect to server"
- Check if server is running (`python main.py`)
- Verify port 8000 is not in use
- Check firewall settings

### Conversation doesn't remember context
- Make sure you're using `/chat` endpoint (not `/chat/simple`)
- Verify `session_id` is being sent with each request
- Check if session expired (1 hour timeout)

### CORS errors in browser
- Server allows all origins by default
- For production, update line 17 in `main.py` with your domain

## Customizing the Chatbot

### Update Knowledge Base

Edit `main.py`, find the `load_context()` function, and update the context:

```python
def load_context():
    return """
    Your custom context here...
    Add new events, dates, information, etc.
    """
```

### Change Session Timeout

In `main.py`, update line 172:

```python
if current_time - session['last_activity'] > timedelta(hours=2):  # Changed from 1 to 2
```

### Customize Appearance

Edit `chat.html` and modify the CSS variables:

```css
:root {
    --primary-color: #your-color;
    --bg-gradient-start: #your-color;
    --bg-gradient-end: #your-color;
}
```

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Production Checklist

- [ ] Update CORS settings in `main.py` with your domain
- [ ] Use a proper database (Redis) for session storage instead of in-memory
- [ ] Set up HTTPS for your deployment
- [ ] Add rate limiting to prevent abuse
- [ ] Set up monitoring and logging
- [ ] Add analytics to track usage
- [ ] Create backup of chat logs if needed

## Support

For issues or questions:
- Check the troubleshooting section above
- Review API documentation at `/docs`
- Contact ACM Tech Team

## What's Included

```
acm-chatbot/
├── main.py              # FastAPI backend with Gemini
├── chat.html            # Beautiful web interface
├── requirements.txt     # Python dependencies
├── .env.example        # Environment template
├── Dockerfile          # Docker deployment
├── render.yaml         # Render deployment
├── vercel.json         # Vercel deployment
├── README.md           # Full documentation
└── SETUP.md            # This file
```

## Next Steps

1. Test locally using `chat.html`
2. Customize the context for your needs
3. Deploy to Render or Railway
4. Integrate into your ACM website
5. Monitor usage and gather feedback
