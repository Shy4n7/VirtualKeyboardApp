# AI Virtual Keyboard ⌨️

[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![Mediapipe](https://img.shields.io/badge/Mediapipe-Latest-orange.svg)](https://google.github.io/mediapipe/)

A futuristic AI-powered virtual keyboard that allows you to type in mid-air using hand gestures. Built with Python, OpenCV, and Mediapipe for real-time computer vision performance.

## 🌟 Features

- **Touchless Typing**: Type using only hand gestures and finger movements
- **Real-time Tracking**: Low-latency hand tracking for a smooth experience
- **Intelligent Detection**: Uses distance between fingertips to simulate "clicks"
- **Visual Feedback**: Keys light up and change color upon interaction
- **Offline Capable**: Runs entirely locally without internet dependency

## 🚀 Quick Start

### Prerequisites

```bash
Python 3.8+
Webcam
```

### Installation

```bash
# Clone repository
git clone https://github.com/Shy4n7/VirtualKeyboardApp.git
cd VirtualKeyboardApp

# Install dependencies
pip install opencv-python mediapipe cvzone numpy

# Run the application
python main.py
```

## 💡 How It Works

1. **Hand Detection**: The app uses Mediapipe to detect hand landmarks in real-time.
2. **Position Mapping**: Finger coordinates are mapped to the virtual keyboard layout.
3. **Click Simulation**: When the distance between the index finger and thumb (or depth) falls below a threshold, a "click" is registered.
4. **Input Generation**: The `pynput` or similar library sends the keystroke to the operating system.

## 🛠️ Tech Stack

- **Language**: Python
- **Computer Vision**: OpenCV
- **ML Pipeline**: Google Mediapipe
- **Utilities**: CVZone, NumPy

## 🎓 Skills Demonstrated

- Computer Vision & Image Processing
- Real-time Gesture Recognition
- Human-Computer Interaction (HCI)
- Coordinate Geometry & Vector Math
- Python Application Development

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## 📝 License

This project is licensed under the MIT License.

## 📧 Contact

**Shyan**
- GitHub: [@Shy4n7](https://github.com/Shy4n7)

---

*Type the future with AI*
