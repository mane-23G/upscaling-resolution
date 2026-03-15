import matplotlib.pyplot as plt  # type: ignore
import numpy as np # type: ignore

# img1 = np.zeros((3, 3, 3))


# img1[0,0,0] = 1
# img1[0,1,0] = 0.6
# img1[0,2,0] = 0.3

# img1[1,0,0] = 1
# img1[1,1,0] = 0.6
# img1[1,2,0] = 0.3

# img1[1,0,1] = 110/255
# img1[1,1,1] = 70/255
# img1[1,2,1] = 20/255

# img1[1,0,2] = 191/255
# img1[1,1,2] = 140/255
# img1[1,2,2] = 90/255

# img1[2,0,2] = 1
# img1[2,1,2] = 0.6
# img1[2,2,2] = 0.3


# plt.imsave("rgb4.png",img1)
img1 = plt.imread("rgb.png")



img2 = np.zeros((5,5,3))

for r in range(3):
    for c in range(3):
        print("first top box")
        print(f"{img1[r,c,0]}")
        print(f"{img1[r,c,1]}")
        print(f"{img1[r,c,2]}")

        img2[2*r,2*c,0] = img1[r,c,0]
        img2[2*r,2*c,1] = img1[r,c,1]
        img2[2*r,2*c,2] = img1[r,c,2]
        c1 = c if c == 2 else c+1

        
        if 2*c +1 < 5:
            print("second top box")
            print(f"{img1[r,c,0]} and {img1[r,c1,0]}")
            print(f"{img1[r,c,1]} and {img1[r,c1,1]}")
            print(f"{img1[r,c,2]} and {img1[r,c1,2]}")
            img2[2*r,2*c+1,0] = (img1[r,c,0] + img1[r,c1,0]) / 2
            img2[2*r,2*c+1,1] = (img1[r,c,1] + img1[r,c1,1]) / 2
            img2[2*r,2*c+1,2] = (img1[r,c,2] + img1[r,c1,2]) / 2
        # img2[2*r,2*c+1,0] =  img1[r,c,0] + img1[r,c1,0]
        # img2[2*r,2*c+1,1] =  img1[r,c,1] + img1[r,c1,1]
        # img2[2*r,2*c+1,2] =  img1[r,c,2] + img1[r,c1,2]

       
        r1 = r if r == 2 else r+1
        if 2*r +1 < 5:
            print("first bottom box")
            print(f"{img1[r,c,0]} and {img1[r1,c,0]}") 
            print(f"{img1[r,c,1]} and {img1[r1,c,1]}")
            print(f"{img1[r,c,2]} and {img1[r1,c,2]}")

            img2[2*r+1,2*c,0] = (img1[r,c,0] + img1[r1,c,0]) /2
            img2[2*r+1,2*c,1] = (img1[r,c,1] + img1[r1,c,1]) /2
            img2[2*r+1,2*c,2] = (img1[r,c,2] + img1[r1,c,2]) /2

        if 2*r +1 < 5 and 2*c +1 < 5:
            print("second bottom box")
            print(f"{img1[r,c,0]} and {img1[r1,c1,0]}")
            print(f"{img1[r,c,1]} and {img1[r1,c1,1]}")
            print(f"{img1[r,c,2]} and {img1[r1,c1,2]}")

            # img2[2*r+1,2*c+1,0] = (img2[2*r,2*c+1,0] + img1[r1,c1,0] + img2[2*r+1,2*c,0]) /3
            # img2[2*r+1,2*c+1,1] = (img2[2*r,2*c+1,1] + img1[r1,c1,1] + img2[2*r+1,2*c,1]) /3
            # img2[2*r+1,2*c+1,2] = (img2[2*r,2*c+1,2] + img1[r1,c1,2] + img2[2*r+1,2*c,2]) /3
            img2[2*r+1,2*c+1,0] = (img2[2*r,2*c+1,0] + img1[r1,c1,0]) /2
            img2[2*r+1,2*c+1,1] = (img2[2*r,2*c+1,1] + img1[r1,c1,1]) /2
            img2[2*r+1,2*c+1,2] = (img2[2*r,2*c+1,2] + img1[r1,c1,2]) /2

plt.imshow(img2)  
 
plt.imsave("rgb6.png",img2)

print(img2)

plt.show()