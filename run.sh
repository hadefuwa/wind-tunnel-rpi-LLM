#!/bin/bash

# Wind Tunnel Data Explorer Startup Script

echo "🌪️ Starting Wind Tunnel Data Explorer..."

# Check if Ollama is running
echo "Checking Ollama service..."
if ! curl -s http://localhost:11434 > /dev/null; then
    echo "⚠️  Ollama is not running. Starting Ollama..."
    ollama serve &
    sleep 5
    echo "✅ Ollama started"
else
    echo "✅ Ollama is already running"
fi

# Check if Gemma model is available
echo "Checking for Gemma2 model..."
if ! ollama list | grep -q "gemma2:2b"; then
    echo "📥 Downloading Gemma2 2B model..."
    ollama pull gemma2:2b
    echo "✅ Model downloaded"
else
    echo "✅ Gemma2 2B model is available"
fi

# Install Python dependencies if needed
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Start Streamlit app
echo "🚀 Starting Streamlit app..."
streamlit run app.py
