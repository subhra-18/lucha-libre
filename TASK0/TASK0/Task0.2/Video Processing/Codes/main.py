import cv2


def partA():
    cap = cv2.VideoCapture("../Videos/RoseBloom.mp4")
    fps = cap.get(cv2.cv2.CAP_PROP_FPS)
    ret = 1
    ctr = 0
    while ret and ctr <= ((fps * 6) + 1):
        ret, frame = cap.read()
        ctr += 1
    cv2.imwrite("../Generated/frame_as_6.jpg", frame)


def partB():
    img = cv2.imread("../Generated/frame_as_6.jpg")
    img_2 = img.copy()
    h = img.shape[0]
    w = img.shape[1]
    for height in range(h):
        for width in range(w):
            img_2[height][width][0] = 0
            img_2[height][width][1] = 0
    cv2.imwrite("../Generated/frame_as_6_red.jpg", img_2)


partA()
partB()
