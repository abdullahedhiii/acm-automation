#!/bin/bash

echo "========================================="
echo "ACM NUCES Karachi Chatbot Server"
echo "========================================="
echo ""

# Change to script directory
cd "$(dirname "$0")"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Error: Virtual environment not found."
    echo "Please run: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "Error: .env file not found."
    echo "Please create .env file with your GEMINI_API_KEY"
    exit 1
fi

# Activate virtual environment
source venv/bin/activate

# Start server
echo "Starting ACM Chatbot Server..."
echo "Server will be available at: http://localhost:8000"
echo ""
echo "To test:"
echo "1. Open chat.html in your browser"
echo "2. Or visit http://localhost:8000/docs for API documentation"
echo ""
echo "Press Ctrl+C to stop the server"
echo "========================================="
echo ""

python main.py
