# Real-Time Face Detection System

![Python](https://img.shields.io/badge/python-3.7+-blue)
![OpenCV](https://img.shields.io/badge/opencv-4.x-green)
![License](https://img.shields.io/badge/license-MIT-orange)
![Platform](https://img.shields.io/badge/platform-cross--platform-purple)
![Status](https://img.shields.io/badge/status-active-teal)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)

A lightweight Python script using OpenCV's Haar Cascade classifier to detect human faces in real-time via webcam with robust window-close handling.

Unlike basic scripts that only check for a keypress to exit, this implementation includes a smart check for the window's visibility state. This ensures the application closes cleanly even if the user clicks the native **Close (X)** button.

---

## Features

- **Real-time detection** : Smooth frame-by-frame face detection via your default webcam feed.
- **Smart window closing** : Gracefully exits on `q` keypress or native Close (X) click via `WND_PROP_VISIBLE`.
- **Optimized parameters** : Pre-tuned `scaleFactor` and `minNeighbors` values to reduce false positives while maintaining accuracy.

---

## Prerequisites

Python 3.7+ must be installed on your system. Then install OpenCV:

```bash
pip install opencv-python
```

---

## How to Run

1. Save the script as `face_detection.py`

2. Open your terminal and navigate to the project folder:

```bash
cd /path/to/your/project
```

3. Run the script:

```bash
python face_detection.py
```

---

## How to Exit

You can stop the video stream safely using two methods:

| Method | Action |
|--------|--------|
|  Keyboard | Press `q` while the video window is focused |
|  Window button | Click the native **✕ Close** button on the window titlebar |

---

## Code Breakdown

| API / Method | Description |
|---|---|
| `cv2.CascadeClassifier` | Loads OpenCV's pre-trained frontal face Haar Cascade model |
| `cv2.VideoCapture(0)` | Connects to the default system webcam |
| `cv2.getWindowProperty` | Monitored in the loop to detect if the user manually closed the GUI window |
| `detectMultiScale` | Processes the grayscale frame to locate faces using the configured scale and neighbor thresholds |

---

## Project Structure

```
webcam-face-detection/
├── face-detection.py   # Main script
└── README.md           # Project documentation
```

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

*Built with ❤️ using [OpenCV](https://github.com/opencv/opencv)*