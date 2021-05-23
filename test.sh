#!/usr/bin/bash

# Runs solver on all files in examples folder
for file in examples/*.txt
do
    echo $file
    ./solver.py $file
done