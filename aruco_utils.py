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
    # find the lower-left corner (greatest y-value and least x-value), this will be [0, 0, 1]
    lower_left = [ c for c in corners if c[0] < corners[:,0].mean() and c[1] > corners[:,1].mean() ][0]
    # find the lower-right corner (greatest y-value and greatest x-value) this will be [1, 0, 1]
    lower_right = [ c for c in corners if c[0] > corners[:,0].mean() and c[1] > corners[:,1].mean() ][0]
    # find the upper-left corner (least y-value and least x-value), this will be [0, 1, 1]
    upper_left = [ c for c in corners if c[0] < corners[:,0].mean() and c[1] < corners[:,1].mean() ][0]
    # find the upper-right corner (least y-value and greatest x-value), this will be [1, 1, 1]
    upper_right = [ c for c in corners if c[0] > corners[:,0].mean() and c[1] < corners[:,1].mean() ][0]

    ordered_corners = np.array([ lower_left, lower_right, upper_left, upper_right ])
    # figure out an appropriate sacle for the ordered corners.
    scale = lower_right[0] - lower_left[0]
    desired_corners = np.array([ lower_left, lower_left+[scale, 0.0], lower_left + [0, -scale], lower_left+[scale, -scale] ])

    h, status = cv2.findHomography(ordered_corners, desired_corners)
    return h

