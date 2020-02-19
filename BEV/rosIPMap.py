# IPMapping.py
# READS
# a projective transformation matrix M (map),
# the bounding boxes from the annotation .txt
# 
# PERFORMS
# calculate pixel coordinates of cones based on their BBoxes
# map pixel coordinates to meter coordinates (x,y) in front of vehicle
# 
# RETURNS
# an array with classes,x,y of cones in meters 

import cv2
import numpy as np
import matplotlib.pyplot as plt
import IPM_helper as helper
import time
import os

# ROS RELATED LIBS
import rospy
from sensor_msgs.msg import Image
from darknet_ros_msgs.msg import BoundingBoxes
from darknet_ros_msgs.msg import ObjectCount
from std_msgs.msg import Header
from std_msgs.msg import String



def IPMap(IMAGE_H, IMAGE_W, BoundingBoxes, ObjectCount):

    # P A R A M E T E R S --------------------------------------------------------
    WARPED_IMG_H = 2000
    WARPED_IMG_W = 2000
    
    # IMAGE_H = 720 (default)
    # IMAGE_W = 1280 (default)

    img_path = 'mats/x05-y0-d15.jpg'

    coneRadius = 0.114              # 114 mm to meters
    Fx = 100.0
    Fy = 100.0
    xDisp = 1
    yDisp = 1
    ref_point = np.float32([[0,0]])
 
    plot = 0 # SWITCH TO 1 IF YOU WANNA PLOT HOW THE TRANSFORMATION WORKS

    # P A R A M E T E R S  E N D ------------------------------------------------

    cones_no, p , classes = helper.ros_bbox2points(IMAGE_W, IMAGE_H, BoundingBoxes, ObjectCount) #get points in pixels

    # GET IMAGE TRANSFORM MATRICES
    map_path = os.path.splitext(img_path)[0]+'-M.csv'
    M = np.genfromtxt(map_path)



    # TRANSFORM IMAGE AND POINTS TO BEV
    p_trans = cv2.perspectiveTransform(np.array([p]), M)

    # TRANSFORM PIXELS TO ROAD COORDINATES
    [p_trans_m, p_trans_wo] = helper.px_to_meters(p_trans[0], WARPED_IMG_W, WARPED_IMG_H, Fx, Fy, xDisp, yDisp, coneRadius)


    # PLOT STUFF
    if(plot):
        img = cv2.imread(img_path) # Read the test img
        warped_img = cv2.warpPerspective(img, M, (WARPED_IMG_H, WARPED_IMG_W)) # Image warping
        f1 = plt.figure()
        helper.annotate(img, p, f1, 'red')

        f2 = plt.figure()
        helper.annotate(warped_img, p_trans[0], f2, 'red')

        f3 = plt.figure()
        # helper.annotate_m(warped_img, p_trans[0]+100, p_trans_m, f3, 'red')
        helper.annotate_m(warped_img, p_trans[0], p_trans_m, f3, 'red')
        plt.show(block=True)

    # MERGE CLASSES AND COORDINATES
    #all_p contains all points along with classes
    all_p = np.hstack((classes, p_trans_m)) 


    return all_p


if __name__ == "__main__":
    print("from main func") 

# SUBSCRIBE TO: 
# /darknet_ros/bounding_boxes
# /darknet_ros/object_count
# ------------------
#    missing code
# ------------------
#  ^ HERE

    IPMap(IMAGE_H, IMAGE_W, BoundingBoxes, ObjectCount)