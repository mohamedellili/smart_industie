# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lampe_externe1.ui'
#
# Created: Tue May 08 09:48:33 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
#######################################################################
from config import*
import pyrebase


firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password(mail, password)

# Get a reference to the database service
db = firebase.database()





def stream_handler(message):

    print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}
    #global EtatLampe1
    if  str(message["data"])== '0':
       # EtatLampe1= 'OFF'
        ui.Set_EtatLampe("OFF")
    elif str(message["data"])== '1':
        ui.Set_EtatLampe("ON")
        #EtatLampe1='ON'
    #ui.Set_EtatLampe1(EtatLampe1)

my_stream = db.child("Controle/LampExt").stream(stream_handler)


################################################################################

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(329, 188)
        Form.move(1000,255)
        Form.setStyleSheet(_fromUtf8("QWidget{\n"
"\n"
"background-color: #121254 ;}\n"
""))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 10, 241, 51))
        self.label.setStyleSheet(_fromUtf8("QLabel{\n"
"   color: #00bfff;\n"
"  \n"
"   \n"
"   \n"
"   -webkit-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   -moz-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   text-shadow: rgba(0,0,0,.4) 0 1px 0;\n"
"   color: #FFFFFF;\n"
"   font-size: 29px;\n"
"   font-family: Algerian;\n"
"   text-decoration: none;\n"
"   \n"
"}"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 81, 81))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/lamp64.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 201, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia,serif"))
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(_fromUtf8("QLabel{\n"
"   \n"
"  \n"
"   \n"
"   \n"
"   -webkit-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   -moz-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   text-shadow: rgba(0,0,0,.4) 0 1px 0;\n"
"   color: #66FFFF ;\n"
"   font-size: 17px;\n"
"   font-family: Georgia, serif;\n"
"   text-decoration: none;\n"
"   \n"
"}"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_etat_lampe_externe = QtGui.QLabel(Form)
        self.label_etat_lampe_externe.setGeometry(QtCore.QRect(220, 70, 61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Georgia,serif"))
        font.setPointSize(-1)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.label_etat_lampe_externe.setFont(font)
        self.label_etat_lampe_externe.setStyleSheet(_fromUtf8("QLabel{\n"
"   color: rgb(255, 255, 255);\n"
"  \n"
"   \n"
"   \n"
"   -webkit-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   -moz-box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   box-shadow: rgba(0,0,0,1) 0 1px 0;\n"
"   text-shadow: rgba(0,0,0,.4) 0 1px 0;\n"
"   color: rgb(255, 255, 255);\n"
"   font-size: 17px;\n"
"   font-family: Georgia, serif;\n"
"   text-decoration: none;\n"
"   \n"
"}"))
        self.label_etat_lampe_externe.setObjectName(_fromUtf8("label_etat_lampe_externe"))
        self.btn_on_lampe_externe = QtGui.QPushButton(Form)
        self.btn_on_lampe_externe.setGeometry(QtCore.QRect(120, 130, 71, 41))
        self.btn_on_lampe_externe.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_on_lampe_externe.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background: #ffc100 ;\n"
"  background-image: -webkit-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -moz-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -ms-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -o-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: linear-gradient(to bottom, #4a4f96, #2d95d6);\n"
"  -webkit-border-radius: 20;\n"
"  -moz-border-radius: 20;\n"
"  border-radius: 20px;\n"
"  text-shadow: 10px 1px 3px #666666;\n"
"  font-family: Georgia;\n"
"  color: #2ac83e;\n"
"  font-size: 15px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"QPushButton:hover {\n"
"  background: #4f5a64;\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #3498db);\n"
"  text-decoration: none;\n"
"}\n"
"\n"
""))
        self.btn_on_lampe_externe.setObjectName(_fromUtf8("btn_on_lampe_externe"))
###############################################################################################
        self.btn_on_lampe_externe.clicked.connect(self.LampeON)
###############################################################################################
        self.btn_off_lampe_externe = QtGui.QPushButton(Form)
        self.btn_off_lampe_externe.setGeometry(QtCore.QRect(220, 130, 71, 41))
        self.btn_off_lampe_externe.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_off_lampe_externe.setStyleSheet(_fromUtf8("QPushButton {\n"
"  background:  #ffc100 ;\n"
"  background-image: -webkit-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -moz-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -ms-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: -o-linear-gradient(top, #4a4f96, #2d95d6);\n"
"  background-image: linear-gradient(to bottom, #4a4f96, #2d95d6);\n"
"  -webkit-border-radius: 20;\n"
"  -moz-border-radius: 20;\n"
"  border-radius: 20px;\n"
"  text-shadow: 10px 1px 3px #666666;\n"
"  font-family: Georgia;\n"
"  color: #FF0000;\n"
"  font-size: 15px;\n"
"  padding: 10px 20px 10px 20px;\n"
"  text-decoration: none;\n"
"}\n"
"QPushButton:hover {\n"
"  background: #4f5a64;\n"
"  background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: -o-linear-gradient(top, #3cb0fd, #3498db);\n"
"  background-image: linear-gradient(to bottom, #3cb0fd, #3498db);\n"
"  text-decoration: none;\n"
"}\n"
"\n"
""))
        self.btn_off_lampe_externe.setIconSize(QtCore.QSize(80, 8))
        self.btn_off_lampe_externe.setObjectName(_fromUtf8("btn_off_lampe_externe"))
###############################################################################################
        self.btn_off_lampe_externe.clicked.connect(self.LampeOFF)
###############################################################################################

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Lampe Externe", None))
        self.label.setText(_translate("Form", "Lampe Externe", None))
        self.label_3.setText(_translate("Form", "L\'état actuel de la lampe :", None))
        self.label_etat_lampe_externe.setText(_translate("Form", "ON", None))
        self.btn_on_lampe_externe.setText(_translate("Form", "ON", None))
        self.btn_off_lampe_externe.setText(_translate("Form", "OFF", None))
#############################################################################################
    def Set_EtatLampe(self,s):
##        global EtatLampe1
##        s = EtatLampe1
        self.label_etat_lampe_externe.setText(s)


    def LampeON(self):
        print("lampe on")
        db.child("Controle").update({'LampExt':'1'})
    
    def LampeOFF(self):
        print("lampe off")
        db.child("Controle").update({'LampExt':'0'})
##############################################################################################
import photos_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

