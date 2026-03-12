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

fin_path = "clips_new/"

#selecting clip
path = "clips/"
path_len = len(path)

print(f"Enter your choice for the clip you want to upscale: ")
clip = parse(path)
print(f"clip choosen is {clip}")

fin_path = fin_path + clip[path_len::] + '/'
if os.path.exists(fin_path):
    print(f"final path {fin_path} already exists")
else:
    subprocess.call(['mkdir', fin_path])

#selecting catogery of clip
path = clip + '/'
path_len = len(path)
print(f"\nEnter your choice for the catogery of clip you want to upscale: ")
cat = parse(path)
print(f"catagoery choosen is {cat}")

fin_path = fin_path + cat[path_len::]
if os.path.exists(fin_path):
    print(f"final path {fin_path} already exists")
else:
    subprocess.call(['mkdir', fin_path])



