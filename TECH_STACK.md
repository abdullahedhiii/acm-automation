# ACM NUCES Karachi Chatbot - Tech Stack

## Overview

This chatbot is built using modern, production-ready technologies for AI-powered conversational interfaces.

---

## Backend Stack

### 🐍 **Python 3.11+**
- **Purpose**: Primary programming language
- **Why**: Excellent AI/ML library support, fast development
- **Usage**: All backend logic and API endpoints

### ⚡ **FastAPI**
- **Version**: 0.109.0
- **Purpose**: Modern web framework for building APIs
- **Why**:
  - Async/await support for high performance
  - Automatic API documentation (Swagger/ReDoc)
  - Type hints and validation with Pydantic
  - Fast and lightweight
- **Usage**: REST API endpoints, request handling, CORS management

### 🤖 **Google Gemini API**
- **Model**: gemini-2.5-flash
- **Library**: google-generativeai (v0.3.2)
- **Purpose**: AI language model for conversations
- **Why**:
  - Fast response times (1-3 seconds)
  - High-quality conversational AI
  - Free tier available
  - Good context understanding
- **Usage**: Processing user messages, generating responses

### 📦 **Pydantic**
- **Version**: 2.5.3
- **Purpose**: Data validation and settings management
- **Why**: Type-safe request/response models
- **Usage**: API request/response schemas

### 🔧 **python-dotenv**
- **Version**: 1.0.0
- **Purpose**: Environment variable management
- **Why**: Secure API key storage
- **Usage**: Loading `.env` configuration

### 🚀 **Uvicorn**
- **Version**: 0.27.0 (with standard extras)
- **Purpose**: ASGI server
- **Why**: High-performance async server for FastAPI
- **Usage**: Running the FastAPI application

---

## Frontend Stack

### 🌐 **HTML5**
- **Purpose**: Structure of the chat interface
- **Why**: Standard, widely supported
- **Files**: `chat.html`, `test_client.html`

### 🎨 **CSS3**
- **Purpose**: Styling and responsive design
- **Features**:
  - CSS Grid and Flexbox for layout
  - CSS animations for smooth interactions
  - Custom properties (CSS variables) for theming
  - Media queries for mobile responsiveness
- **Why**: No framework needed, lightweight, fast loading

### ⚙️ **Vanilla JavaScript (ES6+)**
- **Purpose**: Client-side logic and API communication
- **Features**:
  - Async/await for API calls
  - Fetch API for HTTP requests
  - DOM manipulation
  - Session management
- **Why**:
  - No dependencies or build step needed
  - Fast loading time
  - Works in any modern browser

---

## Architecture

### **Session-Based Memory**
- **Storage**: In-memory dictionary (Python dict)
- **Structure**: UUID-based session IDs
- **Expiry**: 1-hour automatic cleanup
- **Scalability**: Can be upgraded to Redis for production

### **RESTful API Design**
- **Endpoints**:
  - `POST /chat` - Chat with memory
  - `POST /chat/simple` - One-off questions
  - `GET /health` - Health check
  - `POST /session/new` - Create session
  - `DELETE /session/{id}` - Delete session
- **Format**: JSON request/response
- **CORS**: Enabled for cross-origin requests

---

## Deployment Options

### **Docker**
- **File**: `Dockerfile`
- **Base Image**: python:3.11-slim
- **Why**: Containerized, consistent across environments

### **Platform Support**
1. **Render** (render.yaml)
   - Free tier available
   - Auto-deploys from GitHub
   - Managed infrastructure

2. **Railway**
   - Fast deployment
   - Good free tier
   - Simple CLI

3. **Vercel** (vercel.json)
   - Serverless deployment
   - Edge network
   - GitHub integration

4. **Heroku**
   - Classic PaaS
   - Easy scaling
   - Add-ons ecosystem

---

## Development Tools

### **Virtual Environment**
- **Tool**: Python venv
- **Purpose**: Isolated dependency management
- **Usage**: Keeps project dependencies separate

### **Version Control**
- **Tool**: Git
- **Files**: `.gitignore` configured for Python projects
- **Purpose**: Source code management

---

## Complete Dependencies

```python
# Backend (requirements.txt)
fastapi==0.109.0           # Web framework
uvicorn[standard]==0.27.0  # ASGI server
google-generativeai==0.3.2 # Gemini AI
pydantic==2.5.3            # Data validation
python-dotenv==1.0.0       # Environment config
```

```html
<!-- Frontend (no dependencies!) -->
- Pure HTML5
- Pure CSS3
- Vanilla JavaScript ES6+
```

---

## Key Features Implementation

