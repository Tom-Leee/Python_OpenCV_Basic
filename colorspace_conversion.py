import cv2
import numpy as np
img = cv2.imread('C:/Users/Green/opencv_images/ryan.png')

#①dtype 변경
img2 = img.astype(np.uint16)

#②채널별로 분리
b,g,r = cv2.split(img)

#③평균 값 연산 후 dtype 변경
gray1 = ((b + g + r)/3).astype(np.uint8)

#④BGR을 그레이 스케일로 변경
gray2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('original', img)
cv2.imshow('gray1', gray1)
cv2.imshow('gray2', gray2)

cv2.waitKey(0)
cv2.destroyAllWindows()