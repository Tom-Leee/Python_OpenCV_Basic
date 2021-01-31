#관심영역 지정
import cv2
import numpy as np

img = cv2.imread('C:/Users/Green/opencv_images/girl.jpg')

x = 110; y = 200; w = 50; h = 50 #roi 좌표
roi = img[y : y+h, x : x+w] #①roi 지정

print(roi.shape)
cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0)) #②roi에 사각형 그리기
cv2.imshow("img", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

