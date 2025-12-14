import cv2
import numpy as np
import mediapipe as mp

print('cv2', cv2.__version__)
print('numpy', np.__version__)
print('mediapipe', mp.__version__)

# Try to create a hands detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
print('Hands created')

# Try opening the camera for one frame
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Warning: Camera could not be opened (no camera or permission issue)')
else:
    ret, frame = cap.read()
    print('Camera read ok:', ret)
    if ret:
        print('Frame shape:', frame.shape)
    cap.release()

print('Smoke test finished')
