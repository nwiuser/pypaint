import cv2
import PIL 
import numpy as np
from PIL import Image as Im

class Image:
    def __init__(self, height, width, color) -> None:
        self.height = height
        self.width = width
        self.color = color

# setters and getters

    def getHeight(self):
        return self.height
    
    def getWidth(self):
        return self.width
    
    def getColor(self):
        return self.color
    
    def setHeight(self, val):
        self.height = val

    def setWidth(self, val):
        self.width = val
    
    def setColor(self, val):
        self.color = val

    def negative(self):
        img = cv2.imread(self)
        imgNeg = 1 - img
        return imgNeg

    def openGray(self):
        img = cv2.imread(self, cv2.IMREAD_GRAYSCALE)
        return img

    def openTransp(self):
        img = cv2.imread(self, cv2.IMREAD_UNCHANGED)
        return img
    
    def openColor(self):
        img = cv2.imread(self, cv2.IMREAD_COLOR)
        return img
    
    def rotateImage(path, degree):
        with Im.open(path) as im:
            rotated_image = im.rotate(degree)
            rotated_image.show()
            return rotated_image
        


image = Image(200,100,(100,155,144))

rotated_image = image.rotateImage('',90)

print(rotated_image)