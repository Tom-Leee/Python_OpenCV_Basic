import cv2
img = cv2.imread('black_500.jpg')

cv2.putText(img, "PLAIN", (50,30), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0))
cv2.putText(img, "SIMPLEX", (50,70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0))
cv2.putText(img, "DUPLEX", (50,110), cv2.FONT_HERSHEY_DUPLEX, 1, (0,0,0))

#*2는 문자열을 두 번 쓰라는
cv2.putText(img, "SIMPLEX * 2", (200,110), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,0,250))
cv2.putText(img, "COMPLEX_SMALL", (200,110), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,0))

#이 코드는 폰트를 함께 사용하는 방법입니다.
# | 구분선은 각각 다른 폰트를 적용해줄 수 있다.
cv2.putText(img, "PLAIN | ITALIC", (50,430), cv2.FONT_HERSHEY_PLAIN | cv2.FONT_ITALIC, 1, (0,0,0))
cv2.putText(img, "COMPLEX | ITALIC", (50,470), cv2.FONT_HERSHEY_COMPLEX | cv2.FONT_ITALIC, 1, (0,0,0))

cv2.imshow('draw text', img)
cv2.waitKey(0)
cv2.destroyAllWindows()