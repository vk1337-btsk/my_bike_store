## Интернет магазин "ВелоМото" на фреймворке Django


### Описание проекта:
Это мой pet-project, который я создаю, пока изучаю фреймворк Django, а также всё, что касается веб-разработки, а именно: HTML, CSS, JavaScript.

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
poetry shell
poetry install
poetry init
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

3. В корне проекта создайте файл config.ini в следующем формате и пропишите данные своей базы данных:
```ini
; Configuration for database my_store
[database_my_store]
dbname=name_db
host=localhost
user=postgres
password=password
port=5432
```

4. Запустите проект:
```text
python manage.py runserver
```

5. Перейдите по адресу вашего локального компьютера в браузере:
```text
http://127.0.0.1:8000
```