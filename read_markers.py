import cv2, PIL
import numpy as np
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd

def quad_area(data):
    l = data.shape[0]//2
    corners = data[["c0", "c1", "c2", "c3"]].values.reshape(l, 2, 4)
    c0 = corners[:, :, 0]
    c1 = corners[:, :, 1]
    c2 = corners[:, :, 2]
    c3 = corners[:, :, 3]
    e0 = c1 - c0
    e1 = c2 - c1
    e2 = c3 - c2
    e3 = c0 - c3
    a = -0.5 * (np.cross(-e0, e1, axis = 1) + np.cross(-e2, e3, axis=1))
    return a

frame = cv2.imread("_data/aruco_picture_2x4.jpg")

frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

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

corners2 = np.array([c[0] for c in corners])

data = pd.DataFrame({"x": corners2[:, :, 0].flatten(), "y": corners2[:, :, 1].flatten()},
        index = pd.MultiIndex.from_product(
            [ids.flatten(), ["c{0}".format(i) for i in np.arange(4)]], names = ["marker", ""]))

data = data.unstack().swaplevel(0, 1, axis = 1).stack()
data["m0"] = data[["c0", "c1"]].mean(axis = 1)
data["m1"] = data[["c1", "c2"]].mean(axis = 1)
data["m2"] = data[["c2", "c3"]].mean(axis = 1)
data["m3"] = data[["c3", "c0"]].mean(axis = 1)
data["o"] = data[["m0", "m1", "m2", "m3"]].mean(axis=1)
print data

