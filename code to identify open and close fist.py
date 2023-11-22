import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Open a video capture stream (you can also use a webcam or video file)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        continue

    # Convert the frame to RGB for processing
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Use MediaPipe to detect hands in the frame
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Calculate the distance between thumb tip and index finger tip
            thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            distance = cv2.norm(
                (int(thumb_tip.x * frame.shape[1]), int(thumb_tip.y * frame.shape[0])),
                (int(index_tip.x * frame.shape[1]), int(index_tip.y * frame.shape[0]))
            )

            # Define a threshold to determine open or closed fist
            threshold = 0.04  # Adjust this value according to your preference

            # Check if the hand is open or closed based on the distance
            if distance < threshold:
                cv2.putText(frame, "Open Fist", (500, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                cv2.putText(frame, "Closed Fist", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Draw landmarks on the hand
            mp_drawing = mp.solutions.drawing_utils
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow('Hand Gesture Detection', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()



'''
import cv2
import mediapipe as mp
import time
import math

class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode= mode
        self.maxHands= maxHands
        self.detectionCon= detectionCon
        self.trackCon= trackCon

        self.mpHands= mp.solutions.Hands
        self.Hands= self.mpHands.Hands(self.mode,self.maxHands,
        self.detectionCon, self.trackCon)
        self.mpdraw= mp.solutions.drawing_utils
        self.tipIds= [4,8,12,16,20]

def findHands(self, img, draw=True):
    imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    self.results = self.hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if self.results.multi_hand_landmarks:
        for handLms in self.results.multi_hand_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, handLms,self.mpHands.HAND_CONNECTIONS)
                return img

def findPosition(self, img, handNo=0, draw=True):
    xList = []
    yList = []
    bbox = []
    self.lmList= []
    if self.results.multi_hand_landmarks:
        myHand= self.results.multi_hand_landmarks[handNo]
        for id, lm in enumerate[myHand.landmark]:
            #print(id,lm)
            h, w, c = img.shape
            cx, cy = int[lm.x*w], int[lm.y*h]
            xList.append(cx)
            yList.append(cy)
            #print(id, cx, cy)
            self.lmList.append([id, cx, cy])
            if draw:
                cv2.circle(img, (cx, cy), 5, (225,0,225), cv2.FILLED)
        xmin, xmax = min(xList), max(xList)
        ymin, ymax = min(yList), max(yList)
        bbox= xmin, ymin, xmax, ymax

        if draw:
            cv2.rectangle(img, (bbox[0]-20, bbox[1]-20),
        (bbox[2]+20, bbox[3]+20), (0, 255, 0), 2)
        return self.lmList, bbox

def fingersUp(self):
    fingers = []
    #THUMB
    if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0]-1][1]:
        fingers.append(1)
    else:
        fingers.append(0)
    #4fingers
    for id in range(1, 5):
        if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id]-2][2]:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

def findDistance(self, p1, p2, img, draw=True):

    x1, y1 = self.lmList[p1][1], self.lmList[p1][2]
    x2, y2 = self.lmList[p2][1], self.lmList[p2][2]
    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

    if draw:
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

    length= math.hypot(x2-x1,y2-y1)
    return length, img, [x1, y1, x2, y2, cx, cy]
''' 