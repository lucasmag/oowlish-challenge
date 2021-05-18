<template>
<div id="customer-info">
  <div class="cell id">
    <InfoCell cell-title="ID" v-bind:cell-value="this.customer.id"/>
  </div>

  <div class="cell first-name">
    <InfoCell cell-title="First Name" v-bind:cell-value="this.customer.firstName"/>
  </div>

  <div class="cell last-name">
    <InfoCell cell-title="Last Name" v-bind:cell-value="this.customer.lastName"/>
  </div>

  <div class="cell email">
    <InfoCell cell-title="Email" v-bind:cell-value="this.customer.email"/>
  </div>

  <div class="cell gender">
    <InfoCell cell-title="Gender" v-bind:cell-value="this.customer.gender"/>
  </div>

  <div class="cell title">
    <InfoCell cell-title="Title" v-bind:cell-value="this.customer.title"/>
  </div>

  <div class="cell city">
    <InfoCell cell-title="City" v-bind:cell-value="this.customer.city"/>
  </div>

  <div class="cell latitude">
    <InfoCell cell-title="Latitude" v-bind:cell-value="this.customer.latitude"/>
  </div>

  <div class="cell longitude">
    <InfoCell cell-title="Longitude" v-bind:cell-value="this.customer.longitude"/>
  </div>
</div>
</template>

<script>
import InfoCell from "@/components/InfoCell";
export default {
  name: "CustomerInfo",
  components: {InfoCell},
  data () {
    return {
      customer: {
        id: 12,
        firstName: 'Lucas',
        lastName: 'Magalhaes',
        gender: 'Female',
        email: 'lucasmagjhjjhjhjhjalhaes@gmail.com',
        city: 'Itapiponkn kkjj ca, CE',
        title: 'Engenheiro da Computação dek mais testh ush uhu',
        latitude: -12.2328321,
        longitude: 30.32312312
      }
    }
  }
}
</script>

<style scoped>
.id {
  grid-area: id;
}
.first-name {
  grid-area: first-name;
}
.last-name {
  grid-area: last-name;
}
.gender {
  grid-area: gender;
}
.email {
  grid-area: email;
}
.city {
  grid-area: city;
}
.title {
  grid-area: title;
}
.latitude {
  grid-area: latitude;
}
.longitude {
  grid-area: longitude;
}
.cell {
  padding: 5px;
  text-align: start;
}

#customer-info {
  grid-gap: 10px;
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  grid-template-rows: auto;
  grid-template-areas:
    "id first-name first-name first-name last-name last-name last-name gender"
    "email email email email title title title title"
    "city city city city latitude latitude longitude longitude"
}
</style>
