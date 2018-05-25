# Periodic tasks using Celery Beat

## Set up env

```sh
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt

# start celery daemon 
celery worker -l info -A app --beat
```

## or Docker (Recommended for production) 
```sh
docker build -t celery-periodic-task .
docker run -d --name redis-celery -it -p 6379:6379 redis 
docker run -d --link redis-celery:redis --name celery-periodic-task-1 celery-periodic-task:latest
```


Happy coding
