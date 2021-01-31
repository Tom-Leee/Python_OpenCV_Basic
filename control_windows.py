import cv2

file_path = 'C:/Users/Green/opencv_images/girl.jpg'
img = cv2.imread(file_path) #이미지를 기본값으로 읽기
img_gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE) #이미지를 그레이 스케일로 읽기

cv2.namedWindow('origin', cv2.WINDOW_AUTOSIZE) #origin 이라는 이름으로 창 생성
cv2.namedWindow('gray', cv2.WINDOW_NORMAL) #gray라는 이름으로 창 생성

cv2.imshow('origin', img) #origin 창에 이미지 표시
cv2.imshow('gray', img_gray) #gray 창에 이미지 표시

cv2.moveWindow('origin', 0, 0) #창 위치 변경
cv2.moveWindow('gray', 100, 100) #창 위치 변경

cv2.waitKey(0)
cv2.resizeWindow('origin', 200, 200) #창 크기 변경(아직 변경 안됨)
cv2.resizeWindow('gray', 100, 100) #창 크기 변경(변경됨)

cv2.waitKey(0)
cv2.destroyWindow('gray') #아무 키나 누르면 gray 창 닫기

cv2.waitKey(0)
cv2.destroyAllWindows() #아무 키나 누르면 창 전체 닫기