# Oowlish Challenge
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Coverage](https://github.com/lucasmag/oowlish-challenge/blob/master/back/customerinfo/tests/utils/coverage.svg)](https://github.com/lucasmag/oowlish-challenge)

Simple application that lists customer information, made with Django, Vue.js, GraphQL and PostgreSQL.

## Installation
### Docker
This application requires [Docker](https://docs.docker.com/engine/install/) and [Docker Compose](https://docs.docker.com/compose/install/).
You can verify the installation by printing their versions:
```bash
$ docker -v && docker-compose -v 
Docker version 20.10.5, build 55c4c88
docker-compose version 1.29.1, build c34c88b2
```
Once docker and docker compose have been installed, clone this repo:
```bash
git clone https://github.com/lucasmag/oowlish-challenge
```
By default, this process will expose ports 5432, 8000 and 60 for PostgreSQL database, Gunicorn and Nginx servers, respectively, so make sure that there is no process running on any of these ports, or change front/back Dockerfiles if necessary. 

When ready, simply use Docker Compose to build the images and run containers.

```bash
$ cd oowlish-challenge
$ docker-compose up -d
```

This will create the network, the volumes, build the images, run the entrypoint scripts for each _container_ and pull in the necessary dependencies.
> Note that this may take some minutes on the first run.

At the end of the process, you should see the containers creation with the following lines on console:

```bash
[...]
Creating postgres ... done
Creating django_server    ... done
Creating nginx  ... done
```

That's it! ✨
The application should be available at **http://localhost:80**

To stop the application and delete network/containers just run from the */oowlish-challenge* folder:

```bash
$ docker-compose down
```

---

> Note: To set up for development you can access each module (back/front) separately and follow the respective README.md instructions of each one.

## Usage ###
The application revolves around two API calls: one to list all customers, and the other to search for a specific customer by its id.

The main screen shows a table with the list of all customers, which were called through the first GraphQL query: `allCustomers`, that returns all customers present at the database, containing the following fields: *id*, *firstName*, *lastName*, *gender* and *city*.

[![Customer list](https://github.com/lucasmag/oowlish-challenge/blob/master/front/src/assets/customer-list.png)](https://github.com/lucasmag/oowlish-challenge)

When clicking on a specific customer, a modal is opened with the complete information of the customer. 
This information is queried through the GraphQL query `customer(id: Int)`, returning all fields.

[![Customer info](https://github.com/lucasmag/oowlish-challenge/blob/master/front/src/assets/customer-info.png)](https://github.com/lucasmag/oowlish-challenge)

The Django API also provides and GraphiQL endpoint to test the available queries for this application as well as see the docs for this schema. Just access in the browser:
```
http://localhost:8000/graphql/graphiql/
```

Write the query and execute(Ctrl + Enter), for example:
```gql
query{
    customer(id: 1){
        id
        firstName
    }
}
```
This query should return something like this.
```gql
{
  "data": {
    "customer": {
      "id": "1",
      "firstName": "Laura"
    }
  }
}
```
The docs are available in the top right corner of the page.

## How does it work? ###
As previously mentioned, when running Docker Compose, three containers are created: one for the frontend (Vue.js), one for the backend (Django) and the last one for the database (PostgreSQL).

The frontend and database steps for letting them in a ready-to-use state are quite simple. For front, the build is done by `npm` and then served by the HTTP `Nginx` server on port 80.
For the database, the container is created running a `PostgreSQL` image with the following credentials: POSTGRES_USER=oowlish and POSTGRES_PASSWORD=oowlishyay. This container is available on port 5432.

For the backend, there are a few more steps. These steps are described below:
1. The entrypoint is the `start-server.sh` file. Initially, this script verify if there is any `Postgres` service running on port 5432 with the previously described configurations. If database is not yet ready to use, this script will try to reconnect every 1 second, until the database is ready to use.
2. Build and run migrations
3. A django management command to import the *customers.csv* file into database is executed. Where *customers.csv* is the path to the csv file we want to import.
    ```python
    python manage.py importcsv customers.csv
    ```
4. The server runs on port 8000

## Tests ##
### Pytest ###
This application uses the easy-to-use test framework [pytest](https://docs.pytest.org/en/6.2.x/) to run its tests.

To run tests enter in the `django_server` container with the following command:
```bash
$ docker exec -it django_server bash
```

Run all tests with the following command:
```python
$ pytest
```

Was also made a runner adapter that allows us to run the tests using Django's `test` command:
```python
$ python ./manage.py test
```

### Coverage ###
There is also a tool to measure the code coverage of backend, which is [coverage](https://coverage.readthedocs.io/en/coverage-5.5/#). You can run tests with coverage running the following command:
```bash
coverage run -m pytest
```

To print the report results:
```bash
coverage report -m
```

### Dependencies ###
These are the main dependencies used in this project.

#### Backend
+ [Python 3.8](https://www.python.org/)
+ [Django](https://www.djangoproject.com/)
+ [Graphene-Django](https://docs.graphene-python.org/projects/django/en/latest/)
+ [Pytest](https://docs.pytest.org/en/6.2.x/index.html)
+ [Coverage](https://coverage.readthedocs.io/en/coverage-5.5/#)
+ [Psycopg2](https://pypi.org/project/psycopg2/)
+ [Black](https://black.readthedocs.io/en/stable/)

#### Frontend
+ [Vue.js](https://vuejs.org/)
+ [Vue-Apollo](https://apollo.vuejs.org/)
+ [Eslint](https://eslint.org/)
+ [BootstrapVue](https://bootstrap-vue.org/)
+ [NGINX](https://www.nginx.com/)

#### Database
+ [PostgreSQL 10](https://www.postgresql.org/)

#### Infrastructure
+ [Docker](https://docs.docker.com/engine/install/)
+ [Docker Compose](https://docs.docker.com/compose/install/)
