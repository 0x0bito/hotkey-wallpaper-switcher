import os
import keyboard
import ctypes
import random


def is_exist(arr, n):
    for ele in arr:
        if (ele == n):
            return 1
    return 0


def change_wallpaper():
    wallpaper_dir = f"C:\\Users\\{os.getlogin()}\\Pictures\\wallpapers"
    wallpapers = os.listdir(wallpaper_dir)

    random_i = random.randint(0, len(wallpapers)) - 1
    image = os.path.join(wallpaper_dir, wallpapers[random_i])
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image, 0)




hotkey = "ctrl+shift+k"
keyboard.add_hotkey(hotkey, change_wallpaper)

print(f'Listening for hotkey: {hotkey}')
keyboard.wait('esc')  # Press 'esc' to stop the script