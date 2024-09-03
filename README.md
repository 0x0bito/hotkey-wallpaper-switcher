# Wallpaper Changer Hotkey (Windows)

This script changes the desktop wallpaper when a specific key combination (Ctrl+Shift+K) is pressed.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/wallpaper-changer-hotkey.git

2. Navigate to the repository:
      `cd wallpaper-changer-hotkey`

3. Install the required Python package:
      `pip install keyboard`

## Setup

-   **Modify** `hotkey_listener.py` to set the correct directory for your wallpapers if necessary.
 The default is `C:/Users/<YourUsername>/Pictures/wallpapers`.

## Usage 

- Press `Ctrl + Shift + K` to change the desktop wallpaper.

## Running Without a Terminal Window
- Use pythonw.exe:
    - Rename the python script with a .pyw extension instead of .py.
    - This will run the script with pythonw.exe, which doesn't open a terminal window.
    - Example: hotkey_listener.pyw

## License 
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
