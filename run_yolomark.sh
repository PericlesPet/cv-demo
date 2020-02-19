#!/bin/bash

cd darknet/
./darknet detector test data/FSCones-yolomark.data custom_cfgs/yolov3-tiny-FSCones.cfg custom-weights/yolov3-tiny-FSCones_30000.weights -dont_show -save_labels < data/yolomark-test.txt

# Check with yolo_mark:

cd ../Yolo_mark
cmake .
make
./yolo_mark ../darknet/data/yolomark-test/ x64/Release/data/train.txt ../darknet/data/FSCones.names
