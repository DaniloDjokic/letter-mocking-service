import keyboard, mocking_flow as mf
import configuration_handler as ch
from global_hotkeys import *
from win10toast import ToastNotifier
from pathlib import Path

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

mocking_flow = mf.MockingFlow()
configuration_handler = ch.ConfigurationHandler()

print("App started")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def displayNotification(toast, text):
    toast.show_toast(
        "Keyboard",
        text,
        icon_path=relative_to_assets('../assets/icon.ico'),
        duration = 1.5,
        threaded = True,
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


        
