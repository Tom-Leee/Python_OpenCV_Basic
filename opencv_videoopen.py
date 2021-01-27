import cv2
video_file = "C:/Users/Green/opencv_videos/lemon.mp4"

#동영상 캡처 객체 생성
cap = cv2.VideoCapture(video_file)

#캡처 객체 초기화 확인
if cap.isOpened():
    while True:

        # 다음 프레임 읽기
        ret, img = cap.read()

        # 프레임 읽기 정상
        if ret:
            # 화면에 표시
            cv2.imshow(video_file, img)

            # 25ms 지연(40fps로 가정)
            cv2.waitKey(25)

        # 다음 프레임을 읽을 수 없음
        else:
            # 재생 완료
            break
else:
    # 캡처 객체 초기화 실패
    print("can't open video.")

# 캡처 자원 반납
cap.release()
cv2.destroyAllWindows()