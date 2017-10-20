'''

SPEEDTEST-SHEET
Created by Jake

PYTHON: 3.6+

'''

# IMPORT
import os
import json
import gspread

from oauth2client.service_account import ServiceAccountCredentials as SAC

# VARIABLES
OAUTH_SCOPE = ['https://spreadsheets.google.com/feeds']
CREDENTIALS = SAC.from_json_keyfile_name('credits.json', OAUTH_SCOPE)
GOOGLE_CREDS = gspread.authorize(CREDENTIALS)
CONFIG = json.load(open('config.json'))

# CONFIG
SHEET = GOOGLE_CREDS.open_by_url(CONFIG['spreadsheet']['url'])
WORKSHEET = SHEET.worksheet(CONFIG['spreadsheet']['sheet'])

def first_empty_row(worksheet):
    """Gathers the first empty row in the given worksheet.

    Args:
        worksheet - The given worksheet in which you want the last row of.

    Returns:
        int - An integer which represents the last empty row in file.

    """
    all_val = worksheet.get_all_values()
    row_num = 1
    consecutive = 0
    for row in all_val:
        flag = False
        for col in row:
            if col != "":
                flag = True
                break
        if flag:
            consecutive = 0
        else:
            consecutive += 1
        if consecutive == 2:
            return row_num - 1
        row_num += 1
    return row_num

SERVER_ID = config['server']['id']
SHELL_COMMAND = os.popen(f'speedtest-cli --json --server {SERVER_ID}').read()
SHELL_RESPONSE = json.loads(SHELL_COMMAND)

ROW = first_empty_row(WORKSHEET)

KEYS = [SHELL_RESPONSE['download'], SHELL_RESPONSE['upload'], SHELL_RESPONSE['ping'],
        SHELL_RESPONSE['server']['id'], SHELL_RESPONSE['server']['sponsor'],
        SHELL_RESPONSE['server']['host'], SHELL_RESPONSE['timestamp']]

for COL in range(0, len(KEYS)):
    WORKSHEET.update_cell(ROW, COL + 1, KEYS[COL])
