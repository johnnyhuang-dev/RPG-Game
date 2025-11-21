#!/bin/bash

# Quick verification and completion script
# Run this AFTER CommandLineTools installation is complete

set -e

echo "🔍 Verifying Git setup..."

cd "/Users/orproja/My project"

# Test if Git works now
if git --version > /dev/null 2>&1; then
    echo "✅ Git is working!"
    git --version
else
    echo "❌ Git still not working. CommandLineTools may still be installing."
    echo "   Please wait a bit longer and try again."
    exit 1
fi

# Verify repository is initialized
if [ -d ".git" ]; then
    echo "✅ Git repository is initialized"
else
    echo "📦 Initializing Git repository..."
    git init
fi

# Verify remote is set
if git remote get-url origin > /dev/null 2>&1; then
    echo "✅ GitHub remote is configured:"
    git remote get-url origin
else
    echo "🔗 Adding GitHub remote..."
    git remote add origin https://github.com/johnnyhuang-dev/RPG-Game.git
fi

# Check Git user config
echo ""
echo "📋 Git user configuration:"
USER_NAME=$(git config user.name 2>/dev/null || echo "")
USER_EMAIL=$(git config user.email 2>/dev/null || echo "")

if [ -z "$USER_NAME" ] || [ -z "$USER_EMAIL" ]; then
    echo "⚠️  Git user name or email not configured"
    echo ""
    echo "Please set them now:"
    echo "  git config user.name 'Your Name'"
    echo "  git config user.email 'your.email@example.com'"
    echo ""
    echo "Or set globally (for all repositories):"
    echo "  git config --global user.name 'Your Name'"
    echo "  git config --global user.email 'your.email@example.com'"
    echo ""
    read -p "Would you like to set them now? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        read -p "Enter your name: " name
        read -p "Enter your email: " email
        git config user.name "$name"
        git config user.email "$email"
        echo "✅ Git user configured"
    fi
else
    echo "✅ Name: $USER_NAME"
    echo "✅ Email: $USER_EMAIL"
fi

# Check status
echo ""
echo "📊 Current repository status:"
git status --short || git status

echo ""
echo "✨ Setup verification complete!"
echo ""
echo "Next steps:"
echo "  1. Review the files to commit (git status)"
echo "  2. Add files: git add ."
echo "  3. Commit: git commit -m 'Initial commit'"
echo "  4. Push to GitHub: git push -u origin main"

