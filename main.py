#Mail Sender v2.1 by t4xe.
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import datetime
import locale
import recentmails
import smtplib
import database

database.createDb()

class Ui_Form(object):
    def setupUi(self, Form):  
        Form.setObjectName("Form")
        Form.resize(475, 360)
        Form.setMaximumSize(475, 360)
        Form.setMinimumSize(475, 360)
        
        Form.setWindowIcon(QtGui.QIcon("icons/icon.ico"))
        self.firstPixLabel = 10
        self.secondPixLabel = 270
        self.thirdPixLabel = 110
        self.fourthPixLabel = 450
        self.recentMailsHidden = True
        self.isDarkModeOn = False
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.getCapsLockState)
        self.timer.start(10)
        
        self.sentOrErrorLabel = QtWidgets.QLabel("", Form)
        self.sentOrErrorLabel.setGeometry(QtCore.QRect(self.thirdPixLabel, 315, 300, 25))
        self.sentOrErrorLabel.setObjectName("sentOrErrorLabel")
        
        self.receiverLineEdit = QtWidgets.QLineEdit(Form)
        self.receiverLineEdit.setGeometry(QtCore.QRect(self.firstPixLabel, 20, 171, 25))
        self.receiverLineEdit.setObjectName("receiverLineEdit")
        self.receiverLineEdit.setPlaceholderText("Receiver")
        
        self.subjectLineEdit = QtWidgets.QLineEdit(Form)
        self.subjectLineEdit.setGeometry(QtCore.QRect(self.firstPixLabel, 60, 171, 25))
        self.subjectLineEdit.setObjectName("subjectLineEdit")
        self.subjectLineEdit.setPlaceholderText("Subject")
        
        self.messageTextEdit = QtWidgets.QTextEdit(Form)
        self.messageTextEdit.setGeometry(QtCore.QRect(self.firstPixLabel, 100, 171, 121))
        self.messageTextEdit.setObjectName("messageTextEdit")
        self.messageTextEdit.setPlaceholderText("Message")
        
        self.sendMailPushButton = QtWidgets.QPushButton(Form)
        self.sendMailPushButton.setGeometry(QtCore.QRect(self.firstPixLabel, 315, 75, 23))
        self.sendMailPushButton.setObjectName("sendMailPushButton")      
        
        self.txtPathPushButton = QtWidgets.QPushButton(Form)
        self.txtPathPushButton.setGeometry(QtCore.QRect(self.firstPixLabel, 240, 100, 23))
        self.txtPathPushButton.setObjectName("txtPathPushButton")
        
        self.senderLineEdit = QtWidgets.QLineEdit(Form)
        self.senderLineEdit.setGeometry(QtCore.QRect(self.secondPixLabel, 20, 171, 25))
        self.senderLineEdit.setObjectName("senderLineEdit")
        self.senderLineEdit.setPlaceholderText("Sender")
        
        self.passwordLineEdit = QtWidgets.QLineEdit(Form)
        self.passwordLineEdit.setGeometry(QtCore.QRect(self.secondPixLabel, 50, 171, 25))
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.passwordLineEdit.setPlaceholderText("Password")
        
        self.showPasswordBox = QtWidgets.QCheckBox(Form)
        self.showPasswordBox.setGeometry(QtCore.QRect(self.secondPixLabel, 78, 121, 21))
        self.showPasswordBox.setObjectName("showPasswordBox")
        
        self.dateAndTimeLabel = QtWidgets.QLabel(Form)
        self.dateAndTimeLabel.setGeometry(QtCore.QRect(self.firstPixLabel, 340, 200, 21))
        self.dateAndTimeLabel.setObjectName("dateAndTimeLabel")

        self.themeCheckBox = QtWidgets.QCheckBox(Form)
        self.themeCheckBox.setGeometry(QtCore.QRect(self.secondPixLabel, 102, 121, 21))
        self.themeCheckBox.setObjectName("themeCheckBox")  

        self.txtPathDialog = QtWidgets.QDialog(Form)
        self.txtPathDialog.resize(300, 120) #w, h
        self.txtPathDialog.setWindowTitle("Attach Text File")
        self.txtPathDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.txtPathDialog.setWindowFlag(QtCore.Qt.WindowContextHelpButtonHint, False)
        
        self.txtPathLineEdit = QtWidgets.QLineEdit(self.txtPathDialog)
        self.txtPathLineEdit.setGeometry(QtCore.QRect(10, 20, 250, 25))
        self.txtPathLineEdit.setPlaceholderText("Enter the path here")
        
        self.txtPathAttachPushButton = QtWidgets.QPushButton("Attach File", self.txtPathDialog)
        self.txtPathAttachPushButton.setGeometry(QtCore.QRect(10, 90, 100, 23))    

        self.pathFoundOrErrorLabel = QtWidgets.QLabel("", self.txtPathDialog)
        self.pathFoundOrErrorLabel.setGeometry(QtCore.QRect(150, 90, 120, 23))
        
        self.txtAddToEnd = QtWidgets.QCheckBox("Add text file to end", self.txtPathDialog)
        self.txtAddToEnd.setGeometry(QtCore.QRect(10, 60, 151, 21))

        self.showOrHideRecentButton = QtWidgets.QPushButton(Form)
        self.showOrHideRecentButton.setGeometry(QtCore.QRect(360, 330, 110, 23))
        self.showOrHideRecentButton.setObjectName("showOrHideRecentButton")
        
        self.capsLockStatePic = QtWidgets.QLabel(Form)
        self.capsLockStatePic.setGeometry(QtCore.QRect(self.fourthPixLabel, 50, 24, 24))
        self.capsLockStatePic.setPixmap(QtGui.QPixmap("icons/capsonimg.png"))
        self.capsLockStatePic.hide()
        
        self.sendMailPushButton.clicked.connect(self.sendMail)
        self.showOrHideRecentButton.clicked.connect(self.showOrHideRecentMails)
        self.txtPathPushButton.clicked.connect(self.txtFileAttachment)
        self.txtPathAttachPushButton.clicked.connect(self.attachTextFile)
        self.txtAddToEnd.stateChanged.connect(self.addTxtToEndState)
        self.showPasswordBox.stateChanged.connect(self.showPwStateChanged)  
        self.themeCheckBox.stateChanged.connect(self.themeCheckBoxStateChanged)          
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        curLocale = locale.getlocale()
        locale.setlocale(locale.LC_TIME, curLocale)
        dateAndTime = datetime.now()
        currentDate = datetime.strftime(dateAndTime, "%D %X") 
        capsLockOnOff = ("")

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Mail Sender"))
        self.sendMailPushButton.setText(_translate("Form", "Send"))
        self.showPasswordBox.setText(_translate("Form", "Show Password"))  
        self.dateAndTimeLabel.setText(_translate("Form", "Date: " + currentDate))  
        self.themeCheckBox.setText(_translate("Form", "Dark Mode"))
        self.showOrHideRecentButton.setText(_translate("Form", "Show Recent Mails"))
        self.txtPathPushButton.setText(_translate("Form", "Attach Text File"))
        
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
                    import sqlite3           
                    curLocale = locale.getlocale()
                    locale.setlocale(locale.LC_TIME, curLocale)
                    dateAndTime = datetime.now()
                    currentDate = datetime.strftime(dateAndTime, "%D %X")
                     
                    sender = self.senderLineEdit.text()
                    password = self.passwordLineEdit.text()
                    receiver = self.receiverLineEdit.text()
                    subject = self.subjectLineEdit.text()
                    messageText = self.messageTextEdit.toPlainText()
                        
                    smtplib.smtp = smtplib.SMTP('smtp.gmail.com', 587)
                    smtplib.smtp.ehlo()
                    smtplib.smtp.starttls()
                    smtplib.smtp.ehlo()
                        
                    smtplib.smtp.login(sender, password)     
                     
                    if database.TemporaryDb.attachTextFile:
                        if database.TemporaryDb.addTxtToEnd:
                            message = ("Subject: " + subject + "\n" + messageText + "\n" + database.TemporaryDb.txtContent)
                        else:
                            message = ("Subject: " + subject + "\n" + database.TemporaryDb.txtContent + "\n" + messageText)
                    else:
                        message = ("Subject: " + subject + "\n" + messageText)    
                        
                    smtplib.smtp.sendmail(sender, receiver, message.encode("utf8"))
     
                    if database.TemporaryDb.isDbClear == True:              
                        database.sendValueToDb(1, receiver, sender, subject, messageText, currentDate)
                    else:
                        lRow = database.TemporaryDb.lastRow
                        lRow += 1
                        database.sendValueToDb(lRow, receiver, sender, subject, messageText, currentDate) 
                        
                    self.sentOrErrorLabel.setText("Email sent.")
                    RecentMails.refreshValues()
                    RecentMails.refreshRecentMails()
                    smtplib.smtp.quit()           
                except smtplib.SMTPAuthenticationError as e:
                    self.sentOrErrorLabel.setText("Username and password does not match.")
                    print(str(e) + "\nIf you can't solve the problem, please contact with me by T4XE#0610 discord address.")
                except smtplib.SMTPServerDisconnected as e:
                    self.sentOrErrorLabel.setText("Server unexpectedly disconnected.")
                    print(str(e) + "\nIf you can't solve the problem, please contact with me by T4XE#0610 discord address.")
                except smtplib.SMTPDataError as e:
                    self.sentOrErrorLabel.setText("The SMTP server refused to accept the message data.")
                    print(str(e) + "\nIf you can't solve the problem, please contact with me by T4XE#0610 discord address.") 
                except smtplib.SMTPSenderRefused as e:
                    self.sentOrErrorLabel.setText("Sender address refused.")
                    print(str(e) + "\nIf you can't solve the problem, please contact with me by T4XE#0610 discord address.") 
                except smtplib.SMTPRecipientsRefused as e:
                    self.sentOrErrorLabel.setText("All recipient addresses refused.")
                    print(str(e) + "\nIf you can't solve the problem, please contact with me by T4XE#0610 discord address.") 
                except smtplib.SMTPNotSupportedError as e:
                    self.sentOrErrorLabel.setText("The command or option attempted is not supported by the server.")
                    print(str(e) + "\nIf you can't solve the problem, please contact with me by T4XE#0610 discord address.") 
                except smtplib.SMTPConnectError as e:
                    self.sentOrErrorLabel.setText("Error occurred during connection.")
                    print(str(e) + "\nIf you can't solve the problem, please contact with me by T4XE#0610 discord address.")  
                except smtplib.SMTPHeloError as e:
                    self.sentOrErrorLabel.setText("The server refused our HELO message.")
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

    def themeCheckBoxStateChanged(self):
        lightTheme = (open("lightTheme.qss", "r").read())
        darkTheme = (open("darkTheme.qss", "r").read())
        if self.themeCheckBox.isChecked():
            app.setStyleSheet(darkTheme)
            self.isDarkModeOn = True
        else:
            app.setStyleSheet(lightTheme)
            self.isDarkModeOn = False
            
    def showOrHideRecentMails(self):
        if self.recentMailsHidden == False:
            RecentMails.show()
            self.recentMailsHidden = True
        else:
            RecentMails.hide()
            self.recentMailsHidden = False
            
    def getCapsLockState(self):
        from extrafunctions import getCapsLockState
        database.TemporaryDb.isFormVisible = Form.isVisible()
        getCapsLockState()
        
        if self.isDarkModeOn == False:
            self.capsLockStatePic.setPixmap(QtGui.QPixmap("icons/capsonimg.png"))
        else:
            self.capsLockStatePic.setPixmap(QtGui.QPixmap("icons/capsonimgdark.png"))
        
        if database.TemporaryDb.keyState == 0:
            self.capsLockStatePic.hide()
        else:
            self.capsLockStatePic.show()
            
        if database.TemporaryDb.isFormVisible == False:
            RecentMails.close()
            
        curLocale = locale.getlocale()
        locale.setlocale(locale.LC_TIME, curLocale)
        dateAndTime = datetime.now()
        currentDate = datetime.strftime(dateAndTime, "%D %X") 
        self.dateAndTimeLabel.setText("Date: " + currentDate)
        
    def txtFileAttachment(self):
        self.txtPathDialog.exec_()
        
    def attachTextFile(self):
        filePath = self.txtPathLineEdit.text()
        
        try:
            if filePath.endswith(".txt") and len(filePath) >= 4:
                with open(f'{filePath}', encoding="utf8") as f:
                    content = f.read()
                    database.TemporaryDb.txtContent = content
                    database.TemporaryDb.attachTextFile = True
                    self.pathFoundOrErrorLabel.setText("File attached.")
            elif len(filePath) < 4:
                self.pathFoundOrErrorLabel.setText("File path is too short.")
            else:
                self.pathFoundOrErrorLabel.setText("Only .txt files allowed.")
                
        except FileNotFoundError:
            self.pathFoundOrErrorLabel.setText("File not found.")
        except PermissionError:
            self.pathFoundOrErrorLabel.setText("Permission denied.")
    
    def addTxtToEndState(self):
        if self.txtAddToEnd.isChecked():
            database.TemporaryDb.addTxtToEndState = True
        else:
            database.TemporaryDb.addTxtToEndState = False
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RecentMails = recentmails.RecentMails()
    RecentMails.hide()
    Form = QtWidgets.QWidget()
    app.setStyleSheet(open("lightTheme.qss", "r").read())
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

