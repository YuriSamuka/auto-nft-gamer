import sys
import threading
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QSize
from numpy import true_divide
import requests
import time
from BombCryptoGamer import BombCryptoGamer


class MainWindow(QMainWindow):
    def __init__(self):

        self.once = True

        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(300, 300))
        self.setStyleSheet("QMainWindow { background-color : #021f59; }")
        self.setWindowTitle("Auto Gamer - Fancy Kayak Solutions") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Validar lincença:')
        self.nameLabel.setStyleSheet("QLabel { color : #f1ffff; font-weight: bold; }")
        self.line = QLineEdit(self)

        self.lbStatus = QLabel(self)
        self.lbStatus.setText('Bot desativado - Usuário não validado')
        self.lbStatus.setStyleSheet("QLabel { color : #f1ffff; font-weight: bold; }")
        self.lbStatus.move(10, 260)
        self.lbStatus.resize(280, 32)

        self.line.move(10, 190)
        self.line.resize(280, 32)
        self.nameLabel.move(10, 160)

        self.pybutton = QPushButton('Validar', self)
        self.pybutton.setStyleSheet("QPushButton { background-color : #bb8a3c; color: #f1ffff; font-weight: bold; }")
        self.pybutton.clicked.connect(self.clickMethod)
        self.pybutton.resize(280,32)
        self.pybutton.move(10, 230)

        pic = QLabel(self)
        pic.setGeometry(27, 0, 247, 143)
        pic.setPixmap(QtGui.QPixmap("./images/banner.jpg"))
        pic.show()


  
        self.loading = QLabel(self)
        # self.loading.setStyleSheet("QMovie { background-color : #021f59; }")
        self.loading.setGeometry(130, 270, 32, 32)
        self.loading.setMinimumSize(QtCore.QSize(32, 32))
        self.loading.setMaximumSize(QtCore.QSize(32, 32))
        self.movie = QMovie("loading-icon.gif")
        self.loading.setMovie(self.movie)

        self.gamer = BombCryptoGamer()

        self.email = ''
        self.tokenSession = ''
        self.active = False



    def clickMethod(self):
        try:
            self.email = self.line.text()
            self.pybutton.setEnabled(False)
            self.pybutton.setText("validando...")
            r = requests.get('https://powerful-island-81194.herokuapp.com/login?email=' + self.email)
            if r.text == 'Cadastro Inexistente!':
                print("Cadastro Inexistente!")
                self.pybutton.setEnabled(True)
                self.pybutton.setText("Validar")
            else :
                self.tokenSession = r.text
                self.active = True
                # self.lbStatus.setText("User validado! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
                print(self.tokenSession)
                self.pybutton.setEnabled(True)
                self.pybutton.setText("Validar")
        except:
            print("An exception on requests.get occurred")

    # def startMainLoop(self):
    #     def func_wrapper():
    #         self.startMainLoop()
    #         if self.active:
    #             if ( time.time() - self.gamer.getLastCheckup() ) > ( 60 * 60 ):
    #                 self.gamer.checkupRoutine()
    #                 self.gamer.setLastCheckup( time.time() )
    #                 print("passou aqui quantasvezes??")
    #         else:
    #             print("user não validado")
    #     self.mainLoopThread = threading.Timer(10, func_wrapper)
    #     self.mainLoopThread.start()

    def startMainLoop(self):
        def func_wrapper():
            err = False
            try:
                if self.active:
                    if ( time.time() - self.gamer.getLastCheckup() ) > ( 60 * 10 ):
                        self.gamer.checkupRoutine()
                        self.gamer.setLastCheckup( time.time() )

                    if ( time.time() - self.gamer.getLastWakeUpAll() ) > ( 60 * 60 * 2 ):
                        self.gamer.wakeUpAll()
                        self.gamer.setLastWakeUpAll( time.time() )

                    if ( time.time() - self.gamer.getLastShackItAll() ) > ( 60 * 5 ):
                        self.gamer.shackItAll()
                        self.gamer.setLastShackItAll( time.time() )
                else:
                    print("user não validado")
            except:
                print("An exception on requests.get occurred of startMainLoop")
                self.stopMainLoop()
                err = True
                self.close()
            if not err:
                self.startMainLoop()
        
        self.mainLoopThread = threading.Timer(1, func_wrapper)
        self.mainLoopThread.start()

    def stopMainLoop(self):
        self.mainLoopThread.cancel()
        self.gamer.stop()


    def startValidatorLoop(self):
        def func_wrapper():
            err = False
            try:
                if self.tokenSession :
                    r = requests.get('https://powerful-island-81194.herokuapp.com/matchtoken?email=' + self.email + '&token=' + self.tokenSession)
                    if r.text != 'true':
                        self.active = False
                        print(r.text)
                    else :
                        self.active = True
                        self.lbStatus.setText("User validado! (ﾉ◕ヮ◕)ﾉ*:･ﾟ✧")
                        print("ainda ativoo!")
            except:
                print("An exception on requests.get occurred of startValidatorLoop")
                self.stopValidatorLoop()
                err = True
                self.close()
            if not err :
                self.startValidatorLoop()

        self.validatorLoop = threading.Timer(10, func_wrapper)
        self.validatorLoop.start()
    
    def stopValidatorLoop(self):
        self.validatorLoop.cancel()

    def __del__(self):
        del self.gamer

        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.startMainLoop()
    mainWin.startValidatorLoop()
    mainWin.show()

    reason = app.exec_()
    mainWin.stopMainLoop()
    mainWin.stopValidatorLoop()
    sys.exit( reason )