import keyboard, mocking_flow as mf
from global_hotkeys import *

mocking_flow = mf.MockingFlow()

bindings = [
    [["control", "shift", "7"], None,  mock]
]

register_hotkeys(bindings)
start_checking_hotkeys()

while(True):
    pass