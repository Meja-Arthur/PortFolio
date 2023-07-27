
<script>
import axios from 'axios'
import TransparentBlogCard from "@/examples/cards/blogCards/TransparentBlogCard.vue";
import bg0 from "@/assets/img/pen.jpg";

export default {
  components: {
    TransparentBlogCard,

  },

  

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

<template>
  <section class="pb-5 position-relative bg-gradient-gray mx-n3">
    <div class="container">

      <div class="row">
        <div class="col-lg-6">
          <h2 class="mb-5">Check my latest Articles</h2>
        </div>
      </div>

      <div class="row">
        <div class="col-lg-3 col-sm-6" v-for="article in latestarticles" :key="article.id">
          <router-link :to="`/landing-pages/articledetails/article/${article.id}`">
            <TransparentBlogCard
              :image="bg0" 
              :title="article.title" 
            />
          </router-link>
        </div>
      </div>

    </div>
  </section>
</template>
