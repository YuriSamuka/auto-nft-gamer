import time
import sys

import numpy as np
from structure import deckFormation
import coordenadas as c
import copy
import cv2 as cv
import pyautogui
import acoes
from ScreenFramePackage import Farming, erroScreen, walletconnect, metamaskSignin, menuScreenTreasureHunt, login

class BombCryptoGamer():
    def __init__(self):
        self.lastCheckup = 0
        self.lastWakeUpAll = 0
        self.lastShackItAll = 0
        self.possibleScreens = [erroScreen, walletconnect, metamaskSignin, menuScreenTreasureHunt, Farming, login] 
        self.giveUp = False
    
    def getLastCheckup(self):
        return self.lastCheckup

    def getLastWakeUpAll(self):
        return self.lastWakeUpAll

    def getLastShackItAll(self):
        return self.lastShackItAll

    def setLastCheckup(self, time):
        self.lastCheckup = time

    def setLastWakeUpAll(self, time):
        self.lastWakeUpAll = time

    def setLastShackItAll(self, time):
        self.lastShackItAll = time

    def shackItAll(self):
        number = deckFormation( 'Bombcrypto - Google Chrome' ) - 1
        while ( number >=0 ):
            if self.giveUp: raise Exception("it's time to stop!")
            print (f'Click window {number}')
            self.selectWindow(number)
            acoes.shake(number)
            time.sleep(1)
            number-=1
        print("All shaked...")


    def wakeUpAll(self):
        number = deckFormation( 'Bombcrypto - Google Chrome' ) - 1
        while ( number >=0 ):
            if self.giveUp: raise Exception("it's time to stop!")
            print (f'Click window {number}')
            self.selectWindow(number)
            acoes.wakeup(number)
            time.sleep(1)
            number-= 1
        print("Awoke!")

    def checkupRoutine(self):
        # number = deckFormation( 'Bombcrypto - Google Chrome' ) - 1
        # time.sleep(5)
        # windowsPos = acoes.mult ( copy.copy ( c.corner), number)
        # # acoes.Click( windowsPos )
        # print(windowsPos)
        # printScreen = printScreenCropped(windowsPos[1], windowsPos[0] - 5, 984, 722, number)
        # print(f'is it menuScreenTreasureHunt?? {menuScreenTreasureHunt.isItMe(printScreen)}')
        # time.sleep(3)

        # windowsPos = acoes.mult ( copy.copy ( c.corner), number -1)
        # # acoes.Click( windowsPos )
        # print(windowsPos)
        # printScreen = printScreenCropped(windowsPos[1], windowsPos[0], 984, 722, number -1)
        # print('troca de janela')
        # time.sleep(3)
        
        # windowsPos = acoes.mult ( copy.copy ( c.corner), number -2)
        # # acoes.Click( windowsPos )
        # print(windowsPos)
        # printScreen = printScreenCropped(windowsPos[1], windowsPos[0], 984, 722, number -2)
        # print('troca de janela')
        # time.sleep(3)

        # sys.exit()

        # token = getSecurityToken()
        # if( True ):
        print("is it running??? omfg!!! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")

        number = deckFormation( 'Bombcrypto - Google Chrome' ) - 1
        while ( number >=0 ):
            if self.giveUp: raise Exception("it's time to stop!")
            # print("aki!")
            # time.sleep(10)
            self.selectWindow(number)
            if ( self.tryToGetAtTheScreen(Farming, number) ):
                print("next window!")
                number-=1
            else:
                print("tenta de novo")
        
        print("achei a tela de boss select")


    def printScreenCropped(self, x, y, dx, dy, i):
        myScreenshot = pyautogui.screenshot()
        imagem = cv.cvtColor(np.array(myScreenshot), cv.COLOR_RGB2BGR)
        crop_img = imagem[y:y+dy , x: x+dx ]
        cv.imwrite("img.png", crop_img)
        return crop_img

    def tryToGetAtTheScreen(self, screen, window, path = [], limitTime = 60):
        # path pra quando precisar de path
        windowsPos = acoes.mult ( copy.copy ( c.corner), window)
        printScreen = self.printScreenCropped(windowsPos[1], windowsPos[0], 984, 722, window)
        timeIni = time.time()
        while (not screen.isItMe(printScreen) and limitTime > time.time() - timeIni):
            if self.giveUp: raise Exception("it's time to stop!")
            i = 0
            while(not self.possibleScreens[i].isItMe(printScreen) and i < len(self.possibleScreens) -1):
                i += 1
            if ( self.possibleScreens[i].isItMe(printScreen) ):
                print(self.possibleScreens[i].info)
                self.possibleScreens[i].performScreenAction(window)
            printScreen = self.printScreenCropped(windowsPos[1], windowsPos[0], 984, 722, window)

        if(limitTime > time.time() - timeIni):
            return True
            
        return False

    def selectWindow(self, window):
        windowsPos = acoes.mult ( copy.copy ( c.head), window)
        acoes.Click(windowsPos)
        time.sleep(2)

    def stop(self):
        self.giveUp = True