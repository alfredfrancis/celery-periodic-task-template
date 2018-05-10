# Periodic tasks using Celery Beat

## Set up env
```sh
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt

```
## start celery daemon 

```sh
celery worker -l info -A app --beat
```

Happy coding
