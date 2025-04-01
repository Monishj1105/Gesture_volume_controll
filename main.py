import cv2
import mediapipe as mp
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
import numpy as np

# Initialize MediaPipe Hand Detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Initialize Pycaw for Volume Control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# Function to calculate distance between two points
def distance(point1, point2):
    return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Video Capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw Hand Landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get landmarks for index finger (8) and thumb (4)
            index_finger = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]

            # Convert normalized coordinates to pixel values
            h, w, _ = frame.shape
            index_coords = (int(index_finger.x * w), int(index_finger.y * h))
            thumb_coords = (int(thumb_tip.x * w), int(thumb_tip.y * h))

            # Draw circles on the fingers
            cv2.circle(frame, index_coords, 5, (0, 255, 0), -1)
            cv2.circle(frame, thumb_coords, 5, (0, 0, 255), -1)

            # Calculate distance to control volume
            dist = distance(index_coords, thumb_coords)
            vol = np.interp(dist, [20, 200], [0.0, 1.0])  # Adjust thresholds as needed
            volume.SetMasterVolumeLevelScalar(vol, None)

            # Display volume level
            cv2.putText(frame, f"Volume: {int(vol * 100)}%", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display the frame
    cv2.imshow('Hand Gesture Volume Control', frame)

    # Break on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
