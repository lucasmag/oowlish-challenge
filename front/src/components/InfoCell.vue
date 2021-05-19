<template>
<div>
  <h4 class="title">{{this.title}}</h4>
  <p class="value">{{this.value}}</p>
</div>
</template>

<script>
export default {
  name: "InfoCell",
  props: ['cellTitle', 'cellValue'],
  data () {
    return {
      title: this.cellTitle,
      value: this.cellValue
    }
  }
}
</script>

<style scoped>
.title {
  font-size: 0.9em;
  margin: 0;
  font-weight: bold;
  color: #242424;
}

.value {
  margin: 0;
  font-size: 1.2em;
  overflow-wrap: break-word;
}
</style>
