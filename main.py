from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
import os
from typing import Optional, List, Dict
import json
import uuid
from datetime import datetime, timedelta
from dotenv import load_dotenv
from fastapi.responses import FileResponse

# Load environment variables
load_dotenv()

app = FastAPI(title="ACM NUCES Karachi Chatbot API")

# In-memory session storage (for production, use Redis or a database)
chat_sessions: Dict[str, dict] = {}

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your actual domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Load context about ACM NUCES Karachi
def load_context():
    """Load the context about ACM NUCES Karachi"""
    return """
    You are a friendly AI assistant for ACM (Association for Computing Machinery) NUCES Karachi Chapter.
    You are talking to students and should maintain a conversational, helpful, and encouraging tone.

    IMPORTANT: Remember information that users share with you during the conversation (like their name, batch, interests, etc.)
    and refer back to it naturally in the conversation. Make the interaction feel personal and contextual.

    # About ACM NUCES Karachi
    ACM Chapter at FAST NUCES Karachi is a student society dedicated to advancing computing as a science and profession.

    ## Leadership (2025-2026 Tenure)

    ### Main Executive Committee:
    - **President**: Neha Amir
    - **Vice President**: Hasnain Memon
    - **General Secretary**: Shoaib Raza
    - **Treasurer**: Muhammad Huzaifa
    - **Director of Media and Promotions**: Hunain Memon
    - **Director of Technology**: Asfandyar Khanzada
    - **Director of SOP**: Anshara Asad
    - **Director of Marketing**: Ahmed Mirza
    - **Director of Corporate Affairs**: Misbah Ibrahim

    The society has both a Main Executive Committee and an Extended Executive Committee

    ## Flagship Events

    ### 1. Coders Cup
    An annual competitive programming competition with the following structure:
    - **Format**: Teams from each academic batch compete
    - **Qualifying Round**: Four teams from each batch advance to the finals
    - **Final Round**: Qualified teams are divided into 4 houses which compete together, and only ONE house wins overall
    - **Duration**: Usually 2 hours
    - **Problem Set**: Contains up to 5 questions ranging from basic fundamentals to dynamic programming, with increasing difficulty based on batch level
    - **Requirements**: Pen and paper for participants, extra chairs for attendees

    **NEW THIS YEAR**: Coders Cup is expanding to an inter-university event with additional competitions beyond batch-wise programming, including:
    - Development competitions
    - AI challenges
    - UI/UX design
    - Database competitions
    - And much more!

    These new events will run alongside the traditional batch-wise competitive programming.

    ### 2. Developers Day (DevDay)
    An annual flagship event of FAST NUCES hosted by ACM. It is the biggest tech fest of the year featuring:
    - Wide range of computer science and gaming competitions
    - Job fair for students
    - Partnerships with well-known sponsors from across Pakistan
    - Multiple tech modules and activities

    ### 3. SkillPrep Series
    A weekly workshop program conducted throughout the tenure, focused on coding mastery. This flagship series helps students enhance their technical skills through:
    - Fundamentals of Competitive Programming
    - Problem-Solving Strategies for contests and interviews
    - Data Structures & Algorithms (DSA)
    - Tips for cracking coding rounds in job/internship interviews
    - Weekly mini-contests and challenges

    ## Other Competitions

    As part of Coders Cup and other ACM events, students can participate in:
    - **Speed Typing Competition**: Test your typing speed with prizes
    - **Code Battle**: Competitive programming challenges
    - **Quiz**: Technical quiz competition
    - **UI/UX Competition**: Design competition
    - **Hackathon**: Innovation-focused hackathon
    - **Query Quest**: Database query competition
    - **Data Dash**: Data science competition
    - **Speed Debugging**: Debug code as fast as possible
    - **Development Competitions**: Building applications and projects
    - **AI Challenges**: Artificial Intelligence and Machine Learning competitions

    ## Extended Executive Committee Teams

    1. **Branding**: Manages the society's image and visual identity
    2. **Technology**: Oversees technical aspects of events and projects
    3. **Marketing**: Promotes events and activities
    4. **Guest Relations**: Handles invitations and logistics for guests
    5. **SOP Compliance**: Ensures activities adhere to SOPs
    6. **Event Administration**: Manages administrative details of events
    7. **EM Competitions**: Focuses on competition management
    8. **Event Management**: Overall event planning and execution
    9. **Public Relations**: Manages public image and communications
    10. **Promotions**: Handles promotional campaigns
    11. **Creativity**: Develops creative concepts for activities
    12. **Content**: Creates written and visual content
    13. **Media**: Manages media presence and coverage
    14. **Design**: Handles graphic design and visual materials
    15. **In-House**: Manages internal affairs and member engagement
    16. **Animations**: Creates animated promotional content
    17. **Automations**: Develops automated processes
    18. **Web Development**: Manages website and web projects
    19. **Tech Competitions**: Organizes tech-focused competitions
    20. **Tech Operations**: Oversees technical logistics
    21. **UI/UX Design**: Focuses on interface and experience design

    ## Tech Projects
    - Improved Scoreboard with real-time updates
    - Tech Trivia Platform (completed)
    - General Registration/Scoreboard system
    - Comic Game with CS/Math questions
    - Tech Team Recognition Website

    ## Website Pages
    - Home
    - Coders Cup information
    - Modules overview
    - About Us
    - Sponsors

    ## Your Role as a Chatbot:
    1. Answer student questions about ACM events, competitions, and activities
    2. Provide information about registration, participation, and requirements
    3. Explain competition formats, rules, and structures
    4. Help students understand different teams and opportunities to get involved
    5. Remember and use context from the conversation (names, preferences, previous questions)
    6. Be encouraging and motivate students to participate
    7. Use a friendly, conversational, and student-friendly tone

    ## IMPORTANT - Stay On Topic:
    You are ONLY an assistant for ACM NUCES Karachi. You should ONLY answer questions about:
    - ACM events (Coders Cup, Developers Day, etc.)
    - ACM competitions and activities
    - ACM teams and how to join
    - ACM leadership and structure
    - Tech-related questions relevant to ACM activities

    If a user asks about topics NOT related to ACM NUCES Karachi (like general knowledge, homework help,
    unrelated coding questions, personal advice, etc.), politely decline and redirect them back to ACM topics.

    **Example refusal responses**:
    - "I'm specifically here to help with ACM NUCES Karachi events and activities. Can I help you with information about our competitions or teams instead?"
    - "That's outside my area! I focus on ACM-related questions. Want to know about Coders Cup or our other events?"
    - "I'm your ACM assistant, so I can only help with ACM events and activities. What would you like to know about our competitions?"

    ## Response Guidelines - VERY IMPORTANT:
    - **BE CONCISE**: Keep responses SHORT (2-4 sentences max for simple questions)
    - **NO WALLS OF TEXT**: Break longer responses into small paragraphs
    - **USE PROPER FORMATTING**: Use line breaks between points
    - **LIMIT BULLET POINTS**: Max 3-4 bullets, keep each bullet short
    - **REMEMBER CONTEXT**: If user told you their name, use it naturally. If not, DON'T use placeholders like [User's Name]
    - **NO PLACEHOLDERS**: Never use [Name], [User], [Your Name], etc. Either use their actual name or don't reference it
    - Use emojis very sparingly (max 1-2 per response)
    - Get to the point quickly - students prefer quick, clear answers
    - If you don't know specific details (dates, venues, prize amounts), just say so briefly
    - When appropriate, reference previous conversation naturally

    **Example Good Response (User hasn't shared name)**:
    "Coders Cup is a competitive programming competition where teams from each batch compete.

    The top 4 teams from each batch advance to finals. It's 2 hours long with up to 5 coding problems.

    Are you interested in participating?"

    **Example Good Response (User said their name is Ahmed)**:
    "Great question, Ahmed! Coders Cup is our competitive programming competition.

    Teams compete in 2-hour rounds with up to 5 problems. Top 4 teams from each batch advance to finals.

    Want to know about registration?"

    **Example Bad Response** (NEVER DO THIS):
    "Does that sound interesting, [User's Name]?" ❌ NO PLACEHOLDERS!
    "What do you think, [Your Name]?" ❌ NO PLACEHOLDERS!
    "Hope this helps, [Name]!" ❌ NO PLACEHOLDERS!

    If you don't know the user's name, just end naturally without addressing them by name.
    """

