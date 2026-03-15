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

def frame_upscale(path: str, fin_path: str):
    frames = Path(path)
    path_len = len(path) + 1
    i = 0
    for frame in frames.iterdir():
        img1 = plt.imread(frame)
        name = str(frame)[path_len::]

        row, col = img1.shape[:2]
        row, col = int(row), int(col)

        img2 = np.empty((row*2, col*2, 3))

        row = 10
        col = 10

        print(f"divided by 510")
        for r in range(row):
            for c in range(col):
                print(f"Row #{r} and Col #{c}")
                # #first top box
                print("first top box")
                print(f"{img1[r,c,0]} /510 = {img1[r,c,0] /255}")
                print(f"{img1[r,c,1]} /510 = {img1[r,c,0] /255}")
                print(f"{img1[r,c,2]} /510 = {img1[r,c,0] /255}")
                img2[2*r,2*c,0] = img1[r,c,0] /255
                img2[2*r,2*c,1] = img1[r,c,1] /255
                img2[2*r,2*c,2] = img1[r,c,2] /255
                
                c1 = c+1 if c+1 < col else c
                r1 = r+1 if r+1 < row else r
                #second top box
                print("second top box")
                print(f"{img1[r,c,0]} + {img1[r,c1,0]} /510 = {(img1[r,c,0] + img1[r,c1,0]) / 510}")
                print(f"{img1[r,c,1]} + {img1[r,c1,1]} /510 = {(img1[r,c,1] + img1[r,c1,1]) / 510}")
                print(f"{img1[r,c,2]} + {img1[r,c1,2]} /510 = {(img1[r,c,2] + img1[r,c1,2]) / 510}")
                img2[2*r,2*c+1,0] = (img1[r,c,0] + img1[r,c1,0]) / 510
                img2[2*r,2*c+1,1] = (img1[r,c,1] + img1[r,c1,1]) / 510
                img2[2*r,2*c+1,2] = (img1[r,c,2] + img1[r,c1,2]) / 510
                if r == 0 and c == 0:
                    act = (87+177) /510
                    print(f"SPECIAL {img2[2*r,2*c+1,2]} vs {act}")
                
                #first bottom box
                print("first bottom box")
                print(f"{img1[r,c,0]} + {img1[r1,c,0]} /510 = {(img1[r,c,0] + img1[r1,c,0]) / 510}") 
                print(f"{img1[r,c,1]} + {img1[r1,c,1]} /510 = {(img1[r,c,1] + img1[r1,c,1]) / 510}")
                print(f"{img1[r,c,2]} + {img1[r1,c,2]} /510 = {(img1[r,c,2] + img1[r1,c,2]) / 510}")
                img2[2*r+1,2*c,0] = (img1[r,c,0] + img1[r1,c,0]) / 510
                img2[2*r+1,2*c,1] = (img1[r,c,1] + img1[r1,c,1]) / 510
                img2[2*r+1,2*c,2] = (img1[r,c,2] + img1[r1,c,2]) / 510
                
                #second bottom box
                print("second bottom box")
                print(f"{img1[r,c,0]} + {img1[r1,c1,0]} / 510 = {(img1[r1,c1,0] + img2[2*r,2*c+1,0]) / 510}")
                print(f"{img1[r,c,1]} + {img1[r1,c1,1]} / 510 = {(img1[r1,c1,1] + img2[2*r,2*c+1,1]) / 510}")
                print(f"{img1[r,c,2]} + {img1[r1,c1,2]} / 510 = {(img1[r1,c1,2] + img2[2*r,2*c+1,2]) / 510}")
                img2[2*r+1,2*c+1,0] = (img1[r1,c1,0] + img2[2*r,2*c+1,0]) / 510
                img2[2*r+1,2*c+1,1] = (img1[r1,c1,1] + img2[2*r,2*c+1,1]) / 510
                img2[2*r+1,2*c+1,2] = (img1[r1,c1,2] + img2[2*r,2*c+1,2]) / 510

                # print(f"Row {r} and Col {c}")
                # print(f"{img2[2*r,2*c]} {img2[2*r,2*c+1]} {img2[2*r+1,2*c]} {img2[2*r+1,2*c+1]}")

        file = fin_path + "frame-new.jpg"
        plt.imsave(file, img2)
        i += 1
        if i == 1:
            break
    
    return

# fin_path = "/Users/mane/Desktop/upscaling project/clips_new/"

# #selecting clip
# path = "/Users/mane/Desktop/upscaling project/clips/"
# path_len = len(path)

# print(f"Enter your choice for the clip you want to upscale: ")
# clip = parse(path)
# print(f"clip choosen is {clip}")

# fin_path = fin_path + clip[path_len::] + '/'
# if os.path.exists(fin_path):
#     print(f"final path {fin_path} already exists")
# else:
#     subprocess.call(['mkdir', fin_path])

# #selecting catogery of clip
# path = clip + '/'
# path_len = len(path)
# print(f"\nEnter your choice for the catogery of clip you want to upscale: ")
# cat = parse(path)
# print(f"catagoery choosen is {cat}")

# fin_path = fin_path + cat[path_len::] + '/'
# if os.path.exists(fin_path):
#     print(f"final path {fin_path} already exists")
# else:
#     subprocess.call(['mkdir', fin_path])

# frame_upscale(cat,fin_path)

cat = "clips_new/trio/lifetime/"
fin_path = "/Users/mane/Desktop/upscaling project/"
frame_upscale(cat,fin_path)
