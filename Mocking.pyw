import keyboard, mocking_flow as mf
import configuration_handler as ch
from global_hotkeys import *

mocking_flow = mf.MockingFlow()
configuration_handler = ch.ConfigurationHandler()

print("App started")

def onHotkey():
    print("Mocking started")
    mocking_flow.startMocking()

hotkeyCollection = configuration_handler.readDefaultHotkey()

bindings = [
    [hotkeyCollection, None,  onHotkey]
]

register_hotkeys(bindings)
start_checking_hotkeys()

keyboard.wait()


        
