import cv2
import numpy as np

#기본 값 옵션
img = cv2.imread('C:/Users/Green/opencv_images/ryan.png')

#IMREAD_COLOR 옵션
bgr = cv2.imread('C:/Users/Green/opencv_images/ryan.png', cv2.IMREAD_COLOR)
bgra = cv2.imread('C:/Users/Green/opencv_images/ryan.png', cv2.IMREAD_UNCHANGED)

#각 옵션에 따른 이미지 SHAPE
print("default :", img.shape, "color:", bgr.shape, "unchanged:", bgra.shape)

cv2.imshow("bgr", bgr)
cv2.imshow("bgra", bgra)

#알파 채널만 표시
cv2.imshow('alpha', bgra[:,:,3])

cv2.waitKey(0)
cv2.destroyAllWindows()