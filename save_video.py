import cv2
cap = cv2.VideoCapture(0)
if cap.isOpened():
    file_path = "image_file/recode.avi" #저장할 파일 경로 이름 ①
    fps = 25.40 #FPS, 초당 프레임 수
    fourcc = cv2.VideoWriter_fourcc(*"DIVX") #인코딩 포맷 문자
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height)) #프레임 크기
    out = cv2.VideoWriter(file_path, fourcc, fps, size) #VideoWriter 객체 생성

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('camera-recoding', frame)
            out.write(frame) #파일 저장
            if cv2.waitKey(int(1000/fps)) != -1 :
                break
        else:
            print("no frame!")
            break
    out.release()
else:
    print("can't open camera")

cap.release()
cv2.destroyAllWindows()