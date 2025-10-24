import cv2
import mediapipe as mp
import numpy as np
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Keyboard layout
keys = [
    ['Q','W','E','R','T','Y','U','I','O','P'],
    ['A','S','D','F','G','H','J','K','L'],
    ['Z','X','C','V','B','N','M','Space','Back','Clear']
]

# Timing for typing delay
last_time_pressed = 0
typing_delay = 0.3  # seconds

# Initialize typed text
typed_text = ""

# Camera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # width
cap.set(4, 720)   # height

# Separate typed text window
typed_window = np.ones((720, 400, 3), np.uint8)*255

def draw_keyboard(frame):
    """Draw keyboard at bottom-center with transparency."""
    overlay = frame.copy()
    h, w, _ = frame.shape
    key_w, key_h = 80, 80
    start_y = h - len(keys)*key_h - 20  # little above bottom
    start_x = (w - 10*key_w)//2
    
    key_positions = {}
    for i, row in enumerate(keys):
        y = start_y + i*key_h
        x = start_x
        for key in row:
            cv2.rectangle(overlay, (x, y), (x+key_w-5, y+key_h-5), (200,200,200), -1)
            cv2.putText(overlay, key, (x+10, y+55), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)
            key_positions[key] = (x, y, x+key_w-5, y+key_h-5)
            x += key_w
    # transparency
    alpha = 0.6
    cv2.addWeighted(overlay, alpha, frame, 1-alpha, 0, frame)
    return key_positions

def is_fist(landmarks):
    """Detect if hand is fist based on finger tips positions."""
    tips_ids = [8, 12, 16, 20]
    return all(landmarks[i].y > landmarks[i-2].y for i in tips_ids)

def index_finger_extended(landmarks):
    return landmarks[8].y < landmarks[6].y  # index finger tip above pip joint

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    key_positions = draw_keyboard(frame)
    
    pointer = None
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)
            landmarks = handLms.landmark

            if index_finger_extended(landmarks) and not is_fist(landmarks):
                h, w, _ = frame.shape
                cx, cy = int(landmarks[8].x*w), int(landmarks[8].y*h)
                pointer = (cx, cy)
                cv2.circle(frame, pointer, 10, (255,0,0), -1)
                
                # Check for key press
                if time.time() - last_time_pressed > typing_delay:
                    for key, (x1,y1,x2,y2) in key_positions.items():
                        if x1 < cx < x2 and y1 < cy < y2:
                            if key == "Space":
                                typed_text += " "
                            elif key == "Back":
                                typed_text = typed_text[:-1]
                            elif key == "Clear":
                                typed_text = ""
                            else:
                                typed_text += key
                            last_time_pressed = time.time()
                            break

    # Update typed window
    typed_window[:] = 255
    if typed_text:
        lines = np.array_split(list(typed_text), max(1, len(typed_text)//20))
        for i, line in enumerate(lines):
            y = 40 + i*40
            cv2.putText(typed_window, ''.join(line), (10, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0), 2)

    cv2.imshow("Hand Tracking Keyboard", frame)
    cv2.imshow("Typed Text", typed_window)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
