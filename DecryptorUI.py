'''

Filename: DecryptorUI.py

The User Interface for The Decryptor

'''

import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
    [sg.Text('THE DECRYPTOR')],
    [sg.Text('Enter text to decrypt: '), sg.InputText()],
    [sg.Button('Decrypt'), sg.Button('Quit')]
]