<template>
  <div id="app">
    <Header class="header"></Header>
    <CustomerList/>
  </div>
</template>

<script>
import CustomerList from "@/components/CustomerList";
import Header from "@/components/Header";

export default {
  name: 'App',
  components: {
    Header,
    CustomerList,
  }
}
</script>

<style>

@font-face {
  font-family: "Montserrat";
  src: local("Montserrat"),
  url(fonts/Montserrat/Montserrat-ExtraBold.ttf) format("truetype");
}

@font-face {
  font-family: "Montserrat-Regular";
  src: local("Montserrat"),
  url(fonts/Montserrat/Montserrat-Regular.ttf) format("truetype");
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0;
  padding: 0;
}

body {
  margin: 0;
  padding: 0;
  background-color: #F2EDE8;
}

html, body {
  height: 100%;
}

.header {
  top: 0;
}
</style>
