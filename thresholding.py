import cv2
import numpy as np
import matplotlib.pylab as plt

# 이미지를 그레이 스케일로 읽기
img = cv2.imread('C:/Users/Green/opencv_images/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)

# --- ① NumPy API로 바이너리 이미지 만들기
# 원본과 동일한 크기의 0으로 채워진 이미지
thresh_np = np.zeros_like(img)

# 127 보다 큰 값만 255로 변경
thresh_np[ img > 127] = 255

# ---② OpenCV API로 바이너리 이미지 만들기
# 변환할 이미지, 경계값, 경계값 기준에 만족하는 픽셀에 적용할 값
ret, thresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# 127.0, 바이너리 이미지에 사용된 문턱 값 반환 ,
# 픽셀 값이 경계값을 넘으면 value를 지정하고, 넘지 못하면 0
print(ret)

# ---③ 원본과 결과물을 matplotlib으로 출력
imgs = {'Original': img, 'NumPy API':thresh_np, 'cv2.threshold': thresh_cv}
for i , (key, value) in enumerate(imgs.items()):
    plt.subplot(1, 3, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]); plt.yticks([])

plt.show()


import cv2
import numpy as np
import matplotlib.pylab as plt

img = cv2.imread('C:/Users/Green/opencv_images/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)

_, t_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, t_bininv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, t_truc = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, t_2zr = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, t_2zrinv = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

imgs = {'origin': img, 'BINARY': t_bin, 'BINARY_INV': t_bininv, \
    'TRUNC': t_truc, 'TOZERO': t_2zr, 'TOZERO_INV': t_2zrinv}

for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(2, 3, i + 1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]);
    plt.yticks([])

plt.show()