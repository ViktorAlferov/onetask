
# Рекомендации по развёртыванию тестового задания «Работа с основными компонентами Django» 

  Суть задания: https://drive.google.com/file/d/0B79gP4rmu79peE5DZm5PeHg2Z1U/view?usp=sharing
  
  1. Склонируйте этот реппозиторий, или загрузите архив. 
  Подробнее:
  https://git-scm.com/book/ru/v2/%D0%9E%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-Git-%D0%A1%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-Git-%D1%80%D0%B5%D0%BF%D0%BE%D0%B7%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D1%8F#_git_cloning
  2. Создайте виртуальное окружение без использования системных пакетов. Используйте python3.5, Django==1.9
  Подробнее:
  http://proft.me/2010/04/3/python-i-okruzhenie-virtualenv/
  3. Активируйте окружение.
  4. Выполните python manage.py makemigrations чтобы создать миграцию для ваших изменений
  5. Выполните python manage.py migrate чтобы применить изменения к базе данных.
  6. Создайте суперпользователя: python manage.py createsuperuser
  7. Запустите сервер. Подробнее:
  http://djbook.ru/rel1.9/intro/tutorial01.html#the-development-server
  
 Вы можете добавить заказчиков, поставщиков и регионы, открыв “/admin/” локального домена в браузере – например, http://127.0.0.1:8000/admin/.
