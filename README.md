# Тестовой задание по направлению Python для HQ
## Запуск проекта
Клонируйте репозиторий с проектом на свой компьютер. В терминале из рабочей директории выполните команду:
```
git@github.com:BaldiskA/Python_Test_Task_HQ.git
```
Установить и активировать виртуальное окружение
```
source /venv/bin/activate
```

Установить зависимости из файла requirements.txt
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

### Выполните миграции
```
python manage.py migrate
```
В папке с файлом manage.py выполнить команду:
```
python manage.py runserver
```
Создание нового супер пользователя
```
python manage.py createsuperuser
```
# Пример запроса к API:
Список пользователей:

GET-запрос
```
http://localhost/api/users/
```
```
"results": [
{
"email": "user@example.com",
"id": 0,
"username": "string",
"first_name": "Вася",
"last_name": "Пупкин",
}
```
Регистрация пользователя:

POST-запрос
```
http://localhost/api/users/
```
```
{
"email": "vpupkin@yandex.ru",
"username": "vasya.pupkin",
"first_name": "Вася",
"last_name": "Пупкин",
"password": "Qwerty123"
}
```
Профиль пользователя:

GET-запрос
```
http://localhost/api/users/{id}/
```
```
{
"email": "user@example.com",
"id": 0,
"username": "string",
"first_name": "Вася",
"last_name": "Пупкин",
}
```
Текущий пользователь:

GET-запрос
```
http://localhost/api/users/me/
```
Изменение пароля:

POST-запрос
```
http://localhost/api/users/set_password/
```
```
{
"new_password": "string",
"current_password": "string"
}
```
Получить токен авторизации:

POST-запрос
```
http://localhost/api/auth/token/login/
```
```
{
"password": "string",
"username": "string"
}
```
Удаление токена:

POST-запрос
```
http://localhost/api/auth/token/logout/
```
## Просмотр выполнения тестового задания

### Посмотреть выполнение первого задания по запросам API:
```
http://localhost/api/lesson-access/
```
### Посмотреть выполнение второго задания по запросам API:
```
http://localhost/api/product-lesson-access/<int:product_id>/
```
### Посмотреть выполнение третьего задания по запросам API:
```
http://localhost/api/product-stats/
```
