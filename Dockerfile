FROM python:3.13-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app/

CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
