# 🚗💤 Driver Alertness & Drowsiness Detection System

An intelligent computer vision and IoT-based safety system built with Python, OpenCV, and Haarcascade classifiers designed to monitor driver alertness in real-time, detect drowsiness or prolonged eye closure, and trigger immediate audio-visual alerts to prevent road accidents.

---

## ⚡ Quick Start (3 Steps)

### Step 1 — Clone the Repository
```bash
git clone [https://github.com/YakeshKrishnanD/Driver-alertness-detection.git](https://github.com/YakeshKrishnanD/Driver-alertness-detection.git)
cd Driver-alertness-detection

```

### Step 2 — Install Dependencies

Make sure you have Python installed, then install the required computer vision and audio libraries:

```bash
pip install opencv-python numpy pygame

```

### Step 3 — Run the Detection Script

```bash
python DAD.py

```

*Press `q` on your keyboard to exit the live video feed window.*

---

## 📋 Features

| Feature | Description |
| --- | --- |
| **Real-Time Face & Eye Tracking** | Utilizes OpenCV Haar Cascade classifiers (`haarcascade_frontalface_default.xml` and `haarcascade_eye.xml`) to continuously track facial regions and eye state. |
| **Drowsiness Thresholding** | Calculates eye aspect states and duration of closure to distinguish between normal blinking and driver fatigue. |
| **Instant Alarm System** | Integrates automated sound alarms (`pygame`) to alert drivers instantly when drowsiness is detected. |
| **Edge Deployment Support** | Includes lightweight scripts optimized for execution on Raspberry Pi hardware. |
| **Visual Documentation** | Stores operational reports, certificates, and detection event snapshots directly in the repository. |

---

## 🗂️ Project Structure

```text
Driver-alertness-detection/
├── DAD.py                                    ← Core real-time detection script
├── haarcascade_eye.xml                       ← Pre-trained eye detector cascade
├── haarcascade_frontalface_default (1).xml   ← Pre-trained face detector cascade
├── project code.txt                          ← Reference algorithm logic
├── rasberry project code.txt                 ← Raspberry Pi deployment code
├── Certificates.pdf                          ← Project completion / achievement certificate
├── final report.pdf                          ← Comprehensive project documentation report
├── researchpaper.docx                        ← Associated research paper documentation
└── screenshot/                               ← Captured UI & event visual assets
    ├── Drowsiness detection.png              ← Alert state visualization
    ├── Eye detection.png                     ← Normal active state tracking
    └── Eye closed detection.png              ← Extended closure detection

```

---

## 🏗️ System Architecture & Workflow

1. **Video Acquisition:** Captures live video streams using a standard webcam or a Raspberry Pi camera module.
2. **Preprocessing & Detection:** Converts frames to grayscale and uses Haar Cascades to isolate the region of interest (ROI) for faces and eyes.
3. **State Evaluation:** Continuously checks frame-by-frame eye visibility. If the eyes remain closed past a threshold duration, a warning state triggers.
4. **Alert Execution:** Fires buzzer/audio alarms and renders visual warning overlays on the screen.

---

## 🖥️ Screenshots & Visual Interface

### 🟢 1. Active Eye Detection (Normal State)
![Eye Detection](screenshot/Eye%20detection.png)

### 🔴 2. Eye Closed / Drowsiness Alert State
![Drowsiness Detection](screenshot/Drowsiness%20detection.png)

### ⚠️ 3. Extended Closure Warning Capture
![Eye Closed Detection](screenshot/Eye%20closed%20detection.png)

---

## 👨‍💻 Author

**Yakesh Krishnan D**

Driver Alertness Detection System — Advanced computer vision and automotive safety systems.

⭐ If you find this project useful, consider giving the repository a star!

```

```
