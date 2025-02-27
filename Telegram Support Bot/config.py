"""
Для начала работы с ботом вам необходимо настроить конфигурационный файл бота - config.py
Обязательными переменными является TOKEN, ADMIN_ID и MySQL.
PROXY_URL вы можете оставить пустым.

Описывать установку и настройку я буду для Linux, Ubuntu-based дистрибутивов. Если у вас установлен Windows, либо же другой дистрибутив, то различия с гайдом ниже вы найдете только в пунктах с установкой и настройкой MySQL. Поэтому, при возникновении проблем попробуйте найти гайд по установке MySQL конкретно под вашу ОС.

1. Сначала, проверьте установлен ли MySQL на вашем ПК.
Откройте терминал и пропишите команду: mysql --version
Если вы увидите сообщение похожее на: mysql Ver xx.xx ****, то можете смело переходить на пункт номер 2.

1.2. Если же MySQL не установлен, то введите несколько команд в терминал: 
sudo apt update 
sudo apt install mysql-server

Возвращаемся в пункт 1 и проверяем правильно ли мы все установили. 
Если видите сообщение с версией установленного MySQL, то переходим дальше. 
Если нет - возвращаемся и проверяем, что вы сделали не так. 

2. С установкой MySQL закончили, переходим к созданию пользователя и БД
Введите в терминал команду mysql

2.2. После этого создайте пользователя командой:
CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';

Где user - имя пользователя
А password - пароль

2.3. Предоставьте права пользователю:
GRANT ALL PRIVILEGES ON * . * TO 'user'@'localhost';
FLUSH PRIVILEGES;

Где user - имя пользователя, которое вы ввели в шаге выше

2.4. Создайте БД:
CREATE DATABASE support_db;

Где support_db - имя базы данных

2.5. Замените все значения в переменной MySQL
localhost - оставить без изменения
user - имя пользователя, которого вы создали
password - пароль для пользователя
support_db - имя базы данных

3. Создайте вашего бота и получите токен для него
Перейдите по ссылке t.me/BotFather, либо найдите его сами в поиске по юзернейму @BotFather и введите команду /newbot
Следуйте дальнейшим указаниям бота и укажите полученный токен в переменной TOKEN

4. Найдите бота, который отправит вам ваш Telegram ID
Одними из таких ботов могут быть @userinfobot или @username_to_id_bot
Введите полученный ID в переменную ADMIN_ID

На этом, настройка конфига завершена. Можете просто сохранить и закрыть этот файл.
"""

MySQL = ['localhost', 'user', 'password', 'support_db'] 
TOKEN = 'ВАШ_ТОКЕН'
ADMIN_ID = 'ADMIN_ID'
PROXY_URL = ''