from setuptools import setup

APP = ['filename.py']  # This should be your Python script that contains the GUI
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['tkinter'],
    'plist': {
        'CFBundleName': 'Minecraft Server Launcher',
        'CFBundleDisplayName': 'Minecraft Server Launcher',
        'CFBundleIdentifier': 'com.jeadyce.serverlauncher',
        'CFBundleVersion': '0.1.0',
        'LSUIElement': False  # Important: Set False so the app opens a window
    },
}

setup(
    app=APP,
    name='Minecraft Server Launcher',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
