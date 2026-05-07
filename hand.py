import cv2
import mediapipe as mp
import pyautogui
import time
import screen_brightness_control as sbc

pyautogui.FAILSAFE = False

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

last_action_time = 0
delay = 1.2


def count_fingers(hand_landmarks, hand_label):
    fingers = []

    # Thumb (left/right handling)
    if hand_label == "Right":
        fingers.append(1 if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x else 0)
    else:
        fingers.append(1 if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x else 0)

    tips = [8, 12, 16, 20]
    for tip in tips:
        fingers.append(1 if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y else 0)

    return sum(fingers)


while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    current_time = time.time()

    if results.multi_hand_landmarks:
        for idx, handLms in enumerate(results.multi_hand_landmarks):

            if results.multi_handedness:
                label = results.multi_handedness[idx].classification[0].label
            else:
                label = "Right"

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            finger_count = count_fingers(handLms, label)

            # Display info
            cv2.putText(img, f'Hand: {label}', (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            cv2.putText(img, f'Fingers: {finger_count}', (10, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            # ===== ACTIONS =====
            if current_time - last_action_time > delay:

                # 1 Finger → Volume Up
                if finger_count == 1:
                    pyautogui.press("volumeup")
                    print("Volume Up 🔊")

                # 2 Fingers → Volume Down
                elif finger_count == 2:
                    pyautogui.press("volumedown")
                    print("Volume Down 🔉")

                # 3 Fingers → Brightness Up
                elif finger_count == 3:
                    current_brightness = sbc.get_brightness()[0]
                    sbc.set_brightness(min(current_brightness + 10, 100))
                    print("Brightness Up 🌗")

                # 4 Fingers → Brightness Down
                elif finger_count == 4:
                    current_brightness = sbc.get_brightness()[0]
                    sbc.set_brightness(max(current_brightness - 10, 0))
                    print("Brightness Down 🌑")

                last_action_time = current_time

    cv2.imshow("Gesture Control (Volume + Brightness)", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()