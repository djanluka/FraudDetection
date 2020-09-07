from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess as sp
import os
import threading
import base64
import io
import json
import requests
import pandas as pd



class Ui_FakeSignature(object):
    def setupUi(self, FakeSignature):
        FakeSignature.setObjectName("FakeSignature")
        FakeSignature.resize(835, 527)
        FakeSignature.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(FakeSignature)
        self.centralwidget.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.centralwidget.setStyleSheet("background-color: silver;")
        self.centralwidget.setObjectName("centralwidget")
        
        #frame
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(220, 30, 331, 211))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
       
        #window icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/home/dutzeee/Desktop/comtrade/app/pic/PinClipart.com_cheap-clipart_5472.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        FakeSignature.setWindowIcon(icon)

        self.CameraBtn = QtWidgets.QPushButton(self.centralwidget)
        self.CameraBtn.setGeometry(QtCore.QRect(100, 280, 131, 61))
        self.CameraBtn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.CameraBtn.setStyleSheet("")
        self.CameraBtn.setObjectName("CameraBtn")
        #turn on camera
        self.CameraBtn.clicked.connect(self.cameraOn)

        self.TakeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.TakeBtn.setGeometry(QtCore.QRect(310, 280, 131, 61))
        self.TakeBtn.setObjectName("TakeBtn")
        #take a picture
        self.TakeBtn.clicked.connect(self.takePhoto)


        self.predictBtn = QtWidgets.QPushButton(self.centralwidget)
        self.predictBtn.setGeometry(QtCore.QRect(520, 280, 131, 61))
        self.predictBtn.setObjectName("predictBtn")
        #predict
        self.predictBtn.clicked.connect(self.predict)


        self.closePic = QtWidgets.QPushButton(self.centralwidget)
        self.closePic.setGeometry(QtCore.QRect(651, 100, 60, 60))
        self.closePic.setObjectName("predictBtn")

        #close picture
        self.closePic.clicked.connect(self.exitPic)
        

        self.rezultat = QtWidgets.QLabel(self.centralwidget)
        self.rezultat.setGeometry(QtCore.QRect(300, 380, 241, 31))
        self.rezultat.setText("")
        self.rezultat.setObjectName("rezultat")
        self.slika = QtWidgets.QLabel(self.centralwidget)
        self.slika.setGeometry(QtCore.QRect(220, 30, 331, 211))
        self.slika.setText("")
        self.slika.setPixmap(QtGui.QPixmap("nesto.jpg"))
        self.slika.setScaledContents(True)
        self.slika.setObjectName("slika")
        self.slika.setVisible(False)
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(640, 370, 171, 81))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("pic/editLogo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        FakeSignature.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(FakeSignature)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 835, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        FakeSignature.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FakeSignature)
        self.statusbar.setObjectName("statusbar")
        FakeSignature.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(FakeSignature)
        self.toolBar.setObjectName("toolBar")
        FakeSignature.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(FakeSignature)
        QtCore.QMetaObject.connectSlotsByName(FakeSignature)

    def retranslateUi(self, FakeSignature):
        _translate = QtCore.QCoreApplication.translate
        FakeSignature.setWindowTitle(_translate("FakeSignature", "FakeSignature"))
        self.CameraBtn.setText(_translate("FakeSignature", "Camera"))
        self.TakeBtn.setText(_translate("FakeSignature", "Take a picture"))
        self.predictBtn.setText(_translate("FakeSignature", "Predict"))
        self.closePic.setText(_translate("FakeSignature", "x"))
        self.menuFile.setTitle(_translate("FakeSignature", "File"))
        self.toolBar.setWindowTitle(_translate("FakeSignature", "toolBar"))


    def cameraOn(self):
        self.rezultat.setText("")
        proc = sp.Popen(["./1.py"])
        prom = threading.Timer(1000000 ,proc.terminate)
        prom.start()

    def takePhoto(self):
        os.system("bash 1.sh")
        self.slika.setPixmap(QtGui.QPixmap("nesto.jpg"))
        self.slika.setScaledContents(True)
        self.slika.setVisible(True)

    def predict(self):
        images = []
        with open("./nesto.jpg", "rb") as img_file:
            my_string = base64.b64encode(img_file.read()).decode('utf-8')
            images.append(my_string)

        response = requests.post("http://144543c5-fc15-4078-bd74-2fee4727df4b.eastus.azurecontainer.io/score", json = {"data":images})
        results = response.json()
      
        if results[0][0] == 0:
            self.rezultat.setText("SIGNATURE IS ORIGINAL")
            self.rezultat.setStyleSheet("color:green")
        else:
            self.rezultat.setText("SIGNATURE IS FAKED")
            self.rezultat.setStyleSheet("color:red")

    def exitPic(self):
        self.slika.setVisible(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FakeSignature = QtWidgets.QMainWindow()
    ui = Ui_FakeSignature()
    ui.setupUi(FakeSignature)
    FakeSignature.show()
    sys.exit(app.exec_())
