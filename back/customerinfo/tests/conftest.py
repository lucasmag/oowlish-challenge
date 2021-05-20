from enum import Enum
from random import uniform

import pytest
from graphene_django.utils.testing import graphql_query

from customerinfo.models import Customer
from customerinfo.utils import Coordinates


SCRANTON_ADDRESS_EXAMPLE = "Scranton, Pennsylvania"


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
def monkeypatch_request(monkeypatch):
    import requests

    def post(*args, **kwargs):
        class Request:
            address = kwargs["params"]["address"]

            def json(self):
                if self.address == SCRANTON_ADDRESS_EXAMPLE:
                    return GoogleGeocodeAPIResponse.OK_STATUS.value

                return GoogleGeocodeAPIResponse.ZERO_RESULTS_STATUS.value

        return Request()

    monkeypatch.setattr(requests, "post", post)


@pytest.fixture(scope="function")
def mock_customer_generator():
    def make_mock(  # Default customer mock
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


class GoogleGeocodeAPIResponse(Enum):
    REQUEST_DENIED_STATUS = {
        "error_message": "You must enable Billing on the Google Cloud Project at https://console.cloud.google.com/project/_/billing/enable Learn more at https://developers.google.com/maps/gmp-get-started",
        "results": [],
        "status": "REQUEST_DENIED"
    }

    OK_STATUS = {
        "results": [
            {
                "formatted_address": "Scranton, PA, USA",
                "geometry": {
                    "location": {
                        "lat": 41.408969,
                        "lng": -75.6624121
                    },
                }
            }
        ],
        "status": "OK"
    }

    ZERO_RESULTS_STATUS = {
        "results": [],
        "status": "ZERO_RESULTS"
    }
