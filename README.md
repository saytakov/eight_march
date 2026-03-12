Сайт 8 марта

Сайт предназначен для поздравления с праздником 8 марта.

Для использования необходимо скачать необходимые библиотеки из requirements.txt

pip install -r requirements.txt

Применить миграции

/eight_march python manage.py migrate

Запустить сервер

/eight_march python manage.py runserver


Сайт реализован на Django
БД SQLite
Запросы реализуются через Django ORM
Была расширена модель User для удобного добавления полей в будущем
Написаны тесты на unittest
Также подключен Django Debug Toolbar для отладки
