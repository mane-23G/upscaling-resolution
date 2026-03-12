import matplotlib.pyplot as plt  # type: ignore
import numpy as np # type: ignore
import subprocess
from pathlib import Path
import os 

def parse(path: str) -> str:
    dir = Path(path)
    dir_len = len(path)
    dir_list = []
    i = 0

    for sub_dir in dir.iterdir():
        sub_dir = str(sub_dir)
        print(f"{i}. {sub_dir[dir_len::]}")
        i += 1
        dir_list.append(sub_dir)

    choice = int(input("\nEnter your choice: "))

    while choice < 0 or choice >= i:
        choice = int(input("Enter valid number: "))
    
    res = dir_list[choice]
    return res


#selecting clip
path = "/Users/mane/Desktop/upscaling project/clips/"
print(f"Enter your choice for the clip you want to upscale: ")
clip = parse(path)
print(f"clip choosen is {clip}")

#selecting catogery of clip
path = clip + '/'
print(f"Enter your choice for the catogery of clip you want to upscale: ")
cat = parse(path)
print(f"catagoery choosen is {cat}")

# lst = os.listdir(clip)


# frames = Path()

#subprocess.call()  