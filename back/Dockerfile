FROM python:3.8

RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8 &&
echo "deb http://apt.postgresql.org/pub/repos/apt/ buster-pgdg main" > /etc/apt/sources.list.d/pgdg.list &&
apt-get -y update - &&
apt-get -y install postgresql-client-11 libpq-dev

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt

RUN ["chmod", "+x", "start_server.sh"]