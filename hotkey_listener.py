import os
import keyboard
import ctypes
import random


def change_wallpaper():
    wallpaper_dir = f"C:\\Users\\{os.getlogin()}\\Pictures\\wallpapers"
    wallpapers = os.listdir(wallpaper_dir)

    image = os.path.join(wallpaper_dir, random.choice(wallpapers))
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 0)


hotkey = "ctrl+shift+k"
keyboard.add_hotkey(hotkey, change_wallpaper)

print(f'Listening for hotkey: {hotkey}')
keyboard.wait('esc')  # Press 'esc' to stop the script
