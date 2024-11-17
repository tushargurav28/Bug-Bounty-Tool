try:
    import os
    from git import Repo
    from flask import session
    import sys
    import subprocess
    from colorama import Fore, Style, init
    from time import sleep
    from rich import print as rich_print
    from rich.panel import Panel
    from rich.table import Table
    import urllib3
    from rich.panel import Panel
    from modules import open_redirection, lfi, sqli, xss, report
    from banner import color
    print("hello world")

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')


    def display_menu():
        print("hello")

    def print_exit_menu():
        clear_screen()

        panel = Panel(r"""

            """,
                      style="bold green",
                      border_style="blue",
                      expand=False
                      )

        rich_print(panel)
        print(color.RED + "\n\nSession Off..\n")
        sys.exit(0)

    # def handle_selection()
    def handle_selection(selection):
        try:
            if selection == '1':
                clear_screen()
                os.system("python3 tool/lfi.py")

            elif selection == '2':
                clear_screen()
                os.system("python3 tool/or.py")

            elif selection == '3':
                clear_screen()

                os.system("python3 tool/sqli.py")

            elif selection == '4':
                clear_screen()
                os.system("python3 tool/xss.py")

            elif selection == '5':
                clear_screen()
                os.system("python3 tool/crlf.py")

            elif selection == '6':
                clear_screen()
                run_update()
                clear_screen()

            elif selection == '7':
                clear_screen()
                sys.exit(0)

        except KeyboardInterrupt:
            sys.exit(0)


    def main():
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        clear_screen()
        while True:
            try:
                display_menu()
                choice = input(f"\n{Fore.CYAN}[?] Select an option (0-7): {Style.RESET_ALL}").strip()
                handle_selection(choice)

            except KeyboardInterrupt:
                print_exit_menu()
                sys.exit(0)


    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            print_exit_menu()
            sys.exit(0)


except KeyboardInterrupt:
    print_exit_menu()

