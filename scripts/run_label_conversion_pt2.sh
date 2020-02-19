#!/bin/bash


# Convert the labels
cd Label\ Conversion/
python classParser.py labels 3 1 0 2
cp label_converted/* imgs/

# Run YOLO MARK on new labels for the same images
cd ../Yolo_mark
cmake .
make
./yolo_mark ../Label\ Conversion/imgs x64/Release/data/train.txt ../darknet/data/FSCones.names
