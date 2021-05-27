import json

from django.urls import reverse

from customerinfo.tests.conftest import populate_db_with_customers
from customerinfo.tests.utils.queries import get_customer_by_id, get_all_customers


def test_get_all_customers_graphql_api(client_query, mock_customer_generator):
    populate_db_with_customers(quantity=3)

    response = client_query(get_all_customers())
    result = json.loads(response.content)

    assert result["data"]["allCustomers"]
    assert len(result["data"]["allCustomers"]) == 3


def test_get_customer_by_id_graphql_api(client_query, mock_customer_generator):
    customer_mock = mock_customer_generator(first_name="Michael")
    customer_mock.save()

    response = client_query(get_customer_by_id(customer_mock.id))
    result = json.loads(response.content)

    assert result["data"]["customer"]

    customer_response = result["data"]["customer"]
    assert int(customer_response["id"]) == customer_mock.id
    assert customer_response["firstName"] == "Michael"


def test_try_to_get_nonexistent_customer_graphql_api(client_query):
    response = client_query(get_customer_by_id(9999))

    result = json.loads(response.content)

    assert not result["data"]["customer"]
    assert "errors" in result
    assert result["errors"][0]["message"] == "Customer matching query does not exist."


def test_get_all_customers_rest_api(client, client_query, mock_customer_generator):
    populate_db_with_customers(quantity=2)

    url = reverse("customers")
    response = client.get(url)
    assert response.status_code == 200

    customer_response = json.loads(response.content)
    assert len(customer_response) == 2


def test_get_customer_by_id_rest_api(client, client_query, mock_customer_generator):
    customer_mock = mock_customer_generator(first_name="Michael")
    customer_mock.save()

    url = reverse("customer_by_id", args=[customer_mock.id])
    response = client.get(url)
    assert response.status_code == 200

    customer_response = json.loads(response.content)
    assert int(customer_response["id"]) == customer_mock.id
    assert customer_response["firstName"] == "Michael"


def test_try_to_get_nonexistent_customer_rest_api(client, client_query):
    url = reverse("customer_by_id", args=[9999])
    response = client.get(url)
    assert response.status_code == 404

    result = json.loads(response.content)
    assert result["detail"] == "Não encontrado."
