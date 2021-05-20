<template>
  <div id="app">
    <div id="header">
      <Header></Header>
    </div>

    <div id="body">
      <CustomerList/>
    </div>

    <div id="footer"/>
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

@font-face {
  font-family: "Montserrat-Bold";
  src: local("Montserrat"),
  url(fonts/Montserrat/Montserrat-Bold.ttf) format("truetype");
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin: 0;
  padding: 0;

  font-size: 16px;
  line-height: 1.42857143;
  width: 100%;
  display: grid;
  grid-template-columns: minmax(0, 0.3fr) minmax(0, 1fr) minmax(0, 0.3fr);
  grid-template-rows: min-content minmax(0, 100%) min-content;
  grid-template-areas:
    "header header header"
    ". body ."
    "footer footer footer"
}

#header {
  grid-area: header;
}

#body {
  grid-area: body;
  width: 100%;
  height: 100%;
  max-height: 100%;
}

#footer {
  grid-area: footer;
  height: 100px;
}


html {
  height: 100%;
  max-height: 100%;
}


body {
  margin: 0;
  padding: 0;
  height: 100%;
  max-height: 100%;
  background-color: #F2EDE8;
}

</style>
