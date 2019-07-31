FROM python:3.6

RUN mkdir /app

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

RUN python manage.py collectstatic --no-input

EXPOSE 80

CMD ["gunicorn", "--bind", ":80", "cookbook.wsgi:application"]
