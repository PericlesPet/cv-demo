#!/bin/bash


# Run YOLO MARK on initial labels for some images
cp Label\ Conversion/labels/* Label\ Conversion/imgs/
cd Yolo_mark
./yolo_mark ../Label\ Conversion/imgs x64/Release/data/train.txt ../darknet/data/FSCones.names

