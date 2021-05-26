import json

from django.urls import reverse

from customerinfo.tests.utils.queries import get_customer_by_id, get_all_customers


def populate_db_with_mocks(mock_customer_generator):
    mock_customer_generator(
        first_name="Dwight",
        last_name="Schrute",
        email="schrutefarms@tripadvisor.com",
        title="Assistant (to the) Regional Manager",
    ).save()

    mock_customer_generator(
        first_name="Jim",
        last_name="Halpert",
        email="bigtuna@athlead.com",
        title="President of New Acquisitions",
    ).save()

    mock_customer_generator(
        first_name="Pam",
        last_name="Beesly",
        email="pamcasso@mifflin.com",
        gender="Female",
        title="Office Administrator",
    ).save()


def test_get_all_customers_graphql_api(client_query, mock_customer_generator):
    populate_db_with_mocks(mock_customer_generator)

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
    populate_db_with_mocks(mock_customer_generator)

    url = reverse('customers')
    response = client.get(url)
    assert response.status_code == 200

    customer_response = json.loads(response.content)
    assert len(customer_response) == 3


def test_get_customer_by_id_rest_api(client, client_query, mock_customer_generator):
    customer_mock = mock_customer_generator(first_name="Michael")
    customer_mock.save()

    url = reverse('customer_by_id', args=[customer_mock.id])
    response = client.get(url)
    assert response.status_code == 200

    customer_response = json.loads(response.content)
    assert int(customer_response["id"]) == customer_mock.id
    assert customer_response["firstName"] == "Michael"
