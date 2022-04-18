import sqlite3

class TemporaryDb(object):
    lastRow = 0
    keyState = None
    rowIdByUser = 0
    txtContent = ("")
    attachTextFile = False
    addTxtToEnd = True
    isDbClear = False
    isFormVisible = False

def createDb():
    c = sqlite3.connect("history.db")
    cursor = c.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS history (id INT, Receiver TEXT, Sender TEXT, Subject TEXT, Message TEXT, Datetime TEXT)")
    c.commit()
    
def clearDb():
    c = sqlite3.connect("history.db")
    cursor = c.cursor()
    cursor.execute("DELETE FROM history")
        
    c.commit()

def sendValueToDb(id, receiver, sender, subject, message, datetime):
    c = sqlite3.connect("history.db")
    cursor = c.cursor()
    cursor.execute("INSERT INTO history VALUES(?,?,?,?,?,?)", (id, receiver, sender, subject, message, datetime))
    
    c.commit()

def getValueFromDb():
    idList = []

    c = sqlite3.connect("history.db")
    cur = c.cursor()
    data = cur.execute("SELECT id FROM history")
    
    for row in data:
        idList.append(row)

    try:
        mx = max(idList)
        maxId = mx[0]
        TemporaryDb.lastRow = maxId
       
        cursor = c.cursor()
        cursor.execute("SELECT * FROM history WHERE id=?", (maxId,))
        
        rows = cursor.fetchall()
         
        for row in rows:
            return row
            
        c.commit()
    
    except ValueError:
        pass
        
def getValueFromDbById():
    try:
        c = sqlite3.connect("history.db")
        cursor = c.cursor()
        cursor.execute("SELECT * FROM history WHERE id=?", (TemporaryDb.rowIdByUser,))
        
        rows = cursor.fetchall()
        
        for row in rows:
            return row
          
        c.commit()
    
    except ValueError:
        pass
        
def getOnlyIdFromDb():
    idList = []

    c = sqlite3.connect("history.db")
    cur = c.cursor()
    data = cur.execute("SELECT id FROM history")
    
    for row in data:
        idList.append(row)

    try:
        mx = max(idList)
        maxId = mx[0]
        TemporaryDb.lastRow = maxId   

    except ValueError:
        pass
    
