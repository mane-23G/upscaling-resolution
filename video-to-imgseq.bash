#! /bin/bash

filename="dms1e1(dvd)"
file="videos/dms1e1(dvd).mkv"
mkdir image_sequences/$filename

dest="image_sequences/$filename/"

ffmpeg -i $file -vf fps=29.97/1 $dest"frame-%06d.jpg"

