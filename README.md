# EvaProjectTest

Запуск через docker:
```
docker compose up
```

Или отдельно запустить сервер и демона:
- запустить сервер
```
cd server/cpu_load
python manage.py migrate
python manage.py runserver
```
- запустить демона
```
cd daemon
python cpu_load.py --host http://127.0.0.1 --port 8000 
```

Эндпоинт отображения нагрузки на процессор:
```
http://0.0.0.0:8000/cpu/
```