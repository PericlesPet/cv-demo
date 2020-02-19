# generateMap.py
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
# import IPM_helper as helper
import time
import os
# P A R A M E T E R S  ---------------------------------------------------------

IMAGE_H = 720
IMAGE_W = 1280
WARPED_IMG_H = 2000
WARPED_IMG_W = 2000

Fx = 100
Fy = 100

cone_x_dist = 2  #bottom and top cones are 2m apart on the x axis
cone_y_dist = 6  #bottom cones are 6m ahead of the top ones on the y axis

img_path = 'mats/1.jpg'
# src = np.float32([[471, 170], [819, 170], [1263, 568], [52, 568]])   #1M - 30D - T5

# img_path = 'mats/x05-y0-d15.jpg'
# src = np.float32([[553, 290] , [737, 290] , [1240, 589], [107 , 589]])       #(0.5, 0)M - 15D - T5 AUGMENTED


# P A R A M E T E R S  E N D ---------------------------------------------------------


img = cv2.imread(img_path) # Read the test img

f1 = plt.figure()

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # Show results    

plt.show(block=True)

# load points from annotation .txt

# dst = np.float32([[WARPED_IMG_W/2, WARPED_IMG_H-cone_y_dist*Fy], [WARPED_IMG_W/2+cone_x_dist*Fx,  WARPED_IMG_H-cone_y_dist*Fy], [WARPED_IMG_W/2+cone_x_dist*Fx, WARPED_IMG_H], [WARPED_IMG_W/2, WARPED_IMG_H]])   #(0.5, 0)M - 15D - T5 AUGMENTED
# yolo_path = os.path.splitext(img_path)[0]+'.txt'  
# cones_no, p = helper.pts_func(IMAGE_W, IMAGE_H, yolo_path)


# # GET IMAGE TRANSFORM MATRICES
# M = cv2.getPerspectiveTransform(src, dst) # The transformation matrix
# Minv = cv2.getPerspectiveTransform(dst, src) # Inverse transformation

# # GET FIGURE OF INITIAL IMAGE WITH PTS
# f1 = plt.figure()
# helper.annotate(img, src, f1, 'green')
# helper.annotate(img, p, f1, 'red')

# # TRANSFORM IMAGE AND POINTS TO BEV
# src_trans = cv2.perspectiveTransform(np.array([src]), M)
# p_trans = cv2.perspectiveTransform(np.array([p]), M)
# warped_img = cv2.warpPerspective(img, M, (WARPED_IMG_W, WARPED_IMG_H)) # Image warping

# # PLOT IMAGE + POINTS
# f2 = plt.figure()
# helper.annotate(warped_img, src_trans[0], f2, 'green')
# helper.annotate(warped_img, p_trans[0], f2, 'red')
# plt.show(block=True)

# save_path_M = os.path.splitext(img_path)[0]+'-M.csv'
# np.savetxt(save_path_M,M, fmt='%.7e',header='Birds Eye View transform matrix')
# np.savetxt("mats/Minv.csv",Minv, fmt='%.7e',header='Birds Eye View inverse transform matrix')
# # M2 = np.genfromtxt("M.csv")

