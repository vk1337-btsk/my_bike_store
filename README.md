## Интернет магазин "ВелоМото" на фреймворке Django

### Описание проекта:

Это мой pet-project, который я создаю, пока изучаю фреймворк Django, а также всё, что касается веб-разработки, а именно:
HTML, CSS, JavaScript.

### Используемые технологии:

- python
- Django
- pillow
- ipython

### Как запустить проект?:

1. Клонируйте проект с GitHub себе на ПК:

```text
git clone https://github.com/vk1337-btsk/my_bike_store
```

2. Создайте и активируйте виртуальное окружение:

- Инструкция для работы через виртуальное окружение - poetry:
  Создает виртуальное окружение -> Активирует виртуальное окружение -> Установить зависимости:

```text
poetry init
poetry shell
poetry install
```

- Инструкция для активации виртуального окружения - pip:
  Создает виртуальное окружение:

```text
python3 -m venv venv
```

Активирует виртуальное окружение:

```text
source env/bin/activate              # для Linux и Mac
source env\Scripts\activate          # для Windows
source env\Scripts\activate.bat      # для Windows
```

Установить зависимости:

```text
pip install -r requirements.txt
```

3. Создайте базу данных postgresql.

4. В корне проекта есть файл "config.ini.sample", внесите в этот файл информацию о созданной вами базе
   (название, пароль и т.д.) и переименуйте в "config.ini". У вас должна получиться примерно следующая запись:

```ini
; Configuration for database my_store
[database_my_store]
dbname = name_db
host = localhost
user = postgres
password = password
port = 5432
```

5. В корне проекта есть файл "env.sample", отредактируйте файл в соответствии с примером ниже

```text
EMAIL_HOST_USER='your_email@yandex.ru' - ваш email для отправки писем
EMAIL_HOST_PASSWORD='your_yandex_smtp_password' - ваш пароль от smtp приложения почтового сервиса
EMAIL_HOST_TO_USER='recipient@example.com' - email получателя для тестов

ADMIN_EMAIL='admin@test.com' - email администратора сайта
ADMIN_PASSWORD='123@secret' - пароль администратора сайта
```

6. Создаем таблицы в БД:

```text
python manage.py migrate
```

7. При необходимости заполните базу данных тестовыми данными следующей командой:

```text
python manage.py fill
```

8. Запустите проект:

```text
python manage.py runserver
```

9. Перейдите по адресу вашего локального компьютера в браузере:

```text
http://127.0.0.1:8000
```