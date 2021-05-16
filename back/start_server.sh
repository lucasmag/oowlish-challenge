#!/bin/sh
# start_server.sh

host="$1"

until PGPASSWORD=oowlishyay psql -h "$host" -U "oowlish" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - starting server"

python manage.py makemigrations
python manage.py migrate
python manage.py importcsv customers_sample.csv
python manage.py runserver 0.0.0.0:8000
