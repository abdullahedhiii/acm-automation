#!/bin/bash

# ACM Chatbot - Installation Test Script
echo "========================================="
echo "ACM NUCES Karachi Chatbot - Setup Test"
echo "========================================="
echo ""

# Check Python
echo "1. Checking Python installation..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo "✓ Found: $PYTHON_VERSION"
else
    echo "✗ Python 3 not found. Please install Python 3.11+"
    exit 1
fi
echo ""

# Check if in correct directory
echo "2. Checking directory structure..."
if [ ! -f "main.py" ]; then
    echo "✗ main.py not found. Please run this script from the acm-chatbot directory"
    exit 1
fi
echo "✓ main.py found"
echo "✓ requirements.txt found"
echo "✓ chat.html found"
echo ""

# Create virtual environment
echo "3. Creating virtual environment..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi
echo ""

# Activate and install
echo "4. Installing dependencies..."
source venv/bin/activate
pip install -q --upgrade pip
pip install -q -r requirements.txt
echo "✓ Dependencies installed"
echo ""

# Check for .env
echo "5. Checking environment configuration..."
if [ ! -f ".env" ]; then
    echo "⚠ .env file not found"
    echo "Creating .env from template..."
    cp .env.example .env
    echo ""
    echo "================================================"
    echo "ACTION REQUIRED:"
    echo "Please edit .env file and add your Gemini API key"
    echo ""
    echo "Get your API key from:"
    echo "https://makersuite.google.com/app/apikey"
    echo ""
    echo "Then run: source venv/bin/activate && python main.py"
    echo "================================================"
else
    echo "✓ .env file exists"

    # Check if API key is set
    if grep -q "your_gemini_api_key_here" .env; then
        echo "⚠ Please update GEMINI_API_KEY in .env file"
    else
        echo "✓ API key appears to be configured"
        echo ""
        echo "================================================"
        echo "Setup complete! To start the chatbot:"
        echo ""
        echo "1. Activate virtual environment:"
        echo "   source venv/bin/activate"
        echo ""
        echo "2. Start the server:"
        echo "   python main.py"
        echo ""
        echo "3. Open chat.html in your browser"
        echo "================================================"
    fi
fi

echo ""
echo "Installation test complete!"
