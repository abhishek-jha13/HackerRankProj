# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np
import sys
input = sys.stdin.readlines()
print type(input)
print len(input)
print len(input[0])
print type(input[0][0])
#for i in range(0, len(data)):
#print input[167]

#end
data = []
print "#########"

for i in range(0, len(input)):
    data_row = []
    pixel = []
    pixel_strings = input[i].split(" ")
    for j in range(0, len(pixel_strings)):         
        pixel = [int(pixel_val) for pixel_val in pixel_strings[j].split(",")]
        data_row.append(pixel)
    data.append(data_row)
        #print pixel
print type(data)
print len(data)
print len(data[0])
print type(data[0][0])
night_avg_pixel = [66,59,56]
day_avg_pixel = [122,126,131]

sum_pixels = [0.0, 0.0, 0.0]
for i in range(0, len(data)):
    for j in range(0, len(data[0])):
        sum_pixels += data[i][j]
print sum_pixels
avg_pixel = [0, 0, 0]
for i in range(0,len(sum_pixels)):
    avg_pixel[i] = sum_pixels[i] / (len(data) * len(data[0]))
if np.linalg.norm(avg_pixel - night_avg_pixel) <= np.linalg.norm(avg_pixel - day_avg_pixel):
    print "day"
else:
    print "night"
