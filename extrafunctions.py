from win32api import GetKeyState
from win32con import VK_CAPITAL

def getCapsLockState():
    import database
    
    cks = GetKeyState(VK_CAPITAL)
    database.TemporaryDb.keyState = cks