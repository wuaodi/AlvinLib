import os
import cv2
import numpy as np
import glob
src_path = '200m-8m/'
img_array = []

# 按序号 1,2,3,...
for filename in [src_path + '{}.png'.format(i+1) for i in range(0, len(os.listdir(src_path)))]:
    img = cv2.imread(filename)
    try:
        height, width, layers = img.shape
        size = (width, height)
        img_array.append(img)
        print(filename)
    except Exception as e:
        print('图片不连续')
        continue

# # # os.listdir
# for filename in os.listdir(src_path):
#     img = cv2.imread(src_path+filename)
#     height, width, layers = img.shape
#     size = (width, height)
#     img_array.append(img)
#     print(filename)

out = cv2.VideoWriter('tuijin.avi', cv2.VideoWriter_fourcc(*'DIVX'), 20, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
print('over')
