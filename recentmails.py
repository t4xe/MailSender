from PyQt5 import QtCore, QtGui, QtWidgets
import database

class RecentMails(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon("icon.ico"))
        self.setWindowTitle("Recent Mails")
        self.resize(300, 350)
        self.setMaximumSize(300, 350)
        self.setMinimumSize(300, 350)    
        
        self.mainFunc()
        
    def mainFunc(self):
        self.setWindowIcon(QtGui.QIcon("icons/icon.ico"))
       
        self.recentSenderLabel = QtWidgets.QLabel("Sender:")
        self.recentSenderLineEdit = QtWidgets.QLineEdit()
        self.recentSenderLineEdit.setFixedSize(275, 25)
        self.recentSenderLineEdit.setReadOnly(True)
            
        self.recentReceiverLabel = QtWidgets.QLabel("Receiver:")
        self.recentReceiverLineEdit = QtWidgets.QLineEdit()
        self.recentReceiverLineEdit.setFixedSize(275, 25)
        self.recentReceiverLineEdit.setReadOnly(True)
            
        self.recentSubjectLabel = QtWidgets.QLabel("Subject:")
        self.recentSubjectLineEdit = QtWidgets.QLineEdit() 
        self.recentSubjectLineEdit.setFixedSize(275, 25)
        self.recentSubjectLineEdit.setReadOnly(True)
            
        self.recentMessageLabel = QtWidgets.QLabel("Message:")
        self.recentMessageTextEdit = QtWidgets.QLineEdit()
        self.recentMessageTextEdit.setFixedSize(275, 50)
        self.recentMessageTextEdit.setReadOnly(True) 

        self.recentDateAndTimeLabel = QtWidgets.QLabel("Date:")
        self.recentDateAndTimeLineEdit = QtWidgets.QLineEdit()
        self.recentDateAndTimeLineEdit.setFixedSize(275, 25)
        self.recentDateAndTimeLineEdit.setReadOnly(True)
        
        self.selectIdLineEdit = QtWidgets.QLineEdit()
        self.selectIdLineEdit.setFixedSize(90, 25)
        self.selectIdLineEdit.setPlaceholderText("ID")
        self.refreshButton = QtWidgets.QPushButton("Refresh")
        self.refreshButton.setFixedSize(90, 21)
        self.clearDbButton = QtWidgets.QPushButton("Clear Database")
        self.clearDbButton.setFixedSize(90, 21)
        
        self.maxRowIdLabel = QtWidgets.QLabel("")
        
        self.selectIdLineEdit.setAlignment(QtCore.Qt.AlignLeft)
        
        database.getOnlyIdFromDb()
        if database.TemporaryDb.lastRow == 0:
            self.maxRowIdLabel.setText("Max ID: Not set")
        else:
            self.maxRowIdLabel.setText("Max ID: " + str(database.TemporaryDb.lastRow))

        layout = QtWidgets.QGridLayout()
        layout.addWidget((self.recentSenderLabel), 0, 0)
        layout.addWidget(self.recentSenderLineEdit)
        layout.addWidget((self.recentReceiverLabel), 2, 0)
        layout.addWidget(self.recentReceiverLineEdit)
        layout.addWidget((self.recentSubjectLabel), 4, 0)
        layout.addWidget(self.recentSubjectLineEdit)
        layout.addWidget((self.recentMessageLabel), 6, 0)
        layout.addWidget(self.recentMessageTextEdit)
        layout.addWidget((self.recentDateAndTimeLabel), 8, 0)
        layout.addWidget(self.recentDateAndTimeLineEdit)
        layout.addWidget((self.refreshButton), 10, 0)
        layout.addWidget((self.clearDbButton), 10, 1)
        layout.addWidget((self.selectIdLineEdit), 11, 0)
        layout.addWidget((self.maxRowIdLabel), 11, 1)
        self.setLayout(layout)
        self.refreshValues()        
        
        self.show() 
        
        self.refreshButton.clicked.connect(self.refreshRecentMails)
        self.clearDbButton.clicked.connect(self.clearDatabase)
            
    def refreshValues(self):
        try:
            historyValues = database.getValueFromDb()
            self.recentSenderLineEdit.setText(str(historyValues[1])) #0 = row id
            self.recentReceiverLineEdit.setText(str(historyValues[2]))
            self.recentSubjectLineEdit.setText(str(historyValues[3]))
            self.recentMessageTextEdit.setText(str(historyValues[4]))
            self.recentDateAndTimeLineEdit.setText(str(historyValues[5]))
            
            if database.TemporaryDb.lastRow == 0:
                self.maxRowIdLabel.setText("Max ID: Not set")
                database.TemporaryDb.isDbClear = True
            else:
                self.maxRowIdLabel.setText("Max ID: " + str(database.TemporaryDb.lastRow))
                database.TemporaryDb.isDbClear = False
        
        except TypeError:
            database.TemporaryDb.isDbClear = True
            self.recentSenderLineEdit.setText("Mail history not found.")
            self.recentReceiverLineEdit.setText("-")
            self.recentSubjectLineEdit.setText("-")
            self.recentMessageTextEdit.setText("-")
            self.recentDateAndTimeLineEdit.setText("-")
            
    def refreshRecentMails(self):
        firstLen = len(self.selectIdLineEdit.text())
        #print(database.TemporaryDb.isFormVisible)
        
        if firstLen != 0:
            database.TemporaryDb.rowIdByUser = self.selectIdLineEdit.text()
            try:
                historyValues = database.getValueFromDbById()
                self.recentSenderLineEdit.setText(str(historyValues[1])) #0 = row id
                self.recentReceiverLineEdit.setText(str(historyValues[2]))
                self.recentSubjectLineEdit.setText(str(historyValues[3]))
                self.recentMessageTextEdit.setText(str(historyValues[4]))
                self.recentDateAndTimeLineEdit.setText(str(historyValues[5]))
                
                if database.TemporaryDb.lastRow == 0:
                    self.maxRowIdLabel.setText("Max ID: Not set")
                    database.TemporaryDb.isDbClear = True
                else:
                    self.maxRowIdLabel.setText("Max ID: " + str(database.TemporaryDb.lastRow))
                    database.TemporaryDb.isDbClear = False
                
            except TypeError:
                database.TemporaryDb.isDbClear = True
                self.recentSenderLineEdit.setText("Mail history not found.")
                self.recentReceiverLineEdit.setText("-")
                self.recentSubjectLineEdit.setText("-")
                self.recentMessageTextEdit.setText("-")
                self.recentDateAndTimeLineEdit.setText("-")
                
    def clearDatabase(self):
        database.clearDb()
        
        self.maxRowIdLabel.setText("Max ID: Not set")