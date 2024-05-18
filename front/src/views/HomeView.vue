<script setup>
import TheWelcome from '../components/TheWelcome.vue'
</script>

<template>
  <main>
    <h1>{{ word }}</h1>
    <TheWelcome />
  </main>
</template>

<script>
export default {
  data: () => ({
    word: null
  }),
  mounted() {
    this.axios.get('http://127.0.0.1:8000/secr').then(resp => {
      this.word = resp.data
    })
  }
}
</script>