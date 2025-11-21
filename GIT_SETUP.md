# Git & GitHub Setup Guide

## Quick Setup Steps

### Step 1: Fix CommandLineTools (if needed)
If you're getting xcrun errors, run this in Terminal:
```bash
xcode-select --install
```
Or if that doesn't work:
```bash
sudo xcode-select --reset
```

### Step 2: Initialize Git Repository
```bash
cd "/Users/orproja/My project"
git init
```

### Step 3: Configure Git (if not already set globally)
```bash
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

Or set globally:
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 4: Add Remote Repository
```bash
git remote add origin https://github.com/johnnyhuang-dev/RPG-Game.git
```

### Step 5: Add and Commit Files
```bash
git add .
git commit -m "Initial commit"
```

### Step 6: Push to GitHub
```bash
git branch -M main
git push -u origin main
```

## For Future Commits in Cursor

Once set up, you can commit and push directly from Cursor:
1. Make your changes
2. Use Cursor's Git panel (Source Control) to stage files
3. Write a commit message
4. Commit
5. Push to GitHub

Or use terminal commands:
```bash
git add .
git commit -m "Your commit message"
git push
```

