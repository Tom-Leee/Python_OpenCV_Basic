import cv2
# 동영상 파일 경로
video_file = "C:/Users/Green/opencv_videos/lemon.mp4"

# 동영상 캡쳐 객체 생성
cap = cv2.VideoCapture(video_file)

# 캡처 객체 초기화 확인
if cap.isOpened():
    
    #초당 프레임 수 구하기
    fps = cap.get(cv2.CAP_PROP_FPS)

    #지연 시간 구하기
    delay = int(1000/fps)
    print("FPS: %f, Delay: %dms" %(fps, delay))
    while True:
        # 다음 프레임 읽기
        ret, img = cap.read()

        # 프레임 읽기 정상
        if ret:
            # 화면에 표시
            cv2.imshow(video_file, img)
            # fps에 맞게 시간 지연
            cv2.waitKey(delay)
        else:
            # 다음 프레임을 읽을 수 없다면 재생 완료
            break

else:
    # 캡처 객체 초기화 실패
    print("can't open video.")

# 캡처 자원 반납
cap.release()
cv2.destroyAllWindows()


#카메라나 영상 대신에 youtube로 대체
import cv2
import pafy

url = 'https://www.youtube.com/watch?v=uidzxS0nytI&t=31s'
video = pafy.new(url)
print('title = ', video.title)
print('video.rating = ', video.rating)
print('video.duration = ', video.duration)

best = video.getbest(preftype='mp4')  # 'webm','3gp'
print('best.resolution', best.resolution)

cap = cv2.VideoCapture(best.url)

# 캡처 객체 초기화 확인
if cap.isOpened():

    # 초당 프레임 수 구하기
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 지연 시간 구하기
    delay = int(1000 / fps)
    print("FPS: %f, Delay: %dms" % (fps, delay))
    while True:
        # 다음 프레임 읽기
        ret, img = cap.read()

        # 프레임 읽기 정상
        if ret:
            # 화면에 표시
            cv2.imshow(video_file, img)
            # fps에 맞게 시간 지연
            cv2.waitKey(delay)
        else:
            # 다음 프레임을 읽을 수 없다면 재생 완료
            break

else:
    # 캡처 객체 초기화 실패
    print("can't open video.")

# 캡처 자원 반납
cap.release()
cv2.destroyAllWindows()