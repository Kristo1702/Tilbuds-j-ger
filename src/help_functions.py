import os
import time
import sys



def clear_terminal():
    if os.name == 'nt':  # Windows
        os.system('cls')
    elif os.name == 'posix':  # Linux og macOS
        os.system('clear')
    else:  # Fallback
        print("\033c", end="")

def spinner(duration=6):
    symbols = ["●      ", "●●     ", "●●●    ", "●●●●   ", "●●●●●  ", " ●●●●● ", "  ●●●● ", "   ●●● ", "    ●● ", "     ● ", "       "]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write("\r" + symbols[i % len(symbols)])
        sys.stdout.flush()
        time.sleep(0.075)
        i += 1