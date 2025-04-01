# 📢 **Hand Gesture Volume Control**

This project allows you to control your system's volume using hand gestures detected via your webcam. It leverages **OpenCV**, **MediaPipe**, and **Pycaw** to track hand movements and adjust the volume dynamically.

---

## 🚀 **Features**
- Control system volume with simple thumb and index finger gestures.
- Real-time hand tracking using MediaPipe.
- Smooth volume adjustment based on finger distance.

---

## ⚙️ **Requirements**

- **Python 3.x**
- **Libraries:**  
  - `opencv-python` (for video capture and image processing)  
  - `mediapipe` (for hand tracking)  
  - `pycaw` (for volume control on Windows)  
  - `comtypes` & `ctypes` (for COM interface communication)

---

## 📥 **Installation**

1. Clone the repository (if applicable):
   ```bash
   git clone https://github.com/your-repo/hand-gesture-volume-control.git
   cd hand-gesture-volume-control
   ```

2. Install the required libraries:
   ```bash
   pip install opencv-python mediapipe pycaw comtypes
   ```

---

## 🖥️ **How to Run**

```bash
python gesture_volume_control.py
```

- A window will open showing the webcam feed.
- Move your **thumb** and **index finger** closer together or apart:
  - **Closer together →** Lower volume
  - **Farther apart →** Higher volume
- Press **`q`** to quit the application.

---

## 📊 **How It Works**

1. **Hand Detection:** Uses MediaPipe's hand tracking to detect key landmarks on your hand.  
2. **Gesture Recognition:** Calculates the distance between your thumb and index finger.  
3. **Volume Control:** Maps this distance to a volume level using the `pycaw` library.

---

## ⚠️ **Notes**

- **Operating System:** This works on **Windows** since `pycaw` relies on the Windows Core Audio API.  
- **Camera:** Ensure your webcam is connected and working properly.  
- **Lighting:** Good lighting improves hand detection accuracy.

---

## 🙋 **Troubleshooting**

- **Error with `pycaw` or `comtypes`:** Make sure they are installed correctly using `pip`.  
- **Hand not detected:** Try adjusting lighting or repositioning your hand.  
- **No volume change:** Check your system's audio settings to ensure the volume isn't locked.

---

## 📄 **License**

This project is open-source and free to use.  
*(Feel free to modify, improve, and contribute!)*

---
