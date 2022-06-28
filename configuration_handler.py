import win32con, win32api

class ConfigurationHandler():
    def __init__(self):
        self.initConfiguration()

    def initConfiguration(self):
        try:
            configurationFile = open("config.txt", "r")
            self.defaultHotkey = configurationFile.read()
        except:
            configurationFile = open("config.txt", "w")
            win32api.SetFileAttributes("config.txt",win32con.FILE_ATTRIBUTE_HIDDEN)
            self.defaultHotkey = "control,alt,shift,o"
            configurationFile.write(self.defaultHotkey)
        finally:
            configurationFile.close()

    def readDefaultHotkey(self):
        return self.defaultHotkey.split(',')