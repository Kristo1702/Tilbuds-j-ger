import main_menu as menu
import help_functions as ft
import filtre as ftr
import os

VERSION = "1.0.0"

def main():
    ft.spinner(0.5)

    while True:
        choose = menu.main_menu()

        if choose == "1": pass #RUN
        if choose == "2": ftr.filters()
        if choose == "0": break #EXIT



if __name__ == "__main__":
    try:
        ft.start_program()
        if not os.path.exists("data/varer.json"):
            ftr.gem_varer(default=True)
    except Exception as e:
        print(f"\n\nUKENDT FEJL I STARTUP:\n{e}\n")

    try:
        main()
    except Exception as e:
        print(f"\n\nUKENDT FEJL I KODE:\n{e}\n\n")