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


