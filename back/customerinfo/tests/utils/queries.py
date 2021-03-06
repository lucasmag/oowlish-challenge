def get_all_customers() -> str:
    return """
        query {
            allCustomers {
                id
                firstName
                lastName
                email
                gender
                company
                city
                title
                latitude
                longitude
            }
        }
    """


def get_customer_by_id(customer_id: int) -> str:
    return (
        """
        query {
            customer (id: %d) {
                id
                firstName
                lastName
                email
                gender
                company
                city
                title
                latitude
                longitude
            }
        }
        """
        % customer_id
    )
