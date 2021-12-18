# api_final_yatube
Стек: Python 3, Django, Django REST Framework, SQLite3, Simple-JWT, GIT.

* Реализована аутентификация по JWT-токену. 
* Имеется документация на redoc и swagger.

* В отличие от встроенной схемы проверки подлинности токенов, для аутентификации JWT не требуется использовать базу данных для проверки токена. 
* Пакет для аутентификации JWT-это djangorestframework-simplejwt, который предоставляет некоторые функции, а также подключаемое приложение для черного списка токенов.
* Проект решает задачу повышения социального взаимодействия.
С помощью публикаций своих историй, пользователи могут размещать информацию в тематических группах, а так же подписываться на заинтересовавших их пользователей с целью оперативного получения информации о новых постах.

#### Использование проекта возможно только через API

#### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/RomanGrbr/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

#### Ознакомиться с полным функционалом и примерами можно по адресу http://127.0.0.1:8000/redoc Доступному после запуска проекта
#### Некоторые из примеров:
Получить список всех публикаций.
```
GET запрос: http://127.0.0.1:8000/api/v1/posts/
Ответ:
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": null,
      "author": null,
      "text": null,
      "pub_date": "2019-08-24T14:15:22Z",
      "image": "string",
      "group": null
    }
  ]
}
```
Создание публикации.
```
POST запрос: http://127.0.0.1:8000/api/v1/posts/
{
  "text": null,
  "image": "string",
  "group": null
}
Ответ:
{
  "id": null,
  "author": null,
  "text": null,
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": null
}
```