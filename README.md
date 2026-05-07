# Hand Gesture Control System 🖐️💻

This project uses Computer Vision to control computer functions (like screen brightness or cursor movement) using hand gestures. It leverages the power of MediaPipe for high-fidelity hand tracking and OpenCV for real-time video processing.

## 🚀 Features
* **Real-time Hand Tracking:** Uses MediaPipe to detect 21 hand landmarks.
* **Finger Counting:** Logic to detect which fingers are up or down.
* **System Control:** Uses PyAutoGUI and Screen-Brightness-Control to interact with your OS.
* **Dual Hand Support:** Handles both left and right hand logic differently for better accuracy.

## 🛠️ Tech Stack
* **Python**
* **OpenCV:** For camera feed and image processing.
* **MediaPipe:** For hand landmark detection.
* **PyAutoGUI:** For simulating mouse/keyboard actions.
* **Screen-Brightness-Control:** For hardware interaction.

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/devraj-30/Hand-Gesture-Control.git](https://github.com/devraj-30/Hand-Gesture-Control.git)
   cd Hand-Gesture-Control
