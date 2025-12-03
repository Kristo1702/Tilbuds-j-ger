from colorama import init, Fore, Style
import help_functions as ft
import time
init()

VERSION = "1.0.0"

def print_menu():
    print(Fore.LIGHTBLACK_EX + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(Fore.CYAN + "(1) Scan tilbud")
    print("(2) Filtre")
    print(Fore.RED + "\n(0) Luk programmet")
    print(Fore.LIGHTBLACK_EX + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━" + Style.RESET_ALL)


def input_menu():
    return input("\n\nVælg: ").strip().lower()


def main_menu():
    while True:
        ft.header("Main menu")
        valid_menu_inputs = ["1", "2", "0"]
        print_menu()
        choose = input_menu()
        if ft.input_validation(choose, valid_menu_inputs, "Main menu"):
            return choose