<template>
  <div class="customers-box">
    <div class="customer-list">
      <div class="formFilter">
        <h2 class="title">Customers</h2>
        <b-form-input class="filter" v-model="filterCustomer" placeholder="Filter by any column"></b-form-input>
      </div>
      <b-table class="tabled"
        hover :filter="filterCustomer"
        sticky-header="60vh"
        head-variant="dark"
        :items="allCustomers"
        :fields="fields"
        :sort-by.sync="sortBy"
        :sort-desc.sync="sortDesc"
        :per-page="perPage"
        :current-page="currentPage"
        @row-clicked="showCustomerInfo"
        @filtered="tableFiltered"
        borderless
      ></b-table>

      <div class="table-footer">
        <b-form-radio-group
            size="sm"
            button-variant="dark"
            class="qtt-per-page-options"
            id="btn-radios-1"
            v-model="perPage"
            :options="perPageOptions"
            name="radios-btn-default"
            buttons
        ></b-form-radio-group>
        <b-pagination class="pagination-options"
            v-model="currentPage"
            :total-rows="totalCustomers"
            :per-page="perPage"
            align="center"
        ></b-pagination>
      </div>

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
          <CustomerInfo v-bind:customer-info-data="this.customer"/>
        </div>
        <b-button class="mt-3" variant="warning" block @click="hideCustomerInfoModal">Close</b-button>
      </b-modal>
    </div>
  </div>
</template>

<script>
import CustomerInfo from "@/components/CustomerInfo";
import {GET_ALL_CUSTOMERS, GET_CUSTOMER_BY_ID} from "@/queries";

export default {
  name: "CustomerList",
  components: {CustomerInfo},
  data () {
    return {
      sortBy: 'id',
      filterCustomer: '',
      sortDesc: false,
      allCustomers: [],
      totalCustomers: 0,
      customer: {},
      perPage: 10,
      perPageOptions: [10, 20, 50, 100],
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
  mounted() {
    this.totalCustomers = this.allCustomers.length
  },
  methods: {
    showCustomerInfoModal(customer) {
      this.customer = customer
      this.$bvModal.show('customerInfoModal')
    },
    hideCustomerInfoModal() {
      this.$bvModal.hide('customerInfoModal')
    },
    showCustomerInfo(customer){
      this.$apollo.query({
        query: GET_CUSTOMER_BY_ID,
        variables: { id: customer.id }
      }).then((response) => {
        this.showCustomerInfoModal(response.data.customer)
      }).catch((response) => {
        console.log("Error querying customer :(")
        console.log(response)
      })
    },
    tableFiltered(customers) {
      this.totalCustomers = customers.length
      this.currentPage = 1
    }
  },
  apollo: {
    allCustomers: GET_ALL_CUSTOMERS
  }
}
</script>

<style scoped>
.title {
  font-family: "Montserrat", sans-serif;
  font-size: 1.8em;
  margin: 0;
}
.formFilter {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.filter {
  width: 30%;
  background-color: #e0ded9;
  border-style: none;
}
.qtt-per-page-options {
  grid-area: perpage;
}

.pagination-options {
  grid-area: pagination;
  margin: 0;
  background-color: #F2EDE8;
}
.table-footer {
  display: grid;
  grid-template-columns: 0.3fr 1fr 0.3fr;
  grid-template-rows: auto;
  grid-template-areas:
    "perpage pagination ."
}

.tabled {
  margin: 1rem 0;
  border-radius: 15px;
  background-color: #eae8e3;
  box-shadow: 5px 5px 15px -3px rgba(0, 0, 0, 0.1);

  font-family: Montserrat-Regular, "sans-serif";
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
  background-color: #1f1f1f;
}

>>> .page-item .page-link{
  border-style: none;
  background-color: #343a40;
  color: #e0ded9;
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
