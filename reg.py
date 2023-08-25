import winreg
import sys

def is_registered_startup():
    reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    key = winreg.OpenKey(reg, "SOFTWARE\Microsoft\Windows\CurrentVersion\Run")
    
    try:
        data = winreg.QueryValueEx(key, "SpouseAlarm")

        if data[0] == sys.executable:
            return True
        else:
            return False
    except:
        return False

def set_startup():
    reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    key = winreg.CreateKey(reg, "SOFTWARE\Microsoft\Windows\CurrentVersion\Run")
    
    try:
        winreg.SetValueEx(key, "SpouseAlarm", 0, winreg.REG_SZ, sys.executable)
    except:
        pass

def clean_startup():
    reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
    key = winreg.CreateKey(reg, "SOFTWARE\Microsoft\Windows\CurrentVersion\Run")

    try:
        winreg.DeleteValue(key, "SpouseAlarm")
    except:
        pass