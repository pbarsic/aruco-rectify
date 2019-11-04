import cv2, PIL
import numpy as np
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import aruco_utils


frame = cv2.imread("_data/aruco_picture_2x4.jpg")

frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

corners, ids = aruco_utils.detect_markers(frame_bgr)

pick_one=0
print ids[pick_one]
homography = aruco_utils.compute_projectivity(corners[pick_one][0])

dewarped = cv2.warpPerspective(frame, homography, (frame.shape[1], frame.shape[0]))

cv2.imshow("original image", frame)
cv2.imshow("dewarped image", dewarped)
cv2.waitKey(0)



