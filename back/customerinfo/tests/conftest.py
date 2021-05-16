from random import randint, uniform

import pytest
from graphene_django.utils.testing import graphql_query

from customerinfo.models import Customer
from customerinfo.utils import Coordinates


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture
def client_query(client):
    def func(*args, **kwargs):
        return graphql_query(*args, **kwargs, client=client)

    return func


@pytest.fixture(scope="function")
def monkeypatch_get_coordinates_from_address(monkeypatch):
    def fake_get_coordinates_from_address(*args, **kwargs):
        latitude = round(uniform(-90, 90), 7)
        longitude = round(uniform(-180, 180), 7)

        return Coordinates(latitude, longitude)

    monkeypatch.setattr(
        "customerinfo.management.commands.importcsv.get_coordinates_from_address",
        fake_get_coordinates_from_address,
    )


@pytest.fixture(scope="function")
def mock_customer():
    customer = Customer()
    customer.first_name = "Michael"
    customer.last_name = "Scott"
    customer.email = "worldsbestboss@mifflin.com"
    customer.gender = "Male"
    customer.company = "Dunder Mifflin"
    customer.city = "Scranton, Pennsylvania"
    customer.title = "Regional Manager"
    customer.latitude = "41.4091379"
    customer.longitude = "-75.6624229"
    customer.save()

    return customer


@pytest.yield_fixture(scope="function")
def mock_customer_generator():
    def make_mock(
        first_name="Michael",
        last_name="Scott",
        email="worldsbestboss@mifflin.com",
        gender="Male",
        company="Dunder Mifflin",
        city="Scranton, Pennsylvania",
        title="Regional Manager",
        latitude="41.4091379",
        longitude="-75.6624229",
    ):
        return Customer(
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender,
            company=company,
            city=city,
            title=title,
            latitude=latitude,
            longitude=longitude,
        )

    yield make_mock


class PytestTestRunner:
    """Runs pytest to discover and run tests."""

    def __init__(self, verbosity=1, failfast=False, keepdb=False, **kwargs):
        self.verbosity = verbosity
        self.failfast = failfast
        self.keepdb = keepdb

    @classmethod
    def add_arguments(cls, parser):
        parser.add_argument(
            "--keepdb", action="store_true", help="Preserves the test DB between runs."
        )

    def run_tests(self, test_labels):
        """Run pytest and return the exitcode.

        It translates some of Django's test command option to pytest's.
        """
        import pytest

        argv = []
        if self.verbosity == 0:
            argv.append("--quiet")
        if self.verbosity == 2:
            argv.append("--verbose")
        if self.verbosity == 3:
            argv.append("-vv")
        if self.failfast:
            argv.append("--exitfirst")
        if self.keepdb:
            argv.append("--reuse-db")

        argv.extend(test_labels)
        return pytest.main(argv)
