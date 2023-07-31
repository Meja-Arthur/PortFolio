<!---<script setup>
// example component
import HorizontalTeamCard from "@/examples/cards/teamCards/HorizontalTeamCard.vue";

// images
import emma from "@/assets/img/team-5.jpg";
import william from "@/assets/img/bruce-mars.jpg";
import ivana from "@/assets/img/ivana-squares.jpg";
import marquez from "@/assets/img/ivana-square.jpg";
import axios from 'axios';
import { ref, onMounted } from 'vue';

// Other imports...

// Create a ref to hold the user data
const users = ref([]);

onMounted(async () => {
  // Fetch user data from the backend API
  try {
    const response = await axios.get('/api/users/user/'); // Replace with your actual API endpoint URL
    users.value = response.data;
  } catch (error) {
    console.error('Error fetching user data:', error);
  }
});

// Function to navigate to the user profile page
const navigateToUserProfile = (userId) => {
  router.push({ name: 'userprofile', params: { id: userId } });
};
</script>--->



<template>
  <section class="pb-10 position-relative bg-gradient-dark mx-n3">
    <div class="container">

      <div class="row">
        <div class="col-md-8 text-start mb-5 mt-5">
          <h3 class="text-white z-index-1 position-relative">The Executive Team</h3>
          <p class="text-white opacity-8 mb-0">
           SomeThing Should be Her 
          </p>
        </div>
      </div>
    
      <div class="row">
        <router-link
          v-for="user in users"
          :key="user.id"
          :to="`/landing-pages/profiledetails/user-portfolio/${user.id}`"
          class="col-lg-3 col-sm-6 my-card"
        >
          <div class="my-image">
              <img :src="user.get_image" />
          </div>
          <div class="article-title">{{ user.name }}</div>
          <p>{{ user.position }}</p>
        </router-link>
      </div>

    </div>
  </section>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      users: [],
    };
  },
  mounted() {
    this.fetchUsers();
  },
  methods: {
    fetchUsers() {
      axios.get('/api/v1/user-portfolio/')
        .then(response => {
          this.users = response.data;
        })
        .catch(error => {
          console.error('Error fetching users:', error);
        });
    },
  },
};
</script>
<style>

.my-card {
  padding: 40px 40px 60px;
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
  background-color: aliceblue;
  border-radius: 5px;

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

</style>
