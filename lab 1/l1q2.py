import cv2

vid_read=cv2.VideoCapture(r"C:\Users\student\Desktop\11254215-uhd_3840_2160_30fps.mp4")

if not vid_read.isOpened():
    print("Error opening video file")
    exit()

while (vid_read.isOpened()):
    # vCapture.read() methods returns a tuple, first element is a bool
    # and the second is frame

    ret, frame = vid_read.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        k = cv2.waitKey(20)
        # 113 is ASCII code for q key
        if k == 113:
            break
    else:
        break


vid_read.release()
cv2.destroyAllWindows()