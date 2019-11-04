import cv2, PIL
import numpy as np
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import aruco_utils

video_source = 0

cap = cv2.VideoCapture(video_source)

im_width, im_height = (cap.get(3), cap.get(4))

ret = True

while ret:
    ret, frame = cap.read()

    corners, ids = aruco_utils.detect_markers(frame)

    cv2.imshow("original image", frame)
    cv2.waitKey(1)
    if len(corners) > 0:
        pick_one=0
        homography = aruco_utils.compute_projectivity(corners[pick_one][0])

        dewarped = cv2.warpPerspective(frame, homography, (frame.shape[1], frame.shape[0]))

        cv2.imshow("dewarped image", dewarped)
        cv2.waitKey(1)



