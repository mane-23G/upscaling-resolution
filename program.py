import matplotlib.pyplot as plt  # type: ignore
import numpy as np # type: ignore


img = plt.imread("up720.jpg")
row, col = img.shape[:2]
print(f"width is {col} and height is {row}")

