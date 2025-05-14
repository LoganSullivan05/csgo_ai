# 🎯 CSGO AI Triggerbot (CNN-Based)

An AI-powered triggerbot for Counter-Strike: Global Offensive, using a Convolutional Neural Network (CNN) to detect enemy presence and automatically fire when a target is within the crosshair.

## 🧠 Overview

This project leverages deep learning to classify small screen patches from CSGO and simulate trigger pulls based on real-time predictions. The system includes:

- A custom labeling tool for training data collection
- A Node.js-based local server for annotation
- A Keras CNN model for classification
- A Python-based bot that reads screen pixels and triggers the mouse when enemies are detected

## 🛠️ Components

### `screenshot.py`
Captures 64×64 screen patches centered on the crosshair when the mouse is clicked. Saves the screenshots incrementally to `raw_data/`.

- Press `[` to activate
- Press `p` to pause/unpause data collection

### `label_client.html`
A browser interface to label screenshots manually. Allows users to click the image or press keys to mark coordinates used for training the model.

### `label_server.js`
A Node.js + Express backend to serve labeling images, collect labeled coordinates, and save processed data for training.

### `model.py`
Defines and trains a CNN with Keras (TensorFlow backend). The network uses 64×64 RGB input and classifies into 5 output categories (enemy types or directions). Training is done using image directories labeled via the labeling tool.

### `trigger_bot.py`
A Python script that uses MSS to capture screen pixels in real time, performs model inference, and clicks the mouse if the predicted probability of an enemy exceeds a threshold.

## 🕹️ Controls

Inside the bot (`trigger_bot.py`), the following hotkeys are available:

| Key | Action |
|-----|--------|
| `o` | Switch target team (T or CT) |
| `p` | Pause/resume the bot |
| `=` | Increase confidence threshold |
| `-` | Decrease confidence threshold |

## 📦 Setup Instructions

### Prerequisites

- Python 3.8+
- Node.js (for labeling server)
- CSGO running in windowed mode (or borderless)
- Libraries:
  - `tensorflow`
  - `numpy`
  - `mss`
  - `keyboard`
  - `mouse`
  - `pyautogui`
  - `express` (Node)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/csgo-ai-triggerbot.git
   cd csgo-ai-triggerbot
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start label server**
   ```bash
   node label_server.js
   ```

4. **Open labeling client**
   - Visit [http://localhost](http://localhost) in your browser
   - Click or press keys to label images

5. **Train the model**
   ```bash
   python model.py
   ```

6. **Run the triggerbot**
   ```bash
   python trigger_bot.py
   ```

7. **Collect data**
   ```bash
   python screenshot.py
   ```

## 🧪 Model Training Notes

- Screenshots must be saved as 64×64 PNGs under labeled folders in `images/`
- Adjust number of classes and final dense layer activation as needed
- Training runs for 20 epochs using `CategoricalCrossentropy`

![screenshot_18](https://github.com/user-attachments/assets/a21d2945-24b0-4ade-a535-c9dc6345d01c)


## ⚠️ Disclaimer

This project is intended for educational and research purposes only. Use of automated tools in online games like CSGO may violate terms of service and result in bans. **Use at your own risk.**
