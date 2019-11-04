import cv2, PIL
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl

frame = cv2.imread("_data/aruco_picture_2x4.jpg")

frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
#plt.figure()
#plt.imshow(frame_bgr)
#plt.show()

gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters_create()
corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
frame_markers = aruco.drawDetectedMarkers(frame_bgr.copy(), corners, ids)

plt.figure()
plt.imshow(frame_markers)
for i in range(len(ids)):
    c = corners[i][0]
    plt.plot([c[:, 0].mean()], [c[:, 1].mean()], "o", label = "id={0}".format(ids[i]))
plt.legend()
plt.show()

