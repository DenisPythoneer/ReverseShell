# 🐍 Reverse Shell Tool

![Скриншот интерфейса server.py](https://raw.githubusercontent.com/DenisPythoneer/ReverseShell/main/image/screenshotOne.png)

### Простой Reverse Shell на Python, состоящий из трех компонентов❗

    Сервер (server.py) - принимает подключения и отправляет команды

    Клиент (client.py) - подключается к серверу и выполняет команды

    Билдер (builder.py) - компилирует клиент в EXE файл

### 🎯 Особенности

    Кроссплатформенная работа (Windows/Linux)

    Подсветка вывода с помощью pystyle

    ASCII баннеры через pyfiglet

    Возможность компиляции клиента в EXE через PyInstaller

    Простое управление через консольный интерфейс

### Компоненты ⚙️

server.py

    Принимает входящие подключения от клиентов

    Позволяет выполнять команды на удаленной машине

    Отображает результаты выполнения команд

    Поддержка команды exit для завершения сессии

client.py

    Подключается к указанному серверу

    Выполняет получаемые команды через subprocess

    Отправляет результаты обратно на сервер

    Автоматически очищает экран при подключении

builder.py

    Компилирует client.py в standalone EXE файл

    Автоматически перемещает готовый EXE на рабочий стол

    Проверяет наличие зависимостей (PyInstaller)

![Скриншот интерфейса builder.py](https://raw.githubusercontent.com/DenisPythoneer/ReverseShell/main/image/screenshotTwo.png)

#

### 📦 Установка

Клонировать репозиторий

    bash

    git clone https://github.com/DenisPythoneer/ReverseShell.git
    
    cd reverse-shell

Установить зависимости:

    bash

    pip install -r requirements.txt

### 🍳 Использование

Запустить сервер:

    bash

    python server.py

Запустить клиент на целевой машине:

    bash

    python client.py

    Или использовать скомпилированный EXE (через builder.py)

    Вводить команды на сервере для выполнения на клиенте

### ❗ Предупреждение

    Этот инструмент предназначен только для образовательных целей и легального тестирования на системах, где у вас есть разрешение. Не используйте для незаконной деятельности.

#

### 🔗 Ссылка на автора: https://t.me/denispythoneer
