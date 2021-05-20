<template>
  <div>
    <h4 class="title">{{this.title}}</h4>
    <p class="value" v-if="this.value">{{this.value}}</p>
    <p class="value-not-filled" v-if="!this.value">Value not filled</p>
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

.value .value-not-filled{
  margin: 0;
  font-size: 1.2em;
  overflow-wrap: break-word;
}

.value-not-filled {
  font-style: italic;
  color: rgba(0, 0, 0, 0.4);
}
</style>
