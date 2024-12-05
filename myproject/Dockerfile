FROM python:3.11

WORKDIR /test2

COPY . .

RUN pip install django

RUN python manage.py makemigrations

RUN python manage.py migrate

EXPOSE 9999

CMD [ "python", "manage.py", "runserver", "0.0.0.0:9999"]
