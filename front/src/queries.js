import { gql } from "apollo-boost";

export const GET_ALL_CUSTOMERS = gql`
  query {
    allCustomers {
      id
      firstName
      lastName
      gender
      city
    }
  }
`;

export const GET_CUSTOMER_BY_ID = gql`
  query getCustomerById($id: Int){
    customer(id: $id) {
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
`;
