from colorama import init, Fore, Style
import help_functions as ft
import time
init()


def print_menu():
    print(Fore.LIGHTBLACK_EX + "----------------------")
    print(Fore.GREEN + "(1) Scan tilbud")
    print(Fore.CYAN + "\n(2) Ønskede priser")
    print(Fore.RED + "\n(0) Luk programmet")
    print(Fore.LIGHTBLACK_EX + "----------------------" + Style.RESET_ALL)


def navigate_menu():
    return input("\n\nVælg: ").strip().lower()


def input_validation(selected: str, valids: list) -> bool:
    if selected not in valids:
        ft.clear_terminal()
        print(Fore.RED + "Ugyldigt valg!\n" + Style.RESET_ALL + "Vælg mellem", end="")
        for i in range(len(valids)-2):
            print(f" {valids[i]},", end="")
        print(f" {valids[-2]} eller {valids[-1]}\n")
        
        return False
    return True


def main_menu():
    while True:
        valid_menu_inputs = ["1", "2", "0"]
        print_menu()
        choose = navigate_menu()
        if input_validation(choose, valid_menu_inputs):
            return choose
        
        time.sleep(2)
        ft.clear_terminal()