
<script>
import axios from 'axios'
import TransparentBlogCard from "@/examples/cards/blogCards/TransparentBlogCard.vue";



export default {
  components: {
    TransparentBlogCard,
  },

  data() {
    return {
      latestarticles: [],
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
          <h3 class="mb-5">Check my latest Articles</h3>
        </div>
      </div>

      <div class="row">
        <router-link
          v-for="article in latestarticles"
          :key="article.id"
          :to="`/landing-pages/articledetails/article/${article.id}`"
          class="col-lg-3 col-sm-6 my-card"
        >
            <div class="my-image">
                <img :src="article.get_image"  />
            </div>

          <div class="article-title">{{ article.title }}</div>
          <p>{{ article.description }}</p>
          
        </router-link>
      </div>

    </div>
  </section>
</template>
<style>
.my-card {

  padding: 40px 40px 60px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);

  width: 400px; 
  height: 380px;

  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-start;

  cursor: pointer;
  
  overflow: hidden;
  margin-left: auto;
  margin: 15px 15px 35px;
  margin-bottom: 20px;
  transition: transform 0.2s, box-shadow 0.2s;
}

.my-card:hover {
  
  transform: scale(1.05);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.my-image {
  margin-right: 2px;
 
  overflow: hidden;
  margin: 0;
  display: flex;
  width: 100%;
  height: 300px; 
}
.my-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.article-title {
  
  font-size: 15px;
  font-weight: bold;
  color: #333; 
  margin-top: 15px; 
}
.my-card p {
  
  max-height: 100px; 
  color: #333;
  
}

</style>
