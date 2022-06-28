import keyboard, mocking_flow as mf
import configuration_handler as ch
from global_hotkeys import *
from win10toast import ToastNotifier

mocking_flow = mf.MockingFlow()
configuration_handler = ch.ConfigurationHandler()

print("App started")

def displayNotification(toast, text):
     toast.show_toast(
        "Keyboard",
        text,
        duration = 1.5,
        threaded = True
    )

def onHotkey():
    print("Mocking started")
    toast = ToastNotifier()
    displayNotification(toast, "Mocking Enabled")
    mocking_flow.startMocking()
    displayNotification(toast, "Mocking Disabled")

hotkeyCollection = configuration_handler.readDefaultHotkey()

bindings = [
    [hotkeyCollection, None,  onHotkey]
]

register_hotkeys(bindings)
start_checking_hotkeys()

keyboard.wait()


        
