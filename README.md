## ArUco Orientation

This is a simple project to use ArUco targets to determine a camera orientation relative to a planar surface. It begins with the sample code from [this website](https://mecaruco2.readthedocs.io/en/latest/notebooks_rst/Aruco/aruco_basics.html).

Paul Barsic  
November 2019

## Requirements:  
Linux with a basic Python installation. These instructions use Python 2, but they should not be har dto modify for Python 3.

To use this, you will need a few packages.

First, some system-wide packages:  
'sudo apt update'  
'sudo apt upgrade'  
'sudo apt install python-opencv python-tk'

Next, some nice Python packages:  
`pip install scipy`  
`pip install numpy`  
`pip install Pillow`  
`pip install matplotlib`  
`pip install pandas`


`draw_markers.py`
Python script to generate an ArUco target

`display_detected_markers.py`
Python script to display detected ArUco targets in an image

`reproject_squares.py`
Python script to detect an ArUco target in an image and then rectify the image so that the target is rectangular.

`reproject_video.py`
Python script to use the system camera as an input, look for ArUco targets, and then rectify the image so that the target is rectangular before displaying.

`aruco_utils.py`
Utilities for computing the homography that is used in the reproject scripts
