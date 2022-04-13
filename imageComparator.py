import numpy as np
import cv2 as cv

def compare(img1, img2):    
    color = ('b','g','r')
    pre = {}

    for i,col in enumerate(color):
        histr1 = cv.calcHist([img1],[i],None,[256],[0,256])
        histr2 = cv.calcHist([img2],[i],None,[256],[0,256])
        if col == 'r' :
            pre['vermelho'] = list(np.array(histr1) - np.array(histr2))
        if col == 'b':
            pre['azul'] = list(np.array(histr1) - np.array(histr2))
        if col == 'g':
            pre['verde'] = list(np.array(histr1) - np.array(histr2))

    for i,col in enumerate(color):
        histr2 = cv.calcHist([img2],[i],None,[256],[0,256])
        if col == 'r' :
            pre['vermelho'] = list(np.array(histr1) - np.array(histr2))
        if col == 'b':
            pre['azul'] = list(np.array(histr1) - np.array(histr2))
        if col == 'g':
            pre['verde'] = list(np.array(histr1) - np.array(histr2))

    return np.linalg.norm(histr2 - histr1)

    