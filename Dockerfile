FROM python:3.8-buster

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD . .
RUN pip install .
#CMD flask run -h 0.0.0.0 -p 8080
CMD gunicorn --workers 2 --timeout 90 --bind 0.0.0:8000 --access-logfile - wsgi:application


