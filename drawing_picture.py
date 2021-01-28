import cv2
import numpy as np

img = np.full((500,500,3),255,dtype = np.uint8)
cv2.imwrite('black_500.jpg',img)

import cv2
img = cv2.imread('black_500.jpg')
cv2.line(img, (50,50), (150,50),(255,0,0)) # 파란색 1픽셀 선
cv2.line(img, (200,50), (300,50),(0,255,0)) # 초록색 1픽셀 선
cv2.line(img, (350,50), (450,50),(0,0,5)) # 빨간색 1픽셀 선

cv2.line(img, (100,100), (400,100),(255,255,0), 10) # 하늘색 10 픽셀 선
cv2.line(img, (100,150), (400,150),(255,0,255), 10) # 분홍색 10픽셀 선

cv2.line(img, (100,350), (400,400), (0,0,255), 20, cv2.LINE_4) #4연결선
cv2.line(img, (100,400), (400,450), (0,0,255), 20, cv2.LINE_8) #8연결선
cv2.line(img, (100,450), (400,500), (0,0,255), 20, cv2.LINE_AA) #안티에일리어싱 선

cv2.line(img, (0,0), (500,500), (0,0,255)) #이미지 전체에 대각선

cv2.imshow('lines', img)
cv2.waitKey(0)
cv2.destroyAllWindows()