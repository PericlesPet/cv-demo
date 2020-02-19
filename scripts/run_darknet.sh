#!/bin/bash

cd darknet
mkdir -p build-release
cd build-release
cmake ..
make
make install

pwd
cd ..
pwd
./darknet detector train data/FSCones.data custom_cfgs/yolov3-tiny-FSCones.cfg custom-weights/yolov3-tiny-FSCones_30000.weights 
