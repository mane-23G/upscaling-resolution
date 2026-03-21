#! /bin/bash

filename=$1

dest=$2

# cd clips_new/intro/lifetime/
# ffmpeg -i $file -vf fps=29.97/1 $dest"frame-%06d.jpg"



# ffmpeg -framerate 29.97 -start-number 1 -i $filename"frame-%06d.jpg" -c:v prores_ks -profile:v 3 -pix_fmt yuva444p10le $dest"dms1e1(lifetime)v2.mkv"
# ffmpeg -framerate 29.97 -i output.txt -c:v prores_ks -profile:v 3 -pix_fmt yuva444p10le $dest"dms1e1(lifetime)v2.mkv"
ffmpeg -f concat -safe 0 -i output.txt -vf "fps=29.97" -c:v prores_ks -profile:v 3 -pix_fmt yuva444p10le "videos_new/dms1e1(lifetime).mkv"
