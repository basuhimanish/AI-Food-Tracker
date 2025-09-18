#!/bin/bash
echo "Starting AI Food Tracker Server..."
unset DATABASE_URL
cd "$(dirname "$0")"
source venv/Scripts/activate
uvicorn app.main:app --reload
