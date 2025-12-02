import main_menu as menu
import help_functions as ft
import filtre as ftr
import time



def main():
    ft.spinner(0.5)
    ft.clear_terminal()

    while True:
        choose = menu.main_menu()

        if choose == "1": pass #RUN
        if choose == "2": ftr.view_filters()
        if choose == "0": break #EXIT



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n\nUKENDT FEJL I KODE:\n{e}\n\n")