import keyboard, mocking_flow as mf

mocking_flow = mf.MockingFlow()

def waitForHotkey(hotkey):
    print("Starting")
    keyboard.wait(hotkey)
    return True

    
while(waitForHotkey('ctrl+shift+alt+o')):
   mocking_flow.startMocking()

        
