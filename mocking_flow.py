import keyboard

class MockingFlow():
    def __init__(self):
        self.flipFlag = False
        self.iPressed = False
        self.lPressed = False


    def mockLetter(self, event, key):
        if(event.event_type == keyboard.KEY_DOWN and len(key) == 1 and key.isalpha()): 
            if(self.flipFlag):
                keyboard.send('shift+' + event.name)
            else:
                keyboard.send(event.name)

            self.flipFlag = not self.flipFlag
            return True



    def handleStandardInput(self, event, key):
        if(event.event_type == keyboard.KEY_DOWN):
            keyboard.press(key)

        if(event.event_type == keyboard.KEY_UP):
            keyboard.release(key)


    def handleICase(self):
        self.iPressed = True
        if(self.lPressed):
            keyboard.send("i")
            self.lPressed = False
            return True

        self.lPressed = False
        return False
        
    def handleLCase(self):
        self.lPressed = True
        if(self.iPressed):
            keyboard.send("shift+l")
            self.iPressed = False
            return True

        self.iPressed = True
        return False
        
    def startMocking(self):
        while(True):
            event = keyboard.read_event(True)

            key = str(event.name)

            if(key == "esc"):
                break

            if(event.event_type == keyboard.KEY_DOWN):
                if(key == "i"):
                    if(self.handleICase()):
                        continue
                elif(key == "l"):
                    if(self.handleLCase()):
                        continue
                else:
                    self.lPressed = False
                    self.iPressed = False

            if(self.mockLetter(event, key)):
                continue

            self.handleStandardInput(event, key)