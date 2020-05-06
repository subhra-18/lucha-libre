
import os
import cv2


def partA():
    f = open("../Generated/stats.csv", "w")
    img_b = cv2.imread("../Images/bird.jpg")
    img_c = cv2.imread("../Images/cat.jpg")
    img_f = cv2.imread("../Images/flowers.jpg")
    img_h = cv2.imread("../Images/horse.jpg")
    bnb = os.path.basename("../Images/bird.jpg")
    bnc = os.path.basename("../Images/cat.jpg")
    bnf = os.path.basename("../Images/flowers.jpg")
    bnh = os.path.basename("../Images/horse.jpg")
    img_bh = img_b.shape[0]
    img_bw = img_b.shape[1]
    img_bc = img_b.shape[2]
    img_ch = img_c.shape[0]
    img_cw = img_c.shape[1]
    img_cc = img_c.shape[2]
    img_fh = img_f.shape[0]
    img_fw = img_f.shape[1]
    img_fc = img_f.shape[2]
    img_hh = img_h.shape[0]
    img_hw = img_h.shape[1]
    img_hc = img_h.shape[2]
    xb = img_bh // 2
    yb = img_bw // 2
    xc = img_ch // 2
    yc = img_cw // 2
    xf = img_fh // 2
    yf = img_fw // 2
    xh = img_hh // 2
    yh = img_hw // 2

    f.write(str(bnb))
    f.write(",")
    f.write(str(img_bh))
    f.write(",")
    f.write(str(img_bw))
    f.write(",")
    f.write(str(img_bc))
    f.write(",")
    f.write(str(img_b[xb][yb]))
    f.write(",\n")
    f.write(str(bnc))
    f.write(",")
    f.write(str(img_ch))
    f.write(",")
    f.write(str(img_cw))
    f.write(",")
    f.write(str(img_cc))
    f.write(",")
    f.write(str(img_c[xc][yc]))
    f.write(",\n")
    f.write(str(bnf))
    f.write(",")
    f.write(str(img_fh))
    f.write(",")
    f.write(str(img_fw))
    f.write(",")
    f.write(str(img_fc))
    f.write(",")
    f.write(str(img_f[xf][yf]))
    f.write(",\n")
    f.write(str(bnh))
    f.write(",")
    f.write(str(img_hh))
    f.write(",")
    f.write(str(img_hw))
    f.write(",")
    f.write(str(img_hc))
    f.write(",")
    f.write(str(img_h[xh][yh]))


def partB():
    img = cv2.imread("../Images/cat.jpg")
    img_2 = img.copy()
    h = img.shape[0]
    w = img.shape[1]
    for height in range(h):
        for width in range(w):
            img_2[height][width][0] = 0
            img_2[height][width][1] = 0
    cv2.imwrite("../Generated/cat_red.jpg", img_2)


def partC():
    img = cv2.imread("../Images/flowers.jpg")
    img_2 = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    h = img_2.shape[0]
    w = img_2.shape[1]
    for height in range(h):
        for width in range(w):
            img_2[height][width][3] = 50
    cv2.imwrite("../Generated/flowers_alpha.png", img_2)


def partD():
    img = cv2.imread("../Images/horse.jpg")
    img_2 = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    h = img_2.shape[0]
    w = img_2.shape[1]
    for height in range(h):
        for width in range(w):
            img_2[height][width] = (0.11*img[height][width][0])+(0.59*img[height][width][1])+(0.3*img[height][width][0])
    cv2.imwrite("../Generated/horse_grey.jpg", img_2)


partA()
partB()
partC()
partD()