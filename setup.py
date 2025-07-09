from setuptools import setup

APP = ['launcher.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',  # optional
    'packages': [],
    'plist': {
        'CFBundleName': 'Minecraft Server Launcher',
        'CFBundleShortVersionString': '1.0',
        'CFBundleIdentifier': 'com.jeadyce.minecraftlauncher',
    },
}

setup(
    app=APP,
    name='Minecraft Server Launcher',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
