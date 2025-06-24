#!/bin/bash

# Development setup script for Job Board API

set -e  # Exit on any error

echo "🚀 Setting up Job Board API development environment..."

# Create virtual environment
echo "📦 Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "📚 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "⚙️ Creating .env file from template..."
    cp .env.example .env
    echo "📝 Please update .env file with your settings"
fi

# Create uploads directory
echo "📁 Creating uploads directory..."
mkdir -p uploads
touch uploads/.gitkeep

# Start services with Docker Compose
echo "🐳 Starting database and cache services..."
docker-compose up -d postgres redis rabbitmq

# Wait for services to be ready
echo "⏳ Waiting for services to be ready..."
sleep 10

# Run database migrations
echo "📊 Running database migrations..."
alembic upgrade head

# Create initial data (optional)
echo "🌱 Creating initial data..."
python scripts/create_initial_data.py

echo "✅ Development environment setup complete!"
echo ""
echo "🎯 Next steps:"
echo "1. Activate virtual environment: source venv/bin/activate"
echo "2. Start the API server: uvicorn app.main:app --reload"
echo "3. Visit API docs: http://localhost:8000/docs"
echo "4. Check health: http://localhost:8000/health"
echo ""
echo "🛠️ Useful commands:"
echo "- Run tests: pytest"
echo "- Format code: black . && isort ."
echo "- Check linting: flake8 ."
echo "- Stop services: docker-compose down"
