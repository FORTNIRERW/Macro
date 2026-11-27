import pyautogui as pa
from pynput.keyboard import Key,Listener
pressed = []
keys = ['a','b','c']
def press(key):
    print((key))
def release(key):
    print((key+"released"))

with Listener(on_press=press,on_release=release) as listener:
    listener.join()

