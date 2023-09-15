# API YaTube

### Описание

#### REST API для проекта Yatube

Расширены возможности API проекта Yatube:
- возможность подписываться на авторов;
- аутентификация пользователей по JWT-токену;
- права доступа пользователей к контенту на сайте.

### Технологии
- Python 3.9.10
- Django 2.2.19

### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
```
cd yatube_api
```
```
python3 -m venv env
```
```
source env/bin/activate
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- Выполнить миграции:
``` 
python3 manage.py migrate
``` 
- Запустить проект:
``` 
python3 manage.py runserver
``` 
- В папке с файлом manage.py выполните команду:
```
py manage.py runserver
```

### Автор
nmashkov
