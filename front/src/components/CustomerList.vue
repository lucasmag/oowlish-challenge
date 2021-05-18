<template>
  <div class="customers-box">
    <div class="customer-list">
      <b-table class="tabled"
        hover
        sticky-header="60vh"
        head-variant="dark"
        :items="allCustomers"
        :fields="fields"
        :sort-by.sync="sortBy"
        :sort-desc.sync="sortDesc"
        :per-page="perPage"
        :current-page="currentPage"
        @row-clicked="showCustomerInfo"
        responsive="sm"
        borderless
      ></b-table>
      <b-pagination
          pills
          v-model="currentPage"
          :total-rows="totalCustomers"
          :per-page="perPage"
          align="center"
      ></b-pagination>

      <b-modal
          id="customerInfoModal"
          header-bg-variant="dark"
          header-text-variant="light"
          centered
          size="lg"
          hide-footer>
        <template #modal-title>
          Customer Information
        </template>

        <div class="d-block text-center">
          <CustomerInfo/>
        </div>
        <b-button class="mt-3" variant="warning" block @click="hideCustomerInfoModal">Close</b-button>
      </b-modal>
    </div>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import CustomerInfo from "@/components/CustomerInfo";

export default {
  name: "CustomerList",
  components: {CustomerInfo},
  data () {
    return {
      selectedCustomerId: 0,
      sortBy: 'id',
      sortDesc: false,
      allCustomers: [],
      customer: {
        id: null,
        firstName: '',
        lastName: '',
        gender: '',
        email: '',
        city: '',
        title: '',
        latitude: null,
        longitude: null
      },
      perPage: 20,
      currentPage: 1,
      fields: [
        { key: 'id', sortable: true },
        { key: 'firstName', sortable: true },
        { key: 'lastName', sortable: false },
        { key: 'gender', sortable: false },
        { key: 'city', sortable: true },
      ]
    }
  },
  computed: {
    totalCustomers() {
      return this.allCustomers.length
    }
  },
  methods: {
    showCustomerInfo(customer){
      this.selectedCustomerId = customer.id
      this.showCustomerInfoModal()
    },
    showCustomerInfoModal() {
      this.$bvModal.show('customerInfoModal')
    },
    hideCustomerInfoModal() {
      this.$bvModal.hide('customerInfoModal')
    },
  },
  apollo: {
    allCustomers: gql`
      query getAllCustomers{
        allCustomers {
          id
          firstName
          lastName
          gender
          city
        }
      }
    `,
    customer: {
      query: gql`
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
      `,
      variables() {
        return {
          id: this.selectedCustomerId
        }
      },
      skip () {
        return !this.selectedCustomerId
      },
    }
  }
}
</script>

<style scoped>

.tabled {
  border-radius: 15px;
  background-color: #eae8e3;
  box-shadow: 5px 5px 15px -3px rgba(0, 0, 0, 0.1);

  font-family: Montserrat-Regular, "sans-serif";
  height: 60vh;
}

.customers-box {
  width: 100%;
  height: 100%;

  display: flex;
  align-items: center;
  justify-content: center;
}

.customer-list {
  border-radius: 35px;
  width: -moz-available;
  width: -webkit-fill-available;
  width: fill-available;
}

#customerInfoModal {
  width: 90%;
}

>>> .page-item.active .page-link{
  background-color: #f6b44c;
}

>>> .page-item:not(.active) .page-link:hover{
  background-color: #ffe0b5;
}

>>> .page-item .page-link{
  border-style: none;
}

>>> .page-link {
  color: #242424;
}

/* width */
::-webkit-scrollbar {
  width: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  background-color: #F2EDE8;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #f6b44c;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #FF9D13;
}

</style>
