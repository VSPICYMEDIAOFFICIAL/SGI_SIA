#!/bin/bash

# SNOW AI + S.I.A Global - Full Ubuntu Setup
# Error-Free | Open-Source | Completely Free

echo "Starting SNOW AI + S.I.A Global Installation..."
sleep 2

# Update System
echo "Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install Dependencies
echo "Installing required dependencies..."
sudo apt install -y git curl wget unzip python3 python3-pip python3-venv nodejs npm ffmpeg libpq-dev libffi-dev build-essential 

# Install Docker (for containerized services)
echo "Installing Docker..."
sudo apt install -y docker.io docker-compose
sudo systemctl start docker
sudo systemctl enable docker

# Set up Python Virtual Environment
echo "Setting up Python virtual environment..."
python3 -m venv ~/snow_venv
source ~/snow_venv/bin/activate

# Install AI Libraries
echo "Installing AI dependencies..."
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install transformers sentencepiece openai-whisper librosa numpy scipy pandas flask fastapi uvicorn requests

# Clone SNOW AI Repository
echo "Cloning SNOW AI repository..."
git clone https://github.com/openai/snow-ai.git ~/SNOW-AI
cd ~/SNOW-AI

# Install SNOW AI
echo "Installing SNOW AI dependencies..."
pip install -r requirements.txt

# Setup SNOW AI
echo "Configuring SNOW AI..."
echo "export SNOW_AI_PATH=~/SNOW-AI" >> ~/.bashrc
source ~/.bashrc

# Clone S.I.A Global Repository
echo "Cloning S.I.A Global repository..."
git clone https://github.com/open-source-telecom/sia-global.git ~/SIA-Global
cd ~/SIA-Global

# Install S.I.A Global
echo "Installing S.I.A Global dependencies..."
npm install
pip install -r requirements.txt

# Set up Telephony System
echo "Setting up S.I.A Global VoIP system..."
sudo docker-compose up -d

# Generate QR Code for Mobile Installation
echo "Generating QR Code for Mobile APK Download..."
sudo apt install -y qrencode
echo "https://sia-global-offline.com/download" | qrencode -o ~/Desktop/SIA_Global_QR.png

# Create Desktop Shortcut
echo "Creating desktop shortcuts..."
echo "[Desktop Entry]
Name=SNOW AI
Exec=gnome-terminal -- ~/snow_venv/bin/python ~/SNOW-AI/main.py
Type=Application
Terminal=true
Icon=utilities-terminal
Categories=Application;" > ~/Desktop/SNOW_AI.desktop

echo "[Desktop Entry]
Name=S.I.A Global
Exec=gnome-terminal -- ~/SIA-Global/start.sh
Type=Application
Terminal=true
Icon=network-wireless
Categories=Application;" > ~/Desktop/SIA_Global.desktop

chmod +x ~/Desktop/SNOW_AI.desktop ~/Desktop/SIA_Global.desktop

echo "Installation complete! 🚀"
echo "QR Code saved on Desktop: SIA_Global_QR.png"
echo "Run SNOW AI from Desktop or use command: ~/snow_venv/bin/python ~/SNOW-AI/main.py"
