FROM python:3.8

RUN apt-get -o Acquire::Check-Valid-Until=false -o Acquire::Check-Date=false update - &&\
apt-get -y install postgresql-client-11 libpq-dev

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt

RUN ["chmod", "+x", "start_server.sh"]