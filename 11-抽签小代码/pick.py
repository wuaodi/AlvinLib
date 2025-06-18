import os
import cv2
from random import choice

img_dir = "wx_img/"
result_dir = "result/"

# 显示幸运儿
def lucky(img, num):
    # 调用cv.putText()添加文字
    text = "Lucky person " + str(num) + "  !"
    composite_img = cv2.putText(img, text, (20, 100), cv2.FONT_HERSHEY_SIMPLEX,
                                1.5, (165, 93, 245), 5, cv2.LINE_AA, False)
    cv2.imshow('pick', composite_img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite(result_dir+str(num)+'.jpg', composite_img)


img_list = os.listdir(img_dir)
img_set = set(img_list)

for i in range(len(img_list)):
    i = i +1
    for hhh in range (len(img_set)*2):
        choice_list = list(img_set)
        name = choice(choice_list)
        img = cv2.imread(img_dir + name)
        img = cv2.resize(img, (500, 500))
        cv2.imshow('pick', img)
        cv2.waitKey(50)
    name = img_set.pop()
    img = cv2.imread(img_dir + name)
    img = cv2.resize(img, (500, 500))
    lucky(img, i)
