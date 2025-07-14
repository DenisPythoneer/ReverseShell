import socket
import os
import time

from pystyle import *
from colorama import Fore, init


Success = Colors.green + "[+]" + Colors.reset
Error = Colors.red + "[-]" + Colors.reset
Info = Colors.blue + "[*]" + Colors.reset


init(autoreset=True)


def reverse_shell():
    try:
        print(f"\n{Info} Ожидание подключения клиента к серверу...")

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('127.0.0.1', 8888))
        s.listen(5)

        client, addr = s.accept()
        print(f"\n{Success} Подключение к серверу от {addr[0]}")

        time.sleep(2)
        display_banner()

        while True:
            command = input(f"\n{Info} Введите команду ('exit' - Для выхода): ")
            client.send(command.encode())
            if command.lower() == 'exit':
                print(f"\n{Error} Соединение разорвано!")
                break
            result_output = client.recv(4096).decode()
            print(f"\n{Success} Результат: \n{result_output}")

        client.close()
        s.close()
    except Exception as e:
        print(f"{Error} Произошла ошибка при подключении: {e}")


def display_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.CYAN + """
    ███████████                                                             █████████  █████               ████  ████ 
    ░░███░░░░░███                                                           ███░░░░░███░░███               ░░███ ░░███ 
    ░███    ░███   ██████  █████ █████  ██████  ████████   █████   ██████ ░███    ░░░  ░███████    ██████  ░███  ░███ 
    ░██████████   ███░░███░░███ ░░███  ███░░███░░███░░███ ███░░   ███░░███░░█████████  ░███░░███  ███░░███ ░███  ░███ 
    ░███░░░░░███ ░███████  ░███  ░███ ░███████  ░███ ░░░ ░░█████ ░███████  ░░░░░░░░███ ░███ ░███ ░███████  ░███  ░███ 
    ░███    ░███ ░███░░░   ░░███ ███  ░███░░░   ░███      ░░░░███░███░░░   ███    ░███ ░███ ░███ ░███░░░   ░███  ░███ 
    █████   █████░░██████   ░░█████   ░░██████  █████     ██████ ░░██████ ░░█████████  ████ █████░░██████  █████ █████
    ░░░░░   ░░░░░  ░░░░░░     ░░░░░     ░░░░░░  ░░░░░     ░░░░░░   ░░░░░░   ░░░░░░░░░  ░░░░ ░░░░░  ░░░░░░  ░░░░░ ░░░░░ 
                                                                                                                   
                                        [https://github.com/DenisPythoneer]                                                                                     
    """)


def main():
    display_banner()
    reverse_shell()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Colors.green + "\nДо свидания!" + Colors.reset)