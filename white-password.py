"""
White-Password
Secure-Password-Input
Licensed under CC0-1.0 License to Pavana Narayana Bhat
------------------------------------------------------------------------------------------------------------------------
Code by: Pavana Narayana Bhat AKA PiXinCreate
------------------------------------------------------------------------------------------------------------------------
Description:
    You don't want / wish your password to
be known to anyone in this world except you.
If YES, you're at the right place! Grab the
code, re-use it in your python Code.

NOTE: Usage in README.md
"""
from msvcrt import getch


def white_password(prompt):       # A simple approach to Secure password input.!
    print(prompt, end='', flush=True)
    buf = b''
    while True:
        ch = getch()
        if ch in {b'\n', b'\r', b'\r\n'}:  # End Of Line or Carriage Return
            print('')
            break
        elif ch == b'\x08':  # Backspace
            buf = buf[:-1]
            print(f'\r{(len(prompt) + len(buf) + 1) * ""}\r{prompt}{"" * len(buf)}', end='', flush=True)
        elif ch == b'\x03':  # Copy or Ctrl + C
            raise KeyboardInterrupt
        else:
            buf += ch
            print('', end='', flush=True)       # Prints nothing instead of Password on the screen
    return buf.decode(encoding='utf-8')
