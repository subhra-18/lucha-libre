###############################################################################
## Instructions: Do Not modify the basic skeletal structure of given APIs!!!
###############################################################################


######################
## Essential libraries
######################
import cv2
import numpy as np
import os
import math
import csv

########################################################################
## using os to generalise Input-Output
########################################################################
codes_folder_path = os.path.abspath('.')
images_folder_path = os.path.abspath(os.path.join('..', 'Images'))
generated_folder_path = os.path.abspath(os.path.join('..', 'Generated'))


############################################
## Build your algorithm in this function
## ip_image: is the array of the input image
## imshow helps you view that you have loaded
## the corresponding image
############################################
def process(ip_image):
    ###########################
    ## Your Code goes here

    h = ip_image.shape[0]
    w = ip_image.shape[1]
    ch = h // 2
    cw = w // 2
    gh = 0
    gw = 0
    rh = 0
    rw = 0

    print(ch, cw)

    for height in range(h):
        for width in range(w):
            if ip_image[height][width][1] >= 100 and ip_image[height][width][0] <= 20 and ip_image[height][width][
                2] <= 20:
                gh = height
                gw = width
                break
    print(gh, gw)
    for height in range(h):
        for width in range(w):
            if ip_image[height][width][2] >= 100 and ip_image[height][width][0] <= 20 and ip_image[height][width][
                1] <= 20:
                rh = height
                rw = width
                break
    print(rh, rw)
    rg = math.sqrt((gh - rh) ** 2 + (gw - rw) ** 2)
    gc = math.sqrt((gh - ch) ** 2 + (gw - cw) ** 2)
    cr = math.sqrt((ch - rh) ** 2 + (cw - rw) ** 2)
    angle = math.acos(((gc ** 2) + (cr ** 2) - (rg ** 2)) / (2 * gc * cr))
    print(rg)
    print(gc)
    print(cr)
    print(angle)

    ## Your Code goes here
    ###########################
    cv2.imshow("window", ip_image)
    cv2.waitKey(0);
    return angle


####################################################################
## The main program which provides read in input of one image at a
## time to process function in which you will code your generalized
## output computing code
## Do not modify this code!!!
####################################################################
def main():
    ################################################################
    ## variable declarations
    ################################################################
    i = 1
    line = []
    ## Reading 1 image at a time from the Images folder
    for image_name in os.listdir(images_folder_path):
        ## verifying name of image
        print(image_name)
        ## reading in image
        ip_image = cv2.imread(images_folder_path + "/" + image_name)
        ## verifying image has content
        print(ip_image.shape)
        ## passing read in image to process function
        A = process(ip_image)
        ## saving the output in  a list variable
        line.append([str(i), image_name, str(A)])
        ## incrementing counter variable
        i += 1
    ## verifying all data
    print(line)
    ## writing to angles.csv in Generated folder without spaces
    with open(generated_folder_path + "/" + 'angles.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(line)
    ## closing csv file
    writeFile.close()


############################################################################################
## main function
############################################################################################
if __name__ == '__main__':
    main()
