import json
import os

from redirector import consts

SETTINGS_FILE = f'{consts.storage_folder}/{consts.settings_file}'

os.makedirs(consts.storage_folder, exist_ok=True)

TELEGRAM = 'telegram'
ECHO_TEXT = 'echo_text'
ECHO_BUTTONS = 'echo_buttons'
settings = {
    TELEGRAM: '',
    ECHO_TEXT: '',
    ECHO_BUTTONS: [
        [
            {
                'text': '',
                'url': ''
            }
        ]
    ]
}

try:
    with open(SETTINGS_FILE, 'r', encoding="utf-8") as rf:
        read = rf.read()
        if read != '':
            settings = json.loads(read)
except IOError:
    with open(SETTINGS_FILE, 'w', encoding="utf-8") as file:
        json.dump(settings, file, sort_keys=True, indent=2)
    print("Insert tokens", flush=True)
    exit()
if settings[TELEGRAM] == '':
    print("Insert tokens", flush=True)
    exit()
