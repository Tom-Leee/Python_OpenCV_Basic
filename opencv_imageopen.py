import cv2

img_file = 'C:/Users/Green/opencv_images/girl.jpg'
img = cv2.imread(img_file)

if img is not None:
    cv2.imshow('IMG',img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("NO IMAGE FILE.")
