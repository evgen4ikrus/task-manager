# task-manager
Веб приложение по управлению проектами.

### Установка и запуск:
Клонируйте репозиторий:
```commandline
git clone https://github.com/evgen4ikrus/task-manager.git
```
Перейдите в директорию проекта:
```commandline
cd task-manager/
```
Создайте и активируйте виртуальное окружение:
```commandline
python3 -m venv venv
source venv/bin/activate
```
Установите зависимости:
```commandline
pip install -r requirements.txt
```
Примените миграции БД:
```commandline
python3 manage.py migrate
```
Запустите веб-приложение:
```commandline
python3 manage.py runserver
```
Проверьте работу веб-приложения перейдя по [ссылке](http://127.0.0.1:8000/admin/) в панель администратора.

### Тестовые данные
Для тестирования работы веб-приложения, наполните базу данных тестовыми данными:
```commandline
python3 manage.py loaddata db_test_data.json
```
### Переменные окружения
Всем переменным окружения заданы значения по умолчанию, но вы можете их переопределить. Для этого в корне проекта 
создайте файл `.env` и запишите в него переменные в формате `КЛЮЧ=ЗНАЧЕНИЕ`:
```txt
SECRET_KEY
DEBUG
ALLOWED_HOSTS
DATABASE_URL
```