import cv2
import PIL 
import numpy as np
from PIL import Image 

def negative(name):
    img = cv2.imread(name)
    imgNeg = 1 - img
    cv2.imshow(name,imgNeg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def openGray(name):
    img = cv2.imread(name, cv2.IMREAD_GRAYSCALE)
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def openTransp(name):
    img = cv2.imread(name, cv2.IMREAD_UNCHANGED)
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def openColor(name):
    img = cv2.imread(name, cv2.IMREAD_COLOR)
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def rotateImage(name, degree):
    with Image.open(name) as im:
        im.rotate(degree).show()



negative('images.jpeg')