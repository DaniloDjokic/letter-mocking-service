import keyboard, mocking_flow as mf
from global_hotkeys import *

mocking_flow = mf.MockingFlow()

def waitForHotkey(hotkey):
    print("Starting")
    keyboard.wait(hotkey)
    return True

def onHotkey():
    mocking_flow.startMocking()

bindings = [
    [["control", "shift", "alt", "o"], None,  onHotkey]
]

register_hotkeys(bindings)
start_checking_hotkeys()

keyboard.wait()


        
