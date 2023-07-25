<template>
  <div>
    <h3>Some Of Our Written Articles</h3>
    <ul>
      <li v-for="article in latestarticles" :key="article.id">
        <router-link :to="`/landing-pages/articledetails/article/${article.id}`">
          {{ article.title }}
        </router-link>
      </li>
    </ul>
  </div>
  </template>

<script>
import axios from 'axios'

export default {

  data() {
    return {
      latestarticles: []
    }
  },

  mounted() {
    this.getLatestarticles()

    document.title = ' WrittenArticles|ScribeHaven'
  },

  methods: {
    async getLatestarticles() {

      await axios 
        .get('/api/v1/latest-articles/')
        .then(response => {
            console.log(response.data)
           this.latestarticles = response.data
        })
        .catch(error => {
          console.log(error)
        })
    },


  }
}
</script>

<style>

</style>