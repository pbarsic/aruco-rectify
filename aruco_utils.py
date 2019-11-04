import cv2
import numpy as np
from cv2 import aruco

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


def detect_markers(frame_bgr, aruco_dict = aruco.DICT_6X6_250):
    gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco_dict)
    parameters = aruco.DetectorParameters_create()
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    return corners, ids

def compute_projectivity(corners):
    print corners

