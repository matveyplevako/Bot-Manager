FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN python manage.py collectstatic --noinput
ENTRYPOINT gunicorn --bind 0.0.0.0:8000 Bot_manager.wsgi -w 2 --log-level debug --timeout 60
