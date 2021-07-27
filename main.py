#Mail Sender v0.8 by t4xe.
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import smtplib

class Ui_Form(object):
    def setupUi(self, Form):   
        Form.setObjectName("Form")
        Form.resize(499, 290)
        self.receiverLabel = QtWidgets.QLabel(Form)
        self.receiverLabel.setGeometry(QtCore.QRect(20, 20, 61, 20))
        self.receiverLabel.setObjectName("receiverLabel")
        self.subjectLabel = QtWidgets.QLabel(Form)
        self.subjectLabel.setGeometry(QtCore.QRect(20, 60, 61, 21))
        self.subjectLabel.setObjectName("subjectLabel")
        self.messageLabel = QtWidgets.QLabel(Form)
        self.messageLabel.setGeometry(QtCore.QRect(20, 100, 61, 21))
        self.messageLabel.setObjectName("messageLabel")
        self.senderLabel = QtWidgets.QLabel(Form)
        self.senderLabel.setGeometry(QtCore.QRect(300, 20, 47, 21))
        self.senderLabel.setObjectName("senderLabel")
        self.passwordLabel = QtWidgets.QLabel(Form)
        self.passwordLabel.setGeometry(QtCore.QRect(300, 50, 51, 21))
        self.passwordLabel.setObjectName("passwordLabel")
        self.sentOrErrorLabel = QtWidgets.QLabel(Form)
        self.sentOrErrorLabel.setGeometry(QtCore.QRect(110, 240, 250, 21))
        self.sentOrErrorLabel.setText("")
        self.sentOrErrorLabel.setObjectName("sentOrErrorLabel")
        self.receiverLineEdit = QtWidgets.QLineEdit(Form)
        self.receiverLineEdit.setGeometry(QtCore.QRect(70, 20, 131, 21))
        self.receiverLineEdit.setObjectName("receiverLineEdit")
        self.subjectLineEdit = QtWidgets.QLineEdit(Form)
        self.subjectLineEdit.setGeometry(QtCore.QRect(70, 60, 131, 21))
        self.subjectLineEdit.setObjectName("subjectLineEdit")
        self.messageTextEdit = QtWidgets.QTextEdit(Form)
        self.messageTextEdit.setGeometry(QtCore.QRect(70, 100, 131, 81))
        self.messageTextEdit.setObjectName("messageTextEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 240, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.senderLineEdit = QtWidgets.QLineEdit(Form)
        self.senderLineEdit.setGeometry(QtCore.QRect(350, 20, 131, 21))
        self.senderLineEdit.setObjectName("senderLineEdit")
        self.passwordLineEdit = QtWidgets.QLineEdit(Form)
        self.passwordLineEdit.setGeometry(QtCore.QRect(350, 50, 131, 21))
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.showPasswordBox = QtWidgets.QCheckBox(Form)
        self.showPasswordBox.setGeometry(QtCore.QRect(300, 80, 111, 17))
        self.showPasswordBox.setObjectName("showPasswordBox")
        self.dateAndTimeLabel = QtWidgets.QLabel(Form)
        self.dateAndTimeLabel.setGeometry(QtCore.QRect(10, 270, 140, 21))     
        self.dateAndTimeLabel.setObjectName("dateAndTimeLabel")        

        self.pushButton.clicked.connect(self.sendMail)      
        self.showPasswordBox.stateChanged.connect(self.showPwStateChanged)
        
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        dateAndTime = datetime.now()
        currentDate = datetime.strftime(dateAndTime, "%D")
    
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Mail Sender"))
        self.receiverLabel.setText(_translate("Form", "Receiver:"))
        self.subjectLabel.setText(_translate("Form", "Subject:"))
        self.messageLabel.setText(_translate("Form", "Message:"))
        self.senderLabel.setText(_translate("Form", "Sender:"))
        self.passwordLabel.setText(_translate("Form", "Password:"))
        self.pushButton.setText(_translate("Form", "Send"))
        self.showPasswordBox.setText(_translate("Form", "Show Password"))  
        self.dateAndTimeLabel.setText(_translate("Form", "Date: " + currentDate))
        
    def sendMail(self):
        firstLen = len(self.receiverLineEdit.text())
        secondLen = len(self.messageTextEdit.toPlainText())
        thirdLen = len(self.subjectLineEdit.text())
        fourthLen = len(self.senderLineEdit.text())
        fifthLen = len(self.passwordLineEdit.text())
         
        sender = self.senderLineEdit.text()
        receiver = self.receiverLineEdit.text()
        if firstLen and secondLen and thirdLen and fourthLen and fifthLen != 0:
            if "@" and ".com" in receiver and "@" and ".com" in sender:
                try: 
                    sender = self.senderLineEdit.text()
                    password = self.passwordLineEdit.text()
                    receiver = self.receiverLineEdit.text()
                    subject = self.subjectLineEdit.text()
                    messageText = self.messageTextEdit.toPlainText()
                        
                    smtp = smtplib.SMTP('smtp.gmail.com', 587) 
                    smtp.ehlo()
                    smtp.starttls() 
                    smtp.ehlo()
                        
                    smtp.login(sender, password)               
                    message = ("Subject: " + subject + "\n" + messageText)         
                    smtp.sendmail(sender, receiver, message.encode("utf8"))
                             
                    self.sentOrErrorLabel.setText("Email sent.")
                    smtp.quit()
                except smtplib.SMTPAuthenticationError as e:
                    self.sentOrErrorLabel.setText("Username and password does not match.")
                    print(str(e) + "\nIf you can't solve the problem, please contact with me by T4XE#0610 discord address.")
                except smtplib.SMTPServerDisconnected as e:
                    self.sentOrErrorLabel.setText("Server unexpectedly disconnected.")
                    print(str(e) + "\nIf you can't solve the problem, please contact with me by T4XE#0610 discord address.")
                except smtplib.SMTPDataError as e:
                    self.sentOrErrorLabel.setText("The SMTP server refused to accept the message data.")
                    print(str(e) + "\nIf you can't solve the problem, please contact with me by T4XE#0610 discord address.")         
                except Exception as e:
                    self.sentOrErrorLabel.setText("An unexpected error occured. Please read the console.")
                    print(str(e) + "\nIf you can't solve the problem, please contact with me by T4XE#0610 discord address.")
            else:
                self.sentOrErrorLabel.setText("Please enter correct addresses.")                    
        else:
            self.sentOrErrorLabel.setText("Please fill all fields.")
            
    def showPwStateChanged(self):
        if self.showPasswordBox.isChecked():
            self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
