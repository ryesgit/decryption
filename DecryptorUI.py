'''

Filename: DecryptorUI.py

The User Interface for The Decryptor

'''

import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text('THE DECRYPTOR')],
    [sg.Text('Enter text to decrypt: '), sg.InputText(key='input')],
    [sg.Text('Decrypted Text: '), sg.Text(key='output')],
    [sg.Button('Decrypt'), sg.Button('Quit')]
]

window = sg.Window('Decryptor', layout)

while True:
    event, values = window.read()

    if (event == sg.WIN_CLOSED or event == 'Quit'):
        break

window.close()