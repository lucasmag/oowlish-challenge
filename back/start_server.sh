#!/bin/sh
# start_server.sh

environment="$1"
echo "$environment"

if [ "$environment" = "production" ]; then
  export ENV_PATH=".env.prod"
  database_host="db"
else
  database_host="localhost"
fi


until PGPASSWORD=oowlishyay psql -h "$database_host" -U "oowlish" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - starting server"

python manage.py makemigrations
python manage.py migrate
python manage.py importcsv customers_sample.csv
python manage.py runserver 0.0.0.0:8000
