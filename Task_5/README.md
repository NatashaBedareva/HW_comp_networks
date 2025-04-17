
# Задача 5 Контейнеры и БД

Два докер контейнера. В первом запускается приложение, которое считает количество открытий страницы и выводит результат на веб страницу. 
Во втором лежит база данных, в которую записывается число.

## Создание сети

```
docker network create app-network
```

## Работа с базой данных

Нужно создать файл `.env` со следующими ключами

```
DB_USER = 'myuser'
DB_PASSWORD = 'mypassword'
DB_NAME = 'mydatabase'
DB_HOST = 'postgres-db'
```

Запуск контейнера 

```commandline
docker run -d \
  --name postgres-db \
  --network app-network \
  -e POSTGRES_USER=myuser \
  -e POSTGRES_PASSWORD=mypassword \
  -e POSTGRES_DB=mydatabase \
  -p 5432:5432 \
  postgres:13
```

## Сборка и запуск приложения

```commandline
docker build -t number-app .

docker run -d \
  --name number-app \
  --network app-network \
  -e DB_USER=myuser \
  -e DB_PASSWORD=mypassword \
  -e DB_NAME=mydatabase \
  -e DB_HOST=postgres-db \
  -p 5000:5000 \
  number-app
```

## Запуск

[http://localhost:5000](http://localhost:5000)




