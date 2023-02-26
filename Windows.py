import psutil
import time
import win32gui
import pypresence
import pygetwindow as gw
import keyboard
import win32con
import win32process
import win32api
import fade
import os

client_id = '1079165392536223878'
RPC = pypresence.Presence(client_id)
start_time = time.time()
RPC.connect()

text = ("""
 _       ___           __                      ____  ____  ______
| |     / (_)___  ____/ /___ _      _______   / __ \/ __ \/ ____/
| | /| / / / __ \/ __  / __ \ | /| / / ___/  / /_/ / /_/ / /     
| |/ |/ / / / / / /_/ / /_/ / |/ |/ (__  )  / _, _/ ____/ /___   
|__/|__/_/_/ /_/\__,_/\____/|__/|__/____/  /_/ |_/_/    \____/   
             
                         connected btw
                             v0.1                                                                                 
""")
os.system("mode con: cols=65 lines=13 && cls")
faded_text = fade.purplepink(text)
print(faded_text)

apps = ["Brave", "Chrome", "Firefox", "Edge", "Audacity", "Filmora", "OBS", "Spotify", "Notepad", "Discord", "cmd", "Minecraft", "Lunar", "Badlion",
"Roblox", "CSGO", "Sublime", "Bandicam", "FLStudio", "Opera", "Powershell", "Vegas", "DuckDuckGo", "Calc", "Steam", "Bloc", "ShareX", "Notepad",
"TeamSpeak3", "Gimp"]

typing = False
active_window = None
window_title = ""
typing_timeout = 1

def on_key_pressed(event):
    global typing
    typing = True
    global typing_timer
    typing_timer = time.time()

keyboard.on_press(on_key_pressed)

while True:
    try:
        new_window = gw.getActiveWindow()
        if new_window is not None and new_window != active_window:
            active_window = new_window
            window_title = active_window.title.lower() 
            app = "idle"
            for app_name in apps:
                if app_name.lower() in window_title:
                    app = app_name.lower()
                    break
            RPC.update(
                details=f"Typing: {typing}",
                state=f"Active in {app}", 
                start=start_time,
                large_image=f"{app}",
                large_text=f"{window_title}",
                small_image="windows",
                small_text="Windows Presence v0.1"
            )
        elif new_window is None and active_window is not None:
            active_window = None
            window_title = ""
            typing = False
            RPC.update(
                details=f"Typing: False",
                state=f"Active in {app}", 
                start=start_time,
                large_image=f"{app}",
                large_text=f"{window_title}",
                small_image="windows",
                small_text="Windows Presence v0.1"
            )
        elif typing:
            typing_timer_diff = time.time() - typing_timer
            if typing_timer_diff >= typing_timeout:
                typing = False
            RPC.update(
                details=f"Typing: {typing}",
                state=f"Active in {app}", 
                start=start_time,
                large_image=f"{app}",
                large_text=f"{window_title}",
                small_image="windows",
                small_text="Windows Presence v0.1"
            )
        else:
            time.sleep(1)
    except:
        pass
