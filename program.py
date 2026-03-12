import matplotlib.pyplot as plt  # type: ignore
import numpy as np # type: ignore
import subprocess
from pathlib import Path
import os 


path = "/Users/mane/Desktop/upscaling project/clips/"
clips = Path(path)
clip_dir = []
i = 0
path_len = len(path)

print("Enter the number corresponding to the clip you want to upscale:")
for clip in clips.iterdir():
    c = str(clip)[path_len::]
    print(f"{i}. {c}")
    i += 1
    clip_dir.append(clip)

choice = int(input("Number: "))

while choice < 0 or choice > i:
    choice = int(input("Enter a valid num pls: "))

clip = clip_dir[choice]
print(f"selected clip path is: {clip}\n")

types = Path(clip)
type_dir = []
i = 0
types_len = len(str(types)) + 1
print("Enter the number corresponding to the type of clip you want to upscale:")
for type in types.iterdir():
    t = str(type)[types_len::]
    print(f"{i}. {t}")
    i += 1
    type_dir.append(type)

choice = int(input("Number: "))

while choice < 0 or choice > i:
    choice = int(input("Enter a valid num pls: "))

type = type_dir[choice]
print(f"selected clip is {type}\n")

# lst = os.listdir(clip)


# frames = Path()

#subprocess.call()  