import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1, detectionCon=0.8)
keyboard = Controller()

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)

        # Check if the index finger is open
        if fingers[1] == 1:
            # Simulate a press of the 'Space' key
            keyboard.press(Key.space)
            keyboard.release(Key.space)

            cv2.putText(img, "Index Finger opened - dinosaur UP", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            #print("Index Finger Closed")
            pass

        #print(f'Fingers: {fingers}')

    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv2.destroyAllWindows()
