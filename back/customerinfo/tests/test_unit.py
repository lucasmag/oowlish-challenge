import pytest
from django.core.management import CommandError
from customerinfo.management.commands.importcsv import (
    validade_path_to_csv,
    import_csv_to_database,
)
from customerinfo.models import Customer


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
    path = "customers_sample.csv"
    import_csv_to_database(path)

    all_customers = Customer.objects.all()

    assert all_customers
    assert len(all_customers) == 5
