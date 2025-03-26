
# Задача 4 PostgresSQ

Дополнение Задачи 3, добавлена выгрузка данных в таблицу SQL.

## Работа с локальной базой данных

Нужно создать файл `.env` со следующими ключами

```
USER = 'your_username'
PASSWORD = 'your_password'
HOST = '127.0.0.1'
DB_NAME = 'your_database'
TABLE_NAME = 'your_table'
PORT = 5432
```

## Описание out.csv

Выходной файл является таблицей CSV, имеет следующий вид:

| product_name | mount | article | width    |height|depth|
|:-------------| :-------          |:--------|:---------|:-------- |:-------- | 
| `string`     | `int`             | `string`  | `int см` |`int см` | `int см`|

`product_name` - имя продукта

`mount` - цена продукта

`article` - артикаль

`width, height, depth` - ширина, высота, глубина


## Запуск

```
python main.py
```




