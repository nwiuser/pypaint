import cv2
import tkinter as tk
import PIL 
import numpy as np
from PIL import Image 

def resizeImage(name, x, y):
    img = cv2.imread(name)
    res2 = img.resize((x,y))
    return res2

def composite(name1, name2):
    img1 = Image.open(name1).convert("RGBA")
    img2 = Image.open(name2).convert("RGBA")
    if img1.size != img2.size:
        img2 = img2.resize(img1.size) 

    im3 = Image.alpha_composite(img1, img2) 
    return im3

