from pathlib import Path

import pytest
from django.core.management import CommandError
from customerinfo.management.commands.importcsv import (
    validade_path_to_csv,
    import_csv_to_database,
)
from customerinfo.models import Customer
from customerinfo.tests.conftest import GoogleGeocodeAPIResponse
from customerinfo.utils import check_status_code


def test_validate_path_to_csv_with_no_path():
    with pytest.raises(CommandError) as cmd_error:
        validade_path_to_csv("")
    assert (
        cmd_error.value.args[0]
        == "Invalid Invocation. You must pass the path to .csv customers file."
    )


def test_validate_path_to_csv_that_doesnt_exist():
    with pytest.raises(CommandError) as cmd_error:
        validade_path_to_csv("invalidPath")
    assert cmd_error.value.args[0] == "invalidPath doesn't exist."


def test_import_customers_csv(client_query, monkeypatch_get_coordinates_from_address):
    current_folder = Path(__file__).resolve().parent
    path = f"{current_folder}/customers_test.csv"
    import_csv_to_database(path)

    all_customers = Customer.objects.all()

    assert all_customers
    assert len(all_customers) == 5


def test_call_geocode_api_ok_status(caplog):
    address_test = "Scranton, Pennsylvania"
    response = check_status_code(address_test, GoogleGeocodeAPIResponse.OK_STATUS.value)

    assert response
    assert not caplog.records


def test_call_geocode_api_zero_results_status(caplog):
    address_test = "Scranton, Pennsylvania"
    response = check_status_code(address_test, GoogleGeocodeAPIResponse.ZERO_RESULTS_STATUS.value)
    assert not response

    for record in caplog.records:
        assert record.levelname == "WARNING"
    assert "No results for address Scranton, Pennsylvania" in caplog.text


def test_call_geocode_api_error_status(caplog):
    address_test = "Scranton, Pennsylvania"
    response = check_status_code(address_test, GoogleGeocodeAPIResponse.REQUEST_DENIED_STATUS.value)
    assert not response

    for record in caplog.records:
        assert record.levelname == "WARNING"

    assert GoogleGeocodeAPIResponse.REQUEST_DENIED_STATUS.value["error_message"] in caplog.text
