# ./Dockerfile
FROM python:3

RUN apt-get -y update
RUN apt-get -y install vim

RUN mkdir /srv/django-server
ADD . /srv/django-server

WORKDIR /srv/django-server

## Install packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python","./test_server/manage.py","runserver","0.0.0.0:8000"]
