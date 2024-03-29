# Кулинарная Книга на Django

Этот проект представляет собой небольшое веб-приложение "Кулинарная Книга", разработанное с использованием фреймворка Django. Приложение позволяет управлять рецептами и продуктами, а также предоставляет функционал для отслеживания использования продуктов в рецептах.

## Особенности

- **Управление Продуктами и Рецептами:** Возможность добавлять, редактировать и удалять продукты и рецепты через админ-панель Django.
- **Добавление Продуктов в Рецепты:** Функция для добавления продукта в рецепт с указанием его веса.
- **Приготовление Рецептов:** Функция для учета приготовления рецепта, автоматически увеличивающая счетчик использования каждого продукта в рецепте.
- **Просмотр Рецептов:** Возможность просмотра рецептов, которые не содержат определенный продукт или содержат его в незначительном количестве.

## Технологии

- Python
- Django
- SQLite
  
## Запуск проекта

Чтобы запустить проект локально, выполните следующие шаги:

1. **Клонирование репозитория:**
   ``
    git clone https://github.com/telotonet/mirgovorit
    cd your_project
  ``
2. **Установка зависимостей:**
   ``
     -pip install django
   ``
3. **Настройка и запуск Django:**
   ``
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser # для создания администратора
    python manage.py runserver
  ``
4. После запуска сервера перейдите по адресу `http://localhost:8000` в вашем браузере.

## Админка

Для доступа к админ-панели:

1. Перейдите по адресу `http://localhost:8000/admin`.
2. Введите учетные данные администратора, созданного на предыдущем шаге.
