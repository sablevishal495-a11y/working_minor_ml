import sys
import importlib.util as importlib_util

MIN_PY = (3, 8)
MAX_PY = (3, 11)

def check_python_version():
    major, minor = sys.version_info[:2]
    if (major, minor) < MIN_PY or (major, minor) > MAX_PY:
        print(f"Unsupported Python version {major}.{minor}.{sys.version_info[2]}.")
        print("Mediapipe currently supports Python 3.8 - 3.11. Please install a supported Python and create a virtual environment.")
        return False
    print(f"Python version OK: {major}.{minor}.{sys.version_info[2]}")
    return True

def check_packages():
    pkgs = ["cv2", "numpy", "mediapipe"]
    missing = []
    for p in pkgs:
        if importlib_util.find_spec(p) is None:
            missing.append(p)
    if missing:
        print("Missing packages:", ", ".join(missing))
        print("Install them with: python -m pip install -r requirements.txt")
        return False
    print("All required packages are installed: cv2, numpy, mediapipe")
    return True

if __name__ == '__main__':
    ok_ver = check_python_version()
    ok_pkgs = check_packages()
    if not ok_ver or not ok_pkgs:
        sys.exit(1)
    print("Environment looks good. You can run: python air_canvas.py")
