import numpy as np
from scipy import misc
import glob
import detect_day_or_night.k_means_clustering
folders = glob.glob("C:/Users/ajha2/Desktop/PythonProjects/detect_day_or_night_input/*")
#image = misc.imread("C:/Users/ajha2/Desktop/PythonProjects/detect_day_or_night_input/img1.jpg")
avg_pixel_list = []
for folder in folders:
    files = glob.glob(folder + "/*")
    print (folder)
    for file in files:
        image = misc.imread(file)
        sum_pixels = [0.0, 0.0, 0.0]
        for i in range(0, len(image)):
            for j in range(0, len(image[0])):
                sum_pixels += image[i][j]
        avg_pixel = sum_pixels / (len(image) * len(image[0]))
        avg_pixel_list.append(avg_pixel)
        #print sum_pixels / (len(image) * len(image[0]))
        print (",".join(map(str, avg_pixel.astype(int))))

print (avg_pixel_list)

detect_day_or_night.k_means_clustering.apply(avg_pixel_list, 2)