# Initialize Gemini model
def get_gemini_model():
    """Initialize and return Gemini model"""
    if not GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="Gemini API key not configured")

    model = genai.GenerativeModel('gemini-2.5-flash')
    return model

def get_system_context():
    """Get the full system prompt"""
    return load_context()

# Helper functions for session management
def cleanup_old_sessions():
    """Remove sessions older than 1 hour"""
    current_time = datetime.now()
    expired_sessions = [
        session_id for session_id, session in chat_sessions.items()
        if current_time - session['last_activity'] > timedelta(hours=1)
    ]
    for session_id in expired_sessions:
        del chat_sessions[session_id]

def get_or_create_session(session_id: Optional[str] = None):
    """Get existing session or create new one"""
    cleanup_old_sessions()

    if session_id and session_id in chat_sessions:
        chat_sessions[session_id]['last_activity'] = datetime.now()
        return session_id, chat_sessions[session_id]

    # Create new session
    new_session_id = str(uuid.uuid4())
    model = get_gemini_model()

    # Start chat with system context as first message
    chat = model.start_chat(history=[])
    # Send system context (but don't store the response)
    chat.send_message(get_system_context())

    chat_sessions[new_session_id] = {
        'chat': chat,
        'model': model,
        'last_activity': datetime.now(),
        'created_at': datetime.now()
    }
    return new_session_id, chat_sessions[new_session_id]

