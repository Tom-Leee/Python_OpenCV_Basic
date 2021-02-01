import cv2
import numpy as np
import matplotlib.pylab as plt

# 이미지를 그레이 스케일로 읽기
img = cv2.imread('C:/Users/Green/opencv_images/scaned_paper.jpg', cv2.IMREAD_GRAYSCALE)

# 경계 값을 130으로 지정 ---①
_, t_80 = cv2.threshold(img, 80, 255, cv2.THRESH_BINARY)
_, t_100 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
_, t_130 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)
_, t_170 = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY)

# 경계 값을 지정하지 않고 OTSU 알고리즘 선택 ---②
# 경계값 -1의 전달은 자동으로 선택
t, t_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# Otsu 알고리즘으로 선택된 경계 값 출력
print('otsu threshold:', t)

imgs = {'Original': img, 't:80':t_80,'t:100':t_100,'t:130':t_130,'t:170':t_170, 'otsu:%d'%t: t_otsu}

for i , (key, value) in enumerate(imgs.items()):
    plt.subplot(2, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]); plt.yticks([])

plt.show()