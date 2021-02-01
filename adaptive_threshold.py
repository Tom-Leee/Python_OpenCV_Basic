import cv2
import numpy as np
import matplotlib.pyplot as plt

blk_size = 9 # 블럭 사이즈
C = 5 # 차감 상수

# 그레이 스케일로 읽기
img = cv2.imread('C:/Users/Green/opencv_images/scaned_paper.jpg',
                 cv2.IMREAD_GRAYSCALE)

# ---① 오츠의 알고리즘으로 단일 경계 값을 전체 이미지에 적용
ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# ---② 어뎁티드 쓰레시홀드를 평균과 가우시안 분포로 각각 적용
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,\
                            cv2.THRESH_BINARY, blk_size, C)

#입력 영상, 경계값을 만족하는 픽셀에 적용할 값, 경계 값 결정 방법,
# 스레시홀드 적용 방법 지정(이웃 픽셀의 평균 or 가우시간 분포에 따른 가중치의 합으로 결정),
# 영역으로 나눌 이웃의 크기(홀수), 계산된 경계 값 결과에서 가감할 상수

th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                            cv2.THRESH_BINARY, blk_size, C)

# ---③ 결과를 Matplot으로 출력
imgs = {'Original': img, 'Global-Otsu:%d'%ret:th1, \
        'Adapted-Mean':th2, 'Adapted-Gaussian': th3}

for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2,2,i+1)
    plt.title(k)
    plt.imshow(v,'gray')
    plt.xticks([]),plt.yticks([])

plt.show()