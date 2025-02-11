# Django

## How to run

### Locally

Install dependencies
```bash
pip install -r requirements.txt
```

Run using runserver
```bash
./manage.py runserver
```

Run using gunicorn
```bash
gunicorn myproject.wsgi:application
```

### Using Docker image

Build
```bash
docker build -t django_project .
```

Run
```bash
docker run -d -p 8000:8000 django_project
```