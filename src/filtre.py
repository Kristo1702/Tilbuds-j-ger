from colorama import init, Fore, Style
import help_functions as ft
import time
import os
init()

VERSION = "1.0.0"


def print_filters_menu():
    print(Fore.LIGHTBLACK_EX + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(Fore.CYAN + "(1) Varer og priser")
    print("(2) Butikker")
    print(Fore.RED + "\n(0) Tilbage")
    print(Fore.LIGHTBLACK_EX + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━" + Style.RESET_ALL)


def input_filters_menu():
    return input("\n\nVælg: ").strip().lower()


def filters_menu():
    valid_menu_inputs = ["1", "2", "0"]
    while True:
        ft.header("Main menu > Filters")
        print_filters_menu()
        choose = input_filters_menu()
        if ft.input_validation(choose, valid_menu_inputs, "Main menu > Filters"):
            return choose

def gem_varer(data=None, default=False) -> dict:
    default = {
        "hakket oksekød": {
            "enhed": "kr/kg",
            "max_pris": 90
        },
        "Smør": {
            "enhed": "kr/pakke",
            "max_pris": 10
        },
        "mælk": {
            "enhed": "kr/L",
            "max_pris": 10
        }
    }    

    if default:
        ft.gem_data(default, "data/varer.json")
    
    else:
        ft.gem_data(data, "data/varer.json")

def indlæs_varer():
    varer, is_valid = ft.indlæs_data("data/varer.json")
    if not is_valid:
        print("\nIngen data fundet (data/varer.json)\n")
    return varer

def vis_varer_menu(varer):
    print(Fore.LIGHTBLACK_EX + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━" + Fore.CYAN)
    for i, (vare, info) in enumerate(varer.items(), start=1):
        max_pris = info["max_pris"]
        enhed = info["enhed"]
        print(f"({i}) {vare} | {max_pris} {enhed}")
    print(Fore.GREEN + "\n(+) Tilføj vare")
    print(Fore.YELLOW + "(-) Fjern vare")
    print(Fore.RED + "\n(0) Tilbage")
    print(Fore.LIGHTBLACK_EX + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━" + Style.RESET_ALL)

def input_varer_menu(varer):
    while True:
        ft.header("Main menu > Filters > Varer og priser")
        vis_varer_menu(varer)

        valid_inputs = ["+", "-", "0"]
        for i in range(len(varer)):
            valid_inputs.append(str(i+1))
        
        choose = input("\n\nVælg: ")
        if not ft.input_validation(choose, valid_inputs, "Main menu > Filters > Varer og priser"):
            continue

        if choose == "0":
            break
        

        
def filters():
    while True:
        ft.clear_terminal()
        choose = filters_menu()
        
        if choose == "0": break

        if choose == "1":
            varer = indlæs_varer()
            input_varer_menu(varer)
