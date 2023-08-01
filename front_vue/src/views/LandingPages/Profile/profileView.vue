<template>
   <DefaultNavbar transparent />

   <Header>
      <div
        class="page-header min-height-400"
        :style="{ backgroundImage: `url(${image})` }"
        loading="lazy"
      >
        <span class="mask bg-gradient-dark opacity-8"></span>
      </div>
  </Header>

  <div class="card card-body blur shadow-blur mx-3 mx-md-4 mt-n6 mb-4">

    <section class="py-sm-7 py-5 position-relative mb-5">

            <div class="container">
                <div class="row">
                  <div class="col-12 mx-auto">

                    <div class="mt-n8 mt-md-n9 text-center">
                      <div class="blur-shadow-avatar">
                        <MaterialAvatar
                          size="xxl"
                          class="shadow-xl position-relative z-index-2"
                          :image=" user.get_image "
                          alt="Avatar"
                        />
                      </div>
                    </div>

                    <div class="row py-7">

                    <div class="col-lg-7 col-md-7 z-index-2 position-relative px-md-2 px-sm-5 mx-auto">
                      
                          <div  class="d-flex justify-content-between align-items-center mb-2">
                            <h3 class="mb-0">{{ user.name }}</h3>
                            <div class="d-block">
                              <MaterialButton  class="text-nowrap mb-0" variant="outline" color="success" size="sm">Follow</MaterialButton>
                            </div>
                          </div>

                          <div class="row mb-4">
                            <div class="col-auto"><span class="h6 me-1">323</span><span>Posts</span></div>
                            <div class="col-auto"><span class="h6 me-1">3.5k</span><span>Followers</span></div>
                            <div class="col-auto"><span class="h6 me-1">260</span><span>Following</span></div>
                          </div>

                          <strong>About</strong>
                          <p class="text-lg mb-0">
                            {{ user.bio }}
                          </p> 
                    </div>
          
                  </div>

                </div>
                </div>
            </div>

    </section>

    <section class="pb-10 position-relative bg-gradient-dark mx-n3 mt-10">
      <div class="container">

          <div class="row">
            <div class="col-lg-6">
              <h3 class="mb-5 text-white mt-5">Article written by {{ user.name }}</h3>
            </div>
          </div>

          <div class="row">
            <router-link 
              v-for="article in user.articles" 
              :key="article.id" 
              :to="`/landing-pages/articledetails/article/${article.id}`" 
              class="col-lg-3 col-sm-6 my-card"
            >
                <div class="my-image">
                  <img :src="article.get_image" />
                </div>

                <div class="article-title">{{ article.title }}</div>
                <p>{{ article.description  }}</p>
              <!-- Display article information here -->

            </router-link>
          </div>
      </div>
    </section>

    

  </div>
  
  <DefaultFooter/>
</template>

<script>
import DefaultNavbar from "../../../examples/navbars/NavbarDefault.vue";
import Header from "../../../examples/Header.vue";
import DefaultFooter from "../../../examples/footers/FooterDefault.vue";
import MaterialAvatar from "../../../components/MaterialAvatar.vue";
import MaterialButton from "../../../components/MaterialButton.vue"

import image from "@/assets/img/portfolio1.jpg";
import axios from 'axios';
export default {
  components:{
    DefaultNavbar,  
    DefaultFooter,
    MaterialAvatar,
    MaterialButton,
 
  },
  data() {

    return {
      image: image,
      user:{},
    };
  },
  mounted(){
    this.fetchuser();
    
  },
  methods: {
    fetchuser() {
      const userId = this.$route.params.id
      axios
      .get(`/api/v1/user-portfolio/${userId}/`)
      .then((response) => {
        this.user = response.data;
      })
      .catch((error) =>{
        console.error('Error fetching article:', error);

      });
    }
  }

}
</script>

<style>

</style>