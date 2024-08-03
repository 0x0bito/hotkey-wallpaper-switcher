# Wallpaper Changer Hotkey

This script changes the desktop wallpaper when a specific key combination (Ctrl+Shift+K) is pressed. It runs continuously in the background and can be set to start automatically with Windows.

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

- **Modify** `runner.bat` file to set the correct directory of `hotkey_listener.py`

- **Run** the `setup.py` script to add the `runner.bat` file to the Startup folder.

- **Restart the Computer** to ensure the script runs on startup. With these updates, don't forget to update `runner.bat` to the corresponding path of `hotkey_listener.py` script.

## Usage 

- Press `Ctrl + Shift + K` to change the desktop wallpaper.

## License 
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.