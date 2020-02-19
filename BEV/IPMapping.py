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


def IPMap():

    # P A R A M E T E R S --------------------------------------------------------
    IMAGE_H = 720
    IMAGE_W = 1280
    WARPED_IMG_H = 2000
    WARPED_IMG_W = 2000
    ycrop = 55
    plot = 1

    # img_path = 'mats/1m-30d-t5.jpg'
    img_path = 'mats/x05-y0-d15.jpg'
    coneRadius = 0.114              # 114 mm to meters
    Fx = 100.0
    Fy = 100.0
    xDisp = 1
    yDisp = 1
    ref_point = np.float32([[0,0]])
    # P A R A M E T E R S  E N D ------------------------------------------------

    start = time.time()        #TIME
    yolo_path = os.path.splitext(img_path)[0]+'.txt'
    cones_no, p , classes = helper.bbox2points(IMAGE_W, IMAGE_H, yolo_path) #get points in pixels

    # GET IMAGE TRANSFORM MATRICES
    map_path = os.path.splitext(img_path)[0]+'-M.csv'
    M = np.genfromtxt(map_path)
    # print(M)


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
    all_p = np.hstack((classes, p_trans_m))


    all_p = np.append(all_p, (1, 0.0, 5.0))
    # CALCULATE ELAPSED TIME
    end = time.time()          #TIME 
    elapsed = end-start       #TIME
    print("time elapsed: %f\n"%(elapsed)) #TIME
    return all_p


if __name__ == "__main__":
    print("from main func") 
    IPMap()