### 1. **Conversation Memory**
- **Tech**: Python dict with UUID keys
- **Structure**: Stores Gemini chat objects per session
- **Cleanup**: Datetime-based expiry check

### 2. **AI Integration**
- **Provider**: Google Gemini API
- **Model**: gemini-2.5-flash
- **Context**: System instruction with ACM knowledge base
- **Method**: Chat session with history tracking

### 3. **CORS Support**
- **Library**: FastAPI CORS middleware
- **Config**: Allow all origins (configurable for production)
- **Purpose**: Enable frontend integration from any domain

### 4. **Request Validation**
- **Library**: Pydantic models
- **Features**: Type checking, required fields, defaults
- **Benefit**: Automatic error handling

### 5. **API Documentation**
- **Auto-generated**: Swagger UI at `/docs`
- **Auto-generated**: ReDoc at `/redoc`
- **Format**: OpenAPI (Swagger) specification

---

## Architecture Diagram

```
┌─────────────┐
│   Browser   │
│ (HTML/CSS/JS)│
└──────┬──────┘
       │ HTTP/JSON
       ▼
┌─────────────────┐
│   FastAPI       │
│   + Uvicorn     │
│                 │
│  - CORS         │
│  - Validation   │
│  - Routing      │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
┌────────┐ ┌──────────┐
│Session │ │ Gemini   │
│Manager │ │   API    │
│(Memory)│ │          │
└────────┘ └──────────┘
```

---

## Performance Characteristics

### **Response Time**
- Average: 1-3 seconds
- Depends on: Gemini API response time
- Network latency: Minimal (async processing)

### **Scalability**
- **Current**: Single-server, in-memory sessions
- **Production**: Can add Redis for session storage
- **Horizontal**: FastAPI supports load balancing

### **Memory Usage**
- Base: ~50MB (Python + FastAPI)
- Per session: ~1-2MB (chat history)
- Cleanup: Automatic after 1 hour

---

## Security Features

### **Environment Variables**
- API keys stored in `.env` (not in code)
- `.gitignore` prevents committing secrets

### **CORS**
- Configurable allowed origins
- Default: Allow all (development)
- Production: Restrict to your domain

### **Input Validation**
- Pydantic models validate all inputs
- Type checking on all endpoints
- Automatic error responses for invalid data

### **Topic Guardrails**
- AI prompt restricts to ACM topics only
- Refuses off-topic questions
- Prevents misuse

---

## Why This Stack?

### ✅ **Fast Development**
- Python: Quick prototyping
- FastAPI: Auto-documentation
- Vanilla JS: No build step

### ✅ **Production Ready**
- FastAPI: Battle-tested framework
- Gemini: Enterprise-grade AI
- Docker: Deployment flexibility

### ✅ **Cost Effective**
- Free tier: Gemini API
- Free hosting: Render, Railway
- No paid dependencies

### ✅ **Easy to Maintain**
- Simple architecture
- Clear separation of concerns
- Comprehensive documentation

### ✅ **Scalable**
- Async support (FastAPI)
- Can add Redis, PostgreSQL
- Container-ready (Docker)

---

## Alternative Stacks Considered

| Component | Chosen | Alternatives | Why Chosen |
|-----------|--------|--------------|------------|
| Backend Framework | FastAPI | Flask, Django | Async, auto-docs, modern |
| AI Model | Gemini | OpenAI GPT, Claude | Free tier, fast |
| Frontend | Vanilla JS | React, Vue | No build step, lightweight |
| Server | Uvicorn | Gunicorn | ASGI support, async |
| Deployment | Docker | Direct | Portability, consistency |

---

## Future Enhancements

### Potential Upgrades:
1. **Redis** - For production session storage
2. **PostgreSQL** - Store conversation history
3. **WebSockets** - Real-time streaming responses
4. **React** - More complex UI features
5. **Rate Limiting** - Prevent API abuse
6. **Analytics** - Track usage patterns
7. **Caching** - Reduce API calls

---

## Getting Started

### Install Dependencies:
```bash
pip install -r requirements.txt
```

### Run Server:
```bash
python main.py
```

### Access:
- API: http://localhost:8000
- Docs: http://localhost:8000/docs
- Chat UI: Open `chat.html` in browser

---

## License & Credits

**Built for**: ACM NUCES Karachi
**Purpose**: Student assistance chatbot
**AI Provider**: Google Gemini
**Framework**: FastAPI
**Language**: Python 3.11+

---

**Questions?** Check the other documentation files:
- `QUICKSTART.md` - Quick setup
- `SETUP.md` - Detailed guide
- `README.md` - Full documentation
- `FINAL_STATUS.md` - Current status
