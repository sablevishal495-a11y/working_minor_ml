# Air Canvas

Simple hand-tracking "air drawing" app using MediaPipe, OpenCV, and NumPy.

## Requirements
- Python 3.8 - 3.11 (64-bit recommended)
- Windows 10/11

## Setup (Powershell)
```powershell
# Optional: create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```
------
If `mediapipe` fails to install on your machine, see troubleshooting below.

## Run
```powershell
python air_canvas.py
```

Controls:
- Index finger up: Draw
- Index + Middle fingers up: Select color (tap color bar at top)
- `C`: Clear canvas
- `Q`: Quit

## Troubleshooting
- If you see `ModuleNotFoundError: No module named 'mediapipe'`, run:
```powershell
python -m pip install mediapipe
```
- If installation fails with wheel or DLL errors, try a fresh virtual environment or use Python 3.10/3.11 (64-bit). Copy the full traceback and open an issue so I can help.

---
Made by: Air Canvas helper

