# all kinds of stuff
# needs cleaning up
# order_points, show_figure, show_figure_m the first to go


import cv2
import numpy as np
import matplotlib.pyplot as plt
from imutils import paths
import imutils
from math import sqrt

def bbox2points(IM_WIDTH, IM_HEIGHT, yolo_path):
    # reads the annotation .txt file (yolo_path)
    # extracts the bounding box info for all objects in the image ( [class, x_center, y_center, w, h])
    # converts Bounding Box format to singular points
    # BBox: [x_center, y_center, w, h] -> Point [x, y] = [x_center, y_center-h/2]
    # returns:
    #  (int) number of cones N,
    #  (int[N, 2]) points of cones in pixels, 
    #  (int[N]) classes
    num_cones = sum(1 for line in open(yolo_path))
    cones = np.zeros((num_cones,5),dtype=float)
    pts = np.zeros((num_cones,2), dtype=float)
    classes = np.zeros((num_cones,1))
    cone_ins = 0
    
    for line in open(yolo_path):
        num_count = 0
        for nums in line.split():
            cones[cone_ins, num_count] = float(nums)
            num_count += 1

        cone_class = cones[cone_ins, 0]
        classes[cone_ins] = cone_class
        cones[cone_ins, 1] = cones[cone_ins, 1]*IM_WIDTH  #X
        cones[cone_ins, 2] = cones[cone_ins, 2]*IM_HEIGHT  #Y
        cones[cone_ins, 3] = cones[cone_ins, 3] * IM_WIDTH  #width
        cones[cone_ins, 4] = cones[cone_ins, 4] * IM_HEIGHT  #height

        # cones[cone_ins,5] = cones[cone_ins,4] / cones[cone_ins,3]
        
        pts[cone_ins, 0] = cones[cone_ins, 1]  # X
        pts[cone_ins, 1] = cones[cone_ins, 2]+cones[cone_ins, 4]/2  # Y-h/2

        # cone_center = (cones[cone_ins, 1]*IM_WIDTH,cones[cone_ins, 2]*IM_HEIGHT)  
        # cone_width = cones[cone_ins, 3] * IM_WIDTH
        # cone_height = cones[cone_ins, 4] * IM_HEIGHT
        cone_ins += 1
        
        
    return cone_ins, pts, classes
    


def darknetClass2index(className):
    # darknet ros doesnt index the classes.
    # instead, it gives you the classes directly as strings using the classes.txt you provided it with
    # so, this function maps to indices using the custom classnames (see aristurtle-classes.txt)
    index = -1
    if className == "small-orange":
        index = 0
    elif className == "blue-cone":
        index = 1
    elif className == "yellow-cone":
        index = 2
    elif className == "big-orange":
        index = 3


    return index


def ros_bbox2points(IM_WIDTH, IM_HEIGHT, BoundingBoxes, ObjectCount):
    # INPUT
    # darknet_ros_msgs boundingBoxes msg data
    # FUNCTIONALITY
    # extracts the bounding box info for all detected objects
    # converts DARKNET_ROS Bounding Box format to singular points
    # BBox: [Xmin, Xmax, Ymin, Ymax] -> Point [x, y] = [IMG_Width*(Xmin+Xmax)/2, IMG_Height*(Ymin+Ymax)/2] in absolute pixel coordinates
    # returns:
    #  (int) number of cones N,
    #  (int[N, 2]) points of cones in pixels, 0
    #  (int[N]) classes
    num_cones = ObjectCount.count
    
    cones = np.zeros((num_cones,5),dtype=float)
    
    pts = np.zeros((num_cones,2), dtype=float)
    classes = np.zeros((num_cones,1))
    cone_instance = 0
    
    for bbox in BoundingBoxes.bounding_boxes:
        #CALC X -> xmin + xmax / 2 
        x_c = (bbox.xmin + bbox.xmax)/2
        pts[cone_ins, 0] = x_c * IM_WIDTH
        # CALC Y -> ymax + ymin / 2
        y_c = (bbox.ymin + bbox.ymax)/2
        pts[cone_ins, 1] = y_c * IM_HEIGHT

        classes[cone_ins] = darknetClass2index(bbox.Class) 

        cone_instance += 1
        
        
    return cone_instance, pts, classes
    


def annotate(img, p, f, color):
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # Show results    
    i = 0
    for point in p:
        plt.annotate(str(p[i].astype(int)), xy=(p[i][0], p[i][1]), xycoords='data',
                    xytext=(-80, 10), textcoords='offset pixels',
                    arrowprops=dict(arrowstyle="->"))
        plt.scatter(p[i][0], p[i][1], s=15, c=color, marker='o')
        i+=1
    return f


def annotate_m(img, p, p_m, f, color):
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) # Show results    
    i = 0
    for point in p:

        annotated_x = p_m[i][0]
        annotated_y = p_m[i][1]
        
        # plt.annotate(str(p[i].astype(int)), xy=(p[i][0], p[i][1]), xycoords='data',
        # plt.annotate(f"({annotated_x:.2f},{annotated_y:.2f})", xy=(p[i][0], p[i][1]), xycoords='data',
        plt.annotate("(%.2f, %.2f)"%(annotated_x,annotated_y), xy=(p[i][0], p[i][1]), xycoords='data',
                    xytext=(-80, 10), textcoords='offset pixels',
                    arrowprops=dict(arrowstyle="->"))
        plt.scatter(p[i][0], p[i][1], s=15, c=color, marker='o')
        i+=1
    return f


def offset_xy(point_m, Fx, Fy, coneRadius):

    offset = np.zeros(point_m.shape, dtype=float)

    tan_theta = abs(point_m[1] / point_m[0])
    
    xoff = sqrt((coneRadius**2)/(1+tan_theta**2))
    yoff = tan_theta * xoff

    sign_x = np.sign(point_m[0])

    offset[0] = xoff * sign_x
    offset[1] = yoff

    return offset


# convert pixel coordinates to (x,y)
def px_to_meters(points_px, IMG_W, IMG_H, Fx, Fy, xDisp, yDisp, coneRadius):
    


    points_m = np.zeros(points_px.shape, dtype = float)
    
    points_m[:,0] = (points_px[:,0]-IMG_W/2 ) / Fx
    points_m[:,1] = (IMG_H - points_px[:,1]) / Fy 

    points_m += [-xDisp, yDisp]

    points_wo = np.copy(points_m)
    for i in range(points_m.shape[0]):
        points_m[i] += offset_xy(points_m[i], Fx, Fy, coneRadius)
        
        
    return points_m, points_wo




if __name__ == "__main__":
    print("from main func") 
    default_IM_H = 720
    default_IM_W = 1280
    default_path = "mats/1m-30d-t5.txt"
    bbox2points(default_IM_W, default_IM_H,default_path)