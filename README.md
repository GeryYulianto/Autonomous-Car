# Assistance Car Vision System

A computer-vision project that helps analyze road videos and explain driving risk in simple terms. The system looks at each video frame, detects road objects, estimates distance, checks lane/drivable areas, tracks movement, and shows whether the situation is **Safe**, **Caution**, **Danger**, or **Critical**.

This project was built as a driving-assistance prototype and resume portfolio project.

---

## What This Project Does

- Detects vehicles, pedestrians, motorcycles, and other road objects using YOLO.
- Estimates how far objects are from the camera using Intel RealSense depth data.
- Finds lane and drivable-road areas.
- Tracks movement in the scene with optical flow.
- Calculates object-level and scene-level risk.
- Shows results in a FastAPI web dashboard.
- Saves analysis data into SQLite.
- Creates annotated videos and audio warnings for risky moments.

---

## Why It Is Useful

Road conditions can change very quickly. A driver-assistance system needs to answer simple questions:

- What objects are in front of the car?
- How close are they?
- Are they moving?
- Is the road area still safe?

This project combines those answers into one easy-to-read risk result, so both technical and non-technical users can understand what is happening in the video.

---

## Main Features

| Feature | Simple Explanation |
| --- | --- |
| Object Detection | Finds important road objects such as cars and people. |
| Distance Estimation | Measures how far detected objects are in meters. |
| Lane Detection | Checks lane and drivable-road areas. |
| Motion Tracking | Detects movement in the video scene. |
| Risk Scoring | Gives each object and scene a risk level. |
| Web Dashboard | Shows the video result, warning status, FPS, and timing. |
| Data Storage | Saves frame-by-frame results into `perception.db`. |

---

## Performance Results

The system was optimized to run faster and closer to real-time performance.

| Area Improved | Before | After | Improvement |
| --- | ---: | ---: | ---: |
| YOLO Detection | `84 ms/frame` | `76 ms/frame` | About `10%` faster |
| Optical Flow | `273 ms/frame` | `63 ms/frame` | About `76.9%` faster |
| Lane Detection | `150 ms/frame` | `82 ms/frame` | About `45%` faster |
| Full Pipeline | `1202 ms/frame` | `309 ms/frame` | About `92.5%` faster |

| Version | Speed |
| --- | --- |
| Baseline CPU version | About `0.83 FPS` |
| Optimized GPU version | About `4.08 FPS` |

Test device: **NVIDIA RTX 3050 Ti**.

---

## Processing Flow

```text
Video Input
   ↓
Frame Processing
   ↓
Object Detection + Distance + Lane Check + Motion Tracking
   ↓
Risk Calculation
   ↓
Dashboard + Output Video + Database
```

Supported input:

- Intel RealSense `.bag` recordings
- Standard `.mp4` videos

---

## Output

After a video is processed, the project can generate:

| Output | Description |
| --- | --- |
| Information Video | Detailed result with boxes, distance, risk, FPS, and timing. |
| Driving Video | Simpler view focused on driver-friendly warnings. |
| Audio Alert | Warning sound for high-risk moments. |
| SQLite Database | Stores detections, risk results, motion, lane data, and performance. |
| System Log | Stores processing logs. |

Example output files:

```text
assets/output/{run_id}_information.mp4
assets/output/{run_id}_driving.mp4
assets/output/{run_id}_alert.wav
perception.db
logs/system.log
```

---

## Tech Stack

- **Python** for the main application
- **YOLO / Ultralytics** for object detection
- **OpenCV** for video processing and motion tracking
- **Intel RealSense SDK** for depth-camera recordings
- **FastAPI** for the web dashboard
- **SQLite** for local data storage
- **FFmpeg** for video and audio output

---

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the web dashboard:

```bash
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

Run from the command line:

```bash
python run_backend.py --source "C:/path/to/video.mp4" --type mp4
```

For RealSense recordings:

```bash
python run_backend.py --source "C:/path/to/recording.bag" --type bag
```

---

## Summary

**Assistance Car Vision System** is an AI-based driving-assistance prototype that analyzes road videos to detect objects, estimate distance, identify lane/drivable areas, track motion, and calculate driving risk. It includes a FastAPI dashboard, SQLite logging, annotated video output, audio alerts, and GPU optimization that improved the full pipeline from about **0.83 FPS** to **4.08 FPS** on an **RTX 3050 Ti**.

---

## Possible Improvements

- Support depth estimation for normal videos without RealSense data.
- Export the model to ONNX for faster deployment.
- Improve the dashboard for mobile screens.
- Test more road, weather, and lighting conditions.
