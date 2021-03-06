# Use cases модель

Use-cases, выявленные в процессе моделирования представлены на диаграмме. В данной системе есть только одна роль – Пользователь системы,
которая имеет полный доступ ко всей функциональности разработанной системы.

![Diagram1](../assets/use_case_dio.png)

# Функциональные требования 

Мы можем сформулировать набор функциональных требований:

- FRQ1 Telegram-Bot должен предоставить возможность загрузить фото подписи
- FRQ2 Telegram-Bot должен предоставить возможность редактировать существующую запись пользователя
- FRQ3 Telegram-Bot должен предоставить возможность узнать человека, которому принадлежит подпись
- FRQ4 Telegram-Bot должен предоставить возможность проверить, является ли подпись подделкой

# Примеры Use Case: 

## `Использование Telegram-Bot для загрузки фотографии подписи`

![Diagram2](../assets/user_dia.png)

| Система | Telegram-Bot |
| :-- |--: |
| Основное действующее лицо | Пользователь приложения Telegram |
| Цель | Загрузить своё фото |
| Триггер | Пользователь решает воспользоваться Telegram-Bot и заходит в приложение |
| Результат | Информация о пользователе сохранена |

### Основной поток событий

`Использование Telegram-Bot для загрузки фотографии подписи`

| № шага | Действующее лицо | Шаг | Комментарий |
| :-- | --- | --- | --: |
| 1 | Пользователь | Вводит команду `/start` | |
| 2 | Пользователь | Вводит команду `/my_sign` | |
| 3 | Система | Проверяет, есть ли данный `User Id` в базе данных | Пользователь воспользовался Telegram-Bot первый раз, поэтому запись о нём отсутствует |
| 4 | Система | Просит загрузить фото подписи | Фото должно быть хорошего качества, подпись должна быть сделана на белой не мятой бумаге |
| 5 | Пользователь | Загружает фотографию подписи | |
| 6 | Система | Сохраняет данные о пользователе | |
| 7 | Система | Оповещает пользователя, что информация о нём была записана | |
| 8 | Пользователь | Выходит из приложения | |

## `Использование Telegram-Bot для редактирования существующей записи`

![Diagram2](../assets/user_dia.png)

| Система | Telegram-Bot |
| :-- |--: |
| Основное действующее лицо | Пользователь приложения Telegram |
| Цель | Отредактировать запись о себе |
| Триггер | Пользователь решает воспользоваться Telegram-Bot и заходит в приложение |
| Результат | Информация о пользователе изменена |

### Основной поток событий

`Использование Telegram-Bot для редактирования существующей записи`

| № шага | Действующее лицо | Шаг | Комментарий |
| :-- | --- | --- | --: |
| 1 | Пользователь | Вводит команду `/start` | |
| 2 | Пользователь | Вводит команду `/my_sign` | |
| 3 | Система | Проверяет, есть ли данный `User Id` в базе данных | Пользователь воспользовался Telegram-Bot не первый, поэтому запись о нём присутствует |
| 4 | Система | Спрашивает пользователя о том, желает ли он изменить запись о себе ||
| 5 | Пользователь | Вводит команду `yes` | |
| 6 | Система | Просит загрузить фото подписи | Фото должно быть хорошего качества, подпись должна быть сделана на белой не мятой бумаге |
| 7 | Пользователь | Загружает фотографию подписи | |
| 8 | Система | Сохраняет данные о пользователе | |
| 9 | Система | Оповещает пользователя, что информация о нём была записана | |
| 10 | Пользователь | Выходит из приложения | |

## `Использование Telegram-Bot для проверки пользователя, которому принадлежит подпись`

![Diagram2](../assets/user_dia.png)

| Система | Telegram-Bot |
| :-- |--: |
| Основное действующее лицо | Пользователь приложения Telegram |
| Цель | Узнать, кто владелец подписи |
| Триггер | Пользователь решает воспользоваться Telegram-Bot и заходит в приложение |
| Результат | Пользователь получил информацию о подписи |

### Основной поток событий

`Использование Telegram-Bot для проверки пользователя, которому принадлежит подпись`

