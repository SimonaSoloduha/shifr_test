## Описание проекта

WEB-сервис на Python с возможностью загрузить картинку и проанализировать пиксели
Сервис умеет:
• сообщать каких пикселей больше на картинке, белых или чёрных
• по HEX коду цвета считать количество пикселей этого цвета на картинке

## Запуск проекта

1. Откройте консоль

2. Перейдите в папку, в которой будет храниться проект

cd <путь до папки>

3. Клонируйте проект
git clone https://github.com/SimonaSoloduha/shifr_test.git

4. Перейдите в папку проекта
cd shifr_test

5. Создайте виртуальное окружение venv
python3 -m venv venv

6. Активируйте виртуальное окружение venv
source venv/bin/activate

7. Установите необходимые пакеты:
pip3 install -r requirements.txt

(Все используемые библиотеки представлены в файле requirements.txt)

При необходимости обновите pip

(Если получите сообщение: WARNING: You are using pip version 20.2.3; however, version 21.2.1 is available. You should consider upgrading via the '..... flask/venv/bin/python3 -m pip install --upgrade pip' command.)


8. Запустите проект
(Убедитесь, что вы находитесь в папке shifr_test, внутри которой есть файл manage.py)
python manage.py runserver

9. Перейдете по ссылке
http://127.0.0.1:8000/
