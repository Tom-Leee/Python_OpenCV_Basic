import cv2
cap = cv2.VideoCapture(0) # 카메라 0번 장치 연결
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # 프레임 폭 값 구하기
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # 프레임 높이 값 구하기
print("Original width : %d, height : %d" % (width, height))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320) # 프레임 폭을 320으로 설정
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240) # 프레임 높이를 240으로 설정
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # 재지정한 프레임 폭 값 구하기
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # 재지정한 프레임 높이 값 구하기
print("Resize width : %d, height : %d" % (width, height))