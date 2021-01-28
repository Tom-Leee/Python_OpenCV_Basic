import cv2

video_file = "C:/Users/Green/opencv_videos/lemon.mp4"

# cap = cv2.VideoCapture(0) # 카메라 0번 장치 연결
cap = cv2.VideoCapture(video_file)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # 프레임 폭 값 구하기
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # 프레임 높이 값 구하기
print("Original width : %d, height : %d" % (width, height))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320) # 프레임 폭을 320으로 설정
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240) # 프레임 높이를 240으로 설정
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # 재지정한 프레임 폭 값 구하기
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # 재지정한 프레임 높이 값 구하기
print("Resize width : %d, height : %d" % (width, height))

# #캡처 객체 초기화 확인
# if cap.isOpened():
#     while True:
#         # 다음 프레임 읽기
#         ret, img = cap.read()
#
#         # 프레임 읽기 정상
#         if ret:
#             # 화면에 표시
#             cv2.imshow(video_file, img)
#             if cv2.waitKey(1) != -1:
#                 break
#         # 다음 프레임을 읽을 수 없음
#         else:
#             print("no frame!")
#             # 재생 완료
#             break
# else:
#     # 캡처 객체 초기화 실패
#     print("can't open video.")
#
# # 캡처 자원 반납
# cap.release()
# cv2.destroyAllWindows()