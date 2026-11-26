import pyautogui as pa
import time as t
message = input("What would u like to type to the code: ")
 # gives us a delay to find the location
print(pa.position()) # gives us the location so we can use it to create the macro

# pa.click(819,1052)
pa.click(1301,624)#clicks here
pa.click(1301,624)
pa.typewrite(message,0.04) # writes these letters with a delay of 1 second

pa.press('enter') # clickes a button
print(str(t.time()))