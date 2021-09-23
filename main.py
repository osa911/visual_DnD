import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
# import numpy as np
from utils.screen import get_coords
from components.rectangle import DragRect

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = HandDetector(detectionCon=0.8)

success, img = cap.read()
colorR = (0, 0, 255)
cx, cy, w, h = 100, 100, 200, 200

rectList = []
for x in range(5):
    rectList.append(DragRect([x * 250 + 150, 150]))

while True:
    success2, img = cap.read()
    img = cv2.flip(img, 1)
    hands = detector.findHands(img, False)

    if hands:
        hand1 = hands[0]
        lmList = hand1["lmList"]
        l, _, = detector.findDistance(lmList[4], lmList[8])
        if l < 50:
            cursor = lmList[8]  # index finger tip landmark
            for rect in rectList:
                rect.update(cursor)

    ## Draw solid rectangle
    for rect in rectList:
        cx1, cy1, cx2, cy2 = get_coords(rect.centerPosition, rect.size)
        cv2.rectangle(img, (cx1, cy1), (cx2, cy2), colorR, cv2.FILLED)
        cvzone.cornerRect(img, (cx1, cy1, rect.size[0], rect.size[1]), 20, rt=0)
    cv2.imshow("Image", img)

    ## Draw transparency rectangle
    # imgNew = np.zeros_like(img, np.uint8)
    # for rect in rectList:
    #     cx1, cy1, cx2, cy2 = get_coords(rect.centerPosition, rect.size)
    #     cv2.rectangle(imgNew, (cx1, cy1), (cx2, cy2), colorR, cv2.FILLED)
    #     cvzone.cornerRect(imgNew, (cx1, cy1, rect.size[0], rect.size[1]), 20, rt=0)
    # out = img.copy()
    # alpha = 0.5
    # mask = imgNew.astype(bool)
    # # print(mask.shape)
    # out[mask] = cv2.addWeighted(img, alpha, imgNew, 1 - alpha, 0)[mask]
    # cv2.imshow("Image", out)

    cv2.waitKey(1)
