import os
import shutil

def add_to_startup(file_path):
    # Get the path to the Startup folder
    startup_dir = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    
    # Copy the batch file to the Startup folder
    try:
        shutil.copy(file_path, startup_dir)
        print(f'Successfully copied {file_path} to {startup_dir}')
    except Exception as e:
        print(f'Failed to copy {file_path} to {startup_dir}: {e}')

if __name__ == "__main__":
    batch_file_path = os.path.join(os.path.dirname(__file__), 'runner.bat')
    add_to_startup(batch_file_path)