| № шага | Действующее лицо | Шаг | Комментарий |
| :-- | --- | --- | --: |
| 1 | Пользователь | Вводит команду `/start` | |
| 2 | Пользователь | Вводит команду `/my_sign` | |
| 3 | Система | Проверяет, есть ли данный `User Id` в базе данных | Пользователь воспользовался Telegram-Bot не первый, поэтому запись о нём присутствует |
| 4 | Система | Спрашивает пользователя о том, желает ли он изменить запись о себе ||
| 5 | Пользователь | Вводит команду `no` | |
| 6 | Система | Просит загрузить фото подписи и получить о нём информацию | Фото должно быть хорошего качества, подпись должна быть сделана на белой не мятой бумаге |
| 7 | Пользователь | Загружает фотографию подписи | |
| 8 | Система | Выводит на экране `User Id`, соответствуюший данной подписи | |
| 9 | Система | Спрашивает, хочет ли пользователь проверить данную подпись на подлинность | |
| 10 | Пользователь | Вводит команду `no` | |
| 11 | Пользователь | Выходит из приложения | |

## `Использование Telegram-Bot для проверки подлинности подписи`

![Diagram2](../assets/user_dia.png)

| Система | Telegram-Bot |
| :-- |--: |
| Основное действующее лицо | Пользователь приложения Telegram |
| Цель | Проверить подпись на подлинность |
| Триггер | Пользователь решает воспользоваться Telegram-Bot и заходит в приложение |
| Результат | Пользователь получил информацию о подписи |

### Основной поток событий

`Использование Telegram-Bot для проверки подлинности подписи`

| № шага | Действующее лицо | Шаг | Комментарий |
| :-- | --- | --- | --: |
| 1 | Пользователь | Вводит команду `/start` | |
| 2 | Пользователь | Вводит команду `/my_sign` | |
| 3 | Система | Проверяет, есть ли данный `User Id` в базе данных | Пользователь воспользовался Telegram-Bot не первый, поэтому запись о нём присутствует |
| 4 | Система | Спрашивает пользователя о том, желает ли он изменить запись о себе ||
| 5 | Пользователь | Вводит команду `no` | |
| 6 | Система | Просит загрузить фото подписи и получить о нём информацию | Фото должно быть хорошего качества, подпись должна быть сделана на белой не мятой бумаге |
| 7 | Пользователь | Загружает фотографию подписи | |
| 8 | Система | Выводит на экране `User Id`, соответствуюший данной подписи | |
| 9 | Система | Спрашивает, хочет ли пользователь проверить данную подпись на подлинность | |
| 10 | Пользователь | Вводит команду `yes` | |
| 15 | Система | Выводит сообщение о том, является подпись подлинной или нет | |
| 11 | Пользователь | Выходит из приложения | |

## `Использование Telegram-Bot для проверки подписи в первый раз`

![Diagram2](../assets/user_dia.png)

| Система | Telegram-Bot |
| :-- |--: |
| Основное действующее лицо | Пользователь приложения Telegram |
| Цель | Узнать, кому принадлежит подпись, и проверить ее на подлинность|
| Триггер | Пользователь решает воспользоваться Telegram-Bot и заходит в приложение|
| Результат | Информация о пользователе сохранена, пользователь получит информацию о фото, которое он загрузил |

### Основной поток событий

`Использование Telegram-Bot для проверки подписи в первый раз`

| № шага | Действующее лицо | Шаг | Комментарий |
| :-- | --- | --- | --: |
| 1 | Пользователь | Вводит команду `/start` | |
| 2 | Пользователь | Вводит команду `/my_sign` | |
| 3 | Система | Проверяет, есть ли данный `User Id` в базе данных | Пользователь воспользовался Telegram-Bot первый раз, поэтому запись о нём отсутствует |
| 4 | Система | Просит загрузить фото подписи | Фото должно быть хорошего качества, подпись должна быть сделана на белой не мятой бумаге |
| 5 | Пользователь | По ошибке загружает документ, а не фотографию | |
| 6 | Система | Оповещает пользователя, что данный формат не подходит, и просит пользователя загрузить фото | |
| 7 | Пользователь | Загружает фотографию подписи | |
| 8 | Система | Сохраняет данные о пользователе | |
| 9 | Система | Оповещает пользователя, что информация о нём была записана | |
| 10 | Система | Предлагает пользователю загрузить новое фото и получить о нём информацию | |
| 11 | Пользователь | Загружает новое фото своей подписи | |
| 12 | Система | Выводит на экране `User Id`, соответствуюший данной подписи | В данном случае, `User Id` пользователя |
| 13 | Система | Спрашивает, хочет ли пользователь проверить данную подпись на подлинность | |
| 14 | Пользователь | Вводит команду `yes` | |
| 15 | Система | Выводит сообщение о том, что подпись является подлинной | |
| 16 | Пользователь | Выходит из приложения | |
