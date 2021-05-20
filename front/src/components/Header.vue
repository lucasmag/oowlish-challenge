<template>
  <div class="header">
    <h1>
      <span class="oowlish">Oowlish</span>
      <span class="challenge">Challenge</span>
    </h1>
  </div>
</template>

<script>
export default {
name: "Header"
}
</script>

<style scoped>
.header {
  width: 100%;
  height: 100px;
  margin: 0;
  padding: 0 50px;

  display: flex;
  align-items: center;
}

h1 {
  margin: 0;
  width: max-content;
  font-family: "Montserrat", sans-serif;
  font-size: 1.4em;
}

.oowlish {
  color: #171717;
}

.challenge {
  color: #FF9D13;
}
</style>
