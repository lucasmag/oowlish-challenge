# oowlish-challenge/back

## Project setup for development

The Django backend requires a PostgreSQL database running on port 5432.
The Postgres credentials are:
```
POSTGRES_USER=oowlish
POSTGRES_PASSWORD=oowlishyay
```

You can easily create with `Docker`:
```bash
$ docker run --name postgres -e POSTGRES_USER=oowlish -e POSTGRES_PASSWORD=oowlishyay -p 5432:5432 -d postgres
```

Create and activate the virtualenv for the project.
```bash
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```

Install project dependencies:
```bash
$ pip install -r requirements.txt
```

Then apply the migrations:
```bash
$ python manage.py migrate
```

Import the customers.csv file:
```bash
$ python manage.py importcsv customers.csv
```

You can now run the development server:
```bash
$ python manage.py runserver
```
