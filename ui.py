import raylib as rl
from pyray import * 
import pyautogui as pa
import time as t 
import keyboard
button_auto_click_text = "StartClick"
cps = 1
auto_click = False
mp = get_mouse_position()
mousebox = Rectangle(mp.x-2,mp.y-2,5,5)
class button:
    def __init__(self,width,height,function: function,px,py,text):
        self.width = width
        self.height = height 
        self.function = function
        self.px = px
        self.py= py
        self.text = text
        self.color = BLACK
        self.collider = Rectangle(self.px,self.py,self.width,self.height)
    def draw(self):
        draw_rectangle_rec(self.collider,self.color)
        draw_text(self.text,self.px+int(self.width/4),self.py+int(self.height/4),int((self.width/len(self.text)*1.3)),WHITE)
        if check_collision_recs(self.collider,mousebox):
            self.color = GRAY
        else:
            self.color = BLACK
    def check_click(self):
        if check_collision_recs(mousebox,self.collider) and is_mouse_button_pressed(rl.MOUSE_BUTTON_LEFT):
            self.function()
class cooldown:
    def __init__(self,cps):
        self.cps = cps
        self.frame = 0
    def start_timer(self):
        self.frame += 1
        if self.frame%60:
            self.fps = get_fps()
            
        frame_interval = self.fps / cps
        if self.frame >= frame_interval:
            self.frame = 0
            return True
        else:      
            return False
        


def increase_cps_small():
    global cps
    cps+=1
def decrease_cps_small():
    global cps
    if cps >0:
        cps-=1
def increase_cps_large():
    global cps
    cps+=10
def decrease_cps_large():
    global cps
    if cps >9:
        cps-=10
def start_auto_click():
    global button_auto_click_text
    global auto_click
    if auto_click == False:
        auto_click = True
        button_auto_click_text = "StopClick"
    elif auto_click == True:
        auto_click = False
        button_auto_click_text = "StartClick"
def track_inputs():
    print("tracking")
def run_track():
    print("running track")
def end_tracking():
    print("tracking ended")
color = RAYWHITE

#things to add
"""
a keystroke tracking and repeating software
run-once
run-loop until shortcut pressed
"""


pa.PAUSE = 0
run_track_button: button = button(100,50,run_track,300,400,"Run  ")
track_button: button = button(100,50,track_inputs,80,400,"track")
end_tracking_button:button = button(100,50,end_tracking,190,400,"End  ")
quit: button = button(100,50,close_window,185,625,"quit  ")
plus10:button = button(50,50,increase_cps_large,50,100,"+10")
plus1:button = button(50,50,increase_cps_small,125,100,"+1 ")
minus1:button = button(50,50,decrease_cps_small,325,100,"-1 ")
minus10:button = button(50,50,decrease_cps_large,400,100,"-10")
start_button: button = button(100,50,start_auto_click,185,210,button_auto_click_text)
click_cooldown = cooldown(cps)
set_target_fps(100)
init_window(500,700,"AutoClickerV1")
# set_window_icon() set this later if we want to make a proper gui
while not window_should_close():
    click_cooldown.cps = cps
    mp = get_mouse_position()
    mousebox = Rectangle(mp.x-2,mp.y-2,5,5)
    if is_cursor_on_screen() == True:

        draw_rectangle_rec(mousebox,BLACK)
        quit.check_click()
        plus10.check_click()
        plus1.check_click()
        minus1.check_click()
        minus10.check_click()
        start_button.check_click()
        track_button.check_click()
        run_track_button.check_click()
        end_tracking_button.check_click()
        start_button.text = button_auto_click_text
        if auto_click == False:
            button_auto_click_text = "StartClick"
        elif auto_click == True:
            button_auto_click_text = "StopClick"

            
    begin_drawing()
    clear_background(color)
    quit.draw()
    plus10.draw()
    plus1.draw()
    draw_text("cps: "+str(cps),185,110,30,BLACK)
    minus1.draw()
    minus10.draw()
    start_button.draw()
    track_button.draw()
    run_track_button.draw()
    end_tracking_button.draw()
    try:
        if auto_click == True:
            if click_cooldown.start_timer():
                pa.click()
    except ZeroDivisionError:
        print("you cannot set your cps to zero and start")
    if keyboard.is_pressed("esc"):
        auto_click = False


    end_drawing()

