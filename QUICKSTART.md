# Quick Start - 3 Steps to Get Running

## Step 1: Install Dependencies (2 minutes)

```bash
cd acm-chatbot
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Step 2: Add Your API Key (1 minute)

1. Get API key: https://makersuite.google.com/app/apikey
2. Create `.env` file:

```bash
cp .env.example .env
```

3. Edit `.env` and add your key:

```
GEMINI_API_KEY=your_actual_key_here
PORT=8000
```

## Step 3: Run & Test (1 minute)

```bash
# Start the server
python main.py
```

Then open `chat.html` in your browser!

---

## Quick Test Commands

```bash
# Test if server is running
curl http://localhost:8000/health

# Test a simple question
curl -X POST http://localhost:8000/chat/simple \
  -H "Content-Type: application/json" \
  -d '{"message": "What is Coders Cup?"}'
```

## For Deployment

**Easiest: Render (Free)**
1. Push to GitHub
2. Go to render.com → New Web Service
3. Connect repo
4. Add `GEMINI_API_KEY` environment variable
5. Deploy!

**Quick Deploy: Railway**
```bash
npm i -g @railway/cli
railway login
railway init
railway variables set GEMINI_API_KEY=your_key
railway up
```

## Files You Need

- `main.py` - The backend API
- `chat.html` - The web interface (for testing)
- `.env` - Your API key (create this)

## Key Features

✓ Conversation memory - remembers what you said
✓ Session management - maintains context
✓ Beautiful UI - modern chat interface
✓ Student-friendly - talks like a human
✓ ACM-specific - knows all about NUCES events

## API Endpoint for Your Website

```javascript
const response = await fetch('YOUR_DEPLOYMENT_URL/chat', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    message: userQuestion,
    session_id: sessionId  // for conversation memory
  })
});
const data = await response.json();
// Use: data.response and data.session_id
```

## Troubleshooting

**"Can't connect"** → Server not running? Run `python main.py`
**"API key error"** → Check `.env` file exists with valid key
**"No memory"** → Use `/chat` endpoint with `session_id`

## Full Documentation

- `SETUP.md` - Detailed setup guide
- `README.md` - Complete documentation
- `/docs` - API documentation (when server is running)

---

**Need help?** Check SETUP.md or contact ACM Tech Team
