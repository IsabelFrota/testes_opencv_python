import numpy as np
import cv2

def CarregarImagem(jpeg):
    img = cv2.imread(jpeg)
    cv2.imshow("Lena", img)
    cv2.waitKey(0)


jpg = "len_top.jpg"
CarregarImagem(jpg)

