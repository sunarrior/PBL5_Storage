# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 21:02:46 2022

@author: ASUS
"""

import cv2
import urllib.request
import numpy as np

# cap = cv2.VideoCapture(0)

# while True:
#     success, img = cap.read()
    
#     cv2.imshow("img", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
    
# cap.release()
# cv2.destroyAllWindows()

frame = None

while True:
    imgRes = urllib.request.urlopen('http://192.168.0.107/capture?')
    imgNp = np.array(bytearray(imgRes.read()), dtype=np.uint8)
    frame = cv2.imdecode(imgNp, -1)
    frame = cv2.resize(frame, (640, 480))
    cv2.imshow("Capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
    