
# Задача 1 ping 

В данной задаче нужно занести RTT для сайтов в таблицу CSV.

## Описание input.txt

На вход программа получает путь к txt файлам для чтения и записи.

Входной файл должен:

- содержат названия сайтов через перенос строки

- без пропуска строк

Пример входного файла:

```
unity.com
www.python.org
ru.wikipedia.org
askubuntu.com
www.youtube.com
habr.com
```

## Описание out.csv

Выходной файл является таблицей CSV, имеет следующий вид:

| host_name | average_speed     |
| :-------- | :-------          |
| `host`    | `int`             |

`host_name` - имя сайта из input.txt

`average_speed` - RTT

## Запуск

```
python main.py <input.txt> <out.csv>
```




