import os
import time
import sys
from colorama import init, Fore, Style
import json

init()

VERSION = "1.0.0"

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

def input_validation(selected: str, valids: list, path: str = None) -> bool:
    if selected not in valids:
        header(path)
        print(Fore.RED + "Ugyldigt valg!\n" + Style.RESET_ALL + "Vælg mellem", end="")
        for i in range(len(valids)-2):
            print(f" {valids[i]},", end="")
        print(f" {valids[-2]} eller {valids[-1]}\n")

        input(Fore.LIGHTBLACK_EX + "\n\n\nTryk enter for at fortsætte..." + Style.RESET_ALL)
        return False
    return True

def header(path: str = None, padding: int = 2):
    clear_terminal()
    if VERSION is not None:
        print(Fore.MAGENTA + " _____ _ _ _                _           _                          " + "    " + Fore.LIGHTBLACK_EX + f"v.{VERSION}")
    else:
        print(Fore.MAGENTA + " _____ _ _ _                _           _                          ")
    print(Fore.MAGENTA + "|_   _(_) | |__  _    _  __| |___      | | __ ____  __ _  ___ _ __ ")
    print("  | | | | | '_ \| | | |/ _` / __|   _  | |/ _`  _ \/ _` |/ _ \ '__|")
    print("  | | | | | |_) | |_| | (_| \__ \  | |_| | (_|  __/ (_| |  __/ |   ")
    print("  |_| |_|_|_.__/ \__,_|\__,_|___/   \___/ \__,____|\__, |\___|_|   ")
    print("                                                   |___/           " + Style.RESET_ALL)
    if path is not None:
        path_length = len(path)
        total_length = 67
        white_space = total_length - path_length - 4
        if white_space < 0:
            path = f"...{path[-60:]}"
            white_space = 0
        
        print(Fore.LIGHTBLACK_EX + "╭" + "─"*(total_length-2) + "╮")
        print(f"│ " + Fore.MAGENTA + f"{path}" + Fore.LIGHTBLACK_EX + " "*white_space + " │")
        print("╰" + "─"*(total_length-2) + "╯" + Style.RESET_ALL)
        if padding:
            print("\n"*padding)


def gem_data(data, path):
    try:
        with open(path, "w") as file:
            json.dump(data, file, indent=4)
        return True
    except:
        return False

def indlæs_data(path):
    try:
        if os.path.exists(path):
            with open(path, "r") as file:
                data = json.load(file)
                return data, True
        return {}, False
    except:
        return {}, False

def start_program():
    if not os.path.exists("data"):
        os.makedirs("data", exist_ok=True)