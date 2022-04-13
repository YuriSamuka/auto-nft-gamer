import time
import acoes 
import copy
import cv2 as cv
from imageComparator import compare

class ScreenFrame:
    def __init__(self, x, y, dx, dy, samplePath, threshold, info, clickPoint, waitTime):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.samplePath = samplePath
        self.threshold = threshold
        self.info = info
        self.clickPoint = clickPoint
        self.waitTime = waitTime

    def getFrameImage(self):
        # retorna a img em formato matrix
        return None

    def performScreenAction(self, window, context = None):
        if (context):
            # executa sequencia especifica de comandos
            return None
        else:
            clickPos = acoes.mult ( copy.copy ( self.clickPoint ), window)
            acoes.Click(clickPos)
            time.sleep(self.waitTime)
        return None

    def isItMe(self, printScreen):
        img1 = cv.imread(self.samplePath)[self.y : self.y+self.dy, self.x : self.x+self.dx]
        img2 = printScreen[self.y : self.y+self.dy, self.x : self.x+self.dx]
        cv.imwrite ("./images/img1croped.png", img1 )
        cv.imwrite ("./images/img2croped.png", img2 )
        t = compare(img1, img2)
        print(f'threshold: {t}')
        if (t < self.threshold):
            return True
        return False