import keyboard, mocking_flow as mf
from global_hotkeys import *

mocking_flow = mf.MockingFlow()

def mock():
    f = open(r"C:\Users\DaniloDjokic\Desktop\Logs.txt", "a")
    f.write("RADIM")
    f.close()

bindings = [
    [["control", "shift", "7"], None,  mock]
]

register_hotkeys(bindings)
start_checking_hotkeys()

while(True):
    pass