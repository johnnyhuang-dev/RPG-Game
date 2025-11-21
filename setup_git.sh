#!/bin/bash

# Git and GitHub Setup Script
# This script will initialize Git and connect to your GitHub repository

set -e

echo "🚀 Setting up Git and GitHub connection..."

# Navigate to project directory
cd "/Users/orproja/My project"

# Check if Git is initialized
if [ -d ".git" ]; then
    echo "✅ Git is already initialized"
else
    echo "📦 Initializing Git repository..."
    git init
    echo "✅ Git repository initialized"
fi

# Check if remote is already set
if git remote get-url origin &>/dev/null; then
    echo "⚠️  Remote 'origin' already exists. Current URL:"
    git remote get-url origin
    read -p "Do you want to update it? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        git remote set-url origin https://github.com/johnnyhuang-dev/RPG-Game.git
        echo "✅ Remote updated"
    fi
else
    echo "🔗 Adding GitHub remote..."
    git remote add origin https://github.com/johnnyhuang-dev/RPG-Game.git
    echo "✅ Remote added"
fi

# Check Git user configuration
echo ""
echo "📋 Current Git configuration:"
git config user.name || echo "⚠️  user.name not set"
git config user.email || echo "⚠️  user.email not set"

echo ""
echo "💡 If user.name or user.email are not set, you'll need to configure them:"
echo "   git config user.name 'Your Name'"
echo "   git config user.email 'your.email@example.com'"
echo ""
echo "   Or set globally:"
echo "   git config --global user.name 'Your Name'"
echo "   git config --global user.email 'your.email@example.com'"

# Check if there are files to commit
if [ -n "$(git status --porcelain)" ]; then
    echo ""
    echo "📝 Files ready to be committed. You can now:"
    echo "   1. git add ."
    echo "   2. git commit -m 'Initial commit'"
    echo "   3. git branch -M main"
    echo "   4. git push -u origin main"
else
    echo ""
    echo "✅ No uncommitted changes"
fi

echo ""
echo "✨ Setup complete! Your repository is now connected to GitHub."
echo "   Repository: https://github.com/johnnyhuang-dev/RPG-Game.git"

