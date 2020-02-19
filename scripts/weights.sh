#!/bin/bash


# Place custom weights in darknet 
cd darknet/
mkdir -p custom-weights
mv ../yolov3-tiny-FSCones_30000.weights custom-weights/