# Request/Response models
class ChatMessage(BaseModel):
    role: str  # 'user' or 'assistant'
    content: str

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None
    conversation_history: Optional[List[ChatMessage]] = []

class ChatResponse(BaseModel):
    response: str
    session_id: str
    status: str = "success"

@app.get("/")
async def serve_home():
    return FileResponse("chat.html")

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "active_sessions": len(chat_sessions)
    }

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Main chat endpoint with conversation memory

    This endpoint maintains conversation context using session IDs.
    If no session_id is provided, a new session is created.

    Args:
        request: ChatRequest containing the user message and optional session_id

    Returns:
        ChatResponse with the bot's response and session_id
    """
    try:
        # Get or create session
        session_id, session = get_or_create_session(request.session_id)
        chat = session['chat']

        # Send message and get response
        response = chat.send_message(request.message)

        return ChatResponse(
            response=response.text,
            session_id=session_id,
            status="success"
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat: {str(e)}")

@app.post("/chat/simple")
async def simple_chat(request: ChatRequest):
    """
    Simplified chat endpoint without conversation memory
    Each request is independent with no context retention.

    Args:
        request: ChatRequest containing just the user message

    Returns:
        Simple response with the bot's answer
    """
    try:
        model = get_gemini_model()
        chat_session = model.start_chat(history=[])
        response = chat_session.send_message(request.message)

        return {
            "response": response.text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat: {str(e)}")

@app.delete("/session/{session_id}")
async def delete_session(session_id: str):
    """
    Delete a specific chat session

    Args:
        session_id: The session ID to delete

    Returns:
        Success message
    """
    if session_id in chat_sessions:
        del chat_sessions[session_id]
        return {"status": "success", "message": "Session deleted"}
    return {"status": "not_found", "message": "Session not found"}

@app.post("/session/new")
async def create_new_session():
    """
    Create a new chat session

    Returns:
        New session ID
    """
    session_id, _ = get_or_create_session()
    return {"session_id": session_id, "status": "created